import pygame
from random import randint, choice
pygame.init()

H, W = 950, 700


class Button(pygame.sprite.Sprite):
    def __init__(self, image, pushed_image, clicked_image, xy):
        '''class for storing all rects/sprites with buttons
        all images are just links to image
        xy - bottomleft'''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(bottomleft=xy)
        self.pushed_image = pygame.image.load(pushed_image)
        self.pushed_rect = self.pushed_image.get_rect(bottomleft=xy)
        self.clicked_image = pygame.image.load(clicked_image)
        self.clicked_rect = self.clicked_image.get_rect(bottomleft=xy)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, image_hurt, health, enemies, items_group, speed='rand', pocket=[]):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.image_hurt = pygame.image.load(image_hurt)
        self.items_group = items_group
        self.health = health
        self.xy = [H, W // 2]
        self.pocket = pocket
        self.rect = self.image.get_rect(center=self.xy)
        self.recently_hurt = False
        if speed == 'rand':
            self.speed = randint(1, 8)
        else:
            self.speed = speed
        
        if self.pocket == []:
            self.damage = 1
        else:
            self.damage = self.pocket[0].get_power()
            self.pocket[0].set_player(self, items_group)

        self.add(enemies)
        self.group = enemies
    
    def update(self, xy, dad, scroll):
        if scroll:
            self.rect[0] -= dad.speed
        else:
            if self.xy[0] > xy[0]:
                self.xy[0] -= self.speed
            else:
                self.xy[0] += self.speed
            if self.xy[1] > xy[1]:
                self.xy[1] -= self.speed
            else:
                self.xy[1] += self.speed
            self.rect = self.image.get_rect(center=self.xy)

            if abs(self.xy[0] - xy[0]) <= 200 and abs(self.xy[1] - xy[1]) <= 200 and randint(0, 100) > 90:
                dad.hurt(self.damage)

    def hurt(self, amount, ground_items):
        self.health -= amount
        if self.health <= 0:
            self.death(ground_items)
        
        self.image, self.image_hurt = self.image_hurt, self.image
        self.recently_hurt = True
        print('hurt')
    
    def change_if_hurt(self):
        if self.recently_hurt:
            self.image, self.image_hurt = self.image_hurt, self.image
            self.recently_hurt = False

    def death(self, items_ground):
        self.group.remove(self)
        if len(self.pocket) == 1:
            items_ground.add(self.pocket[0])
            self.items_group.remove(self.pocket[0])
        self.kill()
    
    def scroll(self, speed):
        self.rect[0] -= speed


class MainHero(pygame.sprite.Sprite):
    def __init__(self, image, image_hurt, image_run, pos, speed, itemgroup, pocket=[]):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.image_run = pygame.image.load(image_run)
        self.image_hurt = pygame.image.load(image_hurt)
        self.rect = self.image.get_rect(center=pos)
        self.pos = pos
        self.health = 20
        self.food = 20
        self.speed = speed
        self.pocket = pocket
        self.pocket[0].set_player(self, itemgroup)
        self.itemgroup = itemgroup
        self.hurt_right_now = False
        self.death = False
    
    def hurt(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.death = True
        self.hurt_right_now = True
        print('health: ', self.health)

    def hungry(self):
        if self.food == 0:
            self.hurt(1)
        else:
            self.food -= 1
            print('f:', self.food)
        
    def change_items(self):
        self.itemgroup.remove(self.pocket[0])
        self.pocket.append(self.pocket.pop(0))
        self.pocket[0].set_player(self, self.itemgroup)
        
    
    def new_item(self, item, items_ground):
        if len(self.pocket) == 5:
            self.pocket[0].set_xy((self.rect[0], self.rect[1]))
            items_ground.add(self.pocket[0])
            self.pocket[0] = item
        else:
            self.pocket.append(item)
    
    def use_item(self):
        if len(self.pocket) > 0 and type(self.pocket[0]) == Object:
            self.health += self.pocket[0].healing
            self.itemgroup.remove(self.pocket[0])
            self.food += self.pocket[0].food
            self.pocket.pop(0)
            if self.health > 20:
                self.health = 20
            if self.food > 20:
                self.food = 20
    
    def get_power(self):
        if len(self.pocket) == 0:
            return 1
        return self.pocket[0].power

    def get_distance(self):
        if len(self.pocket) == 0:
            return 150
        return self.pocket[0].distance

class Weapon(pygame.sprite.Sprite):
    def __init__(self, image, power=1, distance=200, is_with_player=False, xy=(0, 0)):
        pygame.sprite.Sprite.__init__(self)
        self.is_with_player = is_with_player
        self.im = image
        self.image = pygame.image.load(image)
        self.power = power
        self.distance = distance
        self.xy = xy
    
    def get_power(self):
        return self.power
    
    def with_player_change(self, xy=None):
        self.is_with_player = not(self.is_with_player)
        if not(self.is_with_player):
            self.xy = xy
    
    def set_player(self, player, group):
        self.is_with_player = player
        group.add(self)
        self.rect = self.image.get_rect(center=(player.rect[0] + 100, player.rect[1] + 120))
    
    def update(self, items_on_ground, scroll):
        if scroll:
            self.rect[0] -= 15
        else:
            if self.is_with_player is not None and self.is_with_player.health <= 0:
                self.is_with_player = None
                items_on_ground.add(self)
            elif self.is_with_player is not None:
                self.rect = self.image.get_rect(
                            center=(self.is_with_player.rect[0] + 100,
                            self.is_with_player.rect[1] + 120))
            
    def copy(self):
        return Weapon(self.im, power=self.power, distance=self.distance)
    
    def set_xy(self, xy):
        '''for items on the ground'''
        self.is_with_player = None
        self.rect = self.image.get_rect(center=xy)

    def get_info(self):
        res = []
        if self.power != 0:
            res.append('p' + str(self.power))
        res.append('d' + str(self.distance))

        return res


class Object(pygame.sprite.Sprite):
    def __init__(self, image, healing=0, food=0, power=1, distance=150, is_with_player=False, xy=(0, 0)):
        pygame.sprite.Sprite.__init__(self)
        self.im = image
        self.image = pygame.image.load(image)
        self.power = power
        self.food = food
        self.healing = healing
        self.distance = distance
        self.is_with_player = is_with_player
        self.xy = xy

    def with_player_change(self, xy=None):
        self.is_with_player = not(self.is_with_player)
        if not(self.is_with_player):
            self.xy = xy
    
    def set_player(self, player, group):
        self.is_with_player = player
        group.add(self)
        self.rect = self.image.get_rect(center=(player.rect[0] + 100, player.rect[1] + 120))
    
    def update(self, items_on_ground, scroll):
        if scroll:
            self.rect[0] -= 15
        else:
            if self.is_with_player is not None and self.is_with_player.health <= 0:
                self.is_with_player = None
                items_on_ground.add(self)
            elif self.is_with_player is not None:
                self.rect = self.image.get_rect(
                            center=(self.is_with_player.rect[0] + 100,
                            self.is_with_player.rect[1] + 120))
        
    def get_power(self):
        return self.power
    
    def copy(self):
        return Object(self.im, healing=self.healing, food=self.food, power=self.power, distance=self.distance)
    
    def set_xy(self, xy):
        '''for items on the ground'''
        self.is_with_player = None
        self.rect = self.image.get_rect(center=xy)
    
    def get_info(self):
        res = []
        if self.healing != 0:
            res.append('h' + str(self.healing))
        if self.food != 0:
            res.append('f' + str(self.food))
        res.append('d' + str(self.distance))

        return res


class Object_on_ground(pygame.sprite.Sprite):
    def __init__(self, image, pos, open_image=None):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)
        if open_image is not None:
            self.open_image = open_image
            self.open = False
    
    def update(self, speed):
        self.rect[0] -= speed
        if self.rect[0] <= -200:
            self.kill()
