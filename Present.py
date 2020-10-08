import pygame
from random import randint
from classes_setup import *
from sprites_setup import *

pygame.init()

# ________constants and screen_________
BLACK = (10, 10, 10)
WHITE = (255, 255, 255)
H, W = 950, 700

clock = pygame.time.Clock()

sc = pygame.display.set_mode((H, W))
sc.fill(BLACK)

# ________sprites_________

pygame.display.update()


def menu():
    global dad
    dad = get_dad()

    sc.blit(menu_fone, menu_fone_rect)
    sc.blit(menu_start_button.image, menu_start_button.rect)
    sc.blit(menu_dad, menu_dad_rect)

    pygame.display.update()

    # status variables
    waving = False
    button_pushed = False
    button_clicked = False

    while True:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()

            if not(waving) and i.type == pygame.MOUSEMOTION and\
                    menu_dad_rect.collidepoint(i.pos):
                sc.blit(menu_fone, menu_fone_rect)
                sc.blit(menu_start_button.image, menu_start_button.rect)
                sc.blit(menu_dad_waving, menu_dad_waving_rect)
                pygame.display.update()
                waving = True
            elif waving:
                sc.blit(menu_fone, menu_fone_rect)
                sc.blit(menu_start_button.image, menu_start_button.rect)
                sc.blit(menu_dad, menu_dad_rect)
                pygame.display.update()
                waving = False

            if not(button_pushed) and not(button_clicked) and i.type == pygame.MOUSEMOTION and\
                    menu_start_button.rect.collidepoint(i.pos):
                sc.blit(menu_fone, menu_fone_rect)
                sc.blit(menu_dad, menu_dad_rect)
                sc.blit(menu_start_button.pushed_image, menu_start_button.pushed_rect)
                button_pushed = True
                pygame.display.update()
            elif button_pushed and i.type == pygame.MOUSEBUTTONDOWN:
                sc.blit(menu_fone, menu_fone_rect)
                sc.blit(menu_dad, menu_dad_rect)
                sc.blit(menu_start_button.clicked_image, menu_start_button.clicked_rect)
                button_clicked = True
                button_pushed = False
                pygame.display.update()
            elif button_pushed and i.type == pygame.MOUSEMOTION and\
                    not(menu_start_button.pushed_rect.collidepoint(i.pos)):
                sc.blit(menu_fone, menu_fone_rect)
                sc.blit(menu_dad, menu_dad_rect)
                sc.blit(menu_start_button.image, menu_start_button.rect)
                pygame.display.update()
                button_pushed = False
                
            if button_clicked and i.type == pygame.MOUSEBUTTONUP:
                story()
                dad = get_dad()

                sc.blit(menu_fone, menu_fone_rect)
                sc.blit(menu_start_button.image, menu_start_button.rect)
                sc.blit(menu_dad, menu_dad_rect)

                pygame.display.update()

                # status variables
                waving = False
                button_pushed = False
                button_clicked = False

                
        pygame.time.delay(20)


def story():
    sc.blit(story_fone, story_fone_rect)
    sc.blit(story_start_button.image, story_start_button.rect)
    
    pygame.display.update()

    # status variables
    button_pushed = False
    button_clicked = False
    stop = False

    while not(stop):
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()

            if i.type == pygame.MOUSEMOTION and story_start_button.rect.collidepoint(i.pos) and\
                    not(button_pushed):
                sc.blit(story_fone, story_fone_rect)
                sc.blit(story_start_button.pushed_image, story_start_button.pushed_rect)
                button_pushed = True
                pygame.display.update()
            elif button_pushed and i.type == pygame.MOUSEBUTTONDOWN:
                sc.blit(story_fone, story_fone_rect)
                sc.blit(story_start_button.clicked_image, story_start_button.clicked_rect)
                button_clicked = True
                button_pushed = False
                pygame.display.update()
            elif i.type == pygame.MOUSEMOTION and button_pushed and\
                    not(story_start_button.pushed_rect.collidepoint(i.pos)):
                sc.blit(story_fone, story_fone_rect)
                sc.blit(story_start_button.image, story_start_button.rect)
                button_pushed = False
                pygame.display.update()

            if button_clicked and i.type == pygame.MOUSEBUTTONUP:
                stop = True
         
        pygame.time.delay(20)
    
    level1()


def level1():
    level1_fone_rect = level1_fone.get_rect(topleft=(0, 0))
    sc.blit(level1_fone, level1_fone_rect)
    sc.blit(level_state_lines, level_state_lines_rect)
    arrange_state(dad, sc)

    sc.blit(dad.image, dad.rect)

    pygame.display.update()

    # time
    gone_since_beginning = 0
    gone_since_last = 0
    food_clock = pygame.time.get_ticks()
    
    # state variables
    x, y = H // 2, W // 2
    move = ''
    right = False
    left = False
    change_legs = False
    
    while not(dad.death):
        for i in pygame.event.get():
            if i.type == pygame.QUIT: 
                exit()
            elif i.type == pygame.KEYDOWN:  # moving section
                if i.key in [pygame.K_LEFT, pygame.K_a]:
                    move += 'L'
                    left = True
                elif i.key in [pygame.K_UP, pygame.K_w]:
                    move += 'U'
                elif i.key in [pygame.K_DOWN, pygame.K_s]:
                    move += 'D'
                elif i.key in [pygame.K_RIGHT, pygame.K_d]:
                    move += 'R'
                    right = True
                elif i.key == pygame.K_SPACE:  # hit from dad
                    check_shot(dad, enemies)
                elif i.key == pygame.K_q:  # taking smth from the ground
                    check_take(dad, items_ground, trashcans)
                elif i.key == pygame.K_r:  # changing items in the inventory
                    dad.change_items()
                elif i.key == pygame.K_e:
                    dad.use_item()

            elif i.type == pygame.KEYUP:  # stop move section
                if i.key in [pygame.K_LEFT, pygame.K_a]:
                    move = move[:move.index('L')] + move[move.index('L') + 1:]
                    left = False
                elif i.key in [pygame.K_UP, pygame.K_w]:
                    move = move[:move.index('U')] + move[move.index('U') + 1:]
                elif i.key in [pygame.K_DOWN, pygame.K_s]:
                    move = move[:move.index('D')] + move[move.index('D') + 1:]
                elif i.key in [pygame.K_RIGHT, pygame.K_d]:
                    move = move[:move.index('R')] + move[move.index('R') + 1:]
                    right = False

        if 'R' in move and x != H:  # moving dad's sprite
            dad.rect[0] += dad.speed
        if 'L' in move and dad.rect[0] >= dad.speed:  # border  (dad cant go left)
            dad.rect[0] -= dad.speed
        if 'U' in move and dad.rect[1] >= W * 0.1:  # border (dad cant go upper building)
            dad.rect[1] -= dad.speed
        if 'D' in move and y != W and dad.rect[1] <= W * 0.77:
            dad.rect[1] += dad.speed
        
        if dad.rect[0] >= W * 0.9 and right:  # if dad is close to right and he is moving towards it
            level1_fone_rect[0] -= dad.speed  # we move the fone
            dad.rect[0] -= dad.speed
            if level1_fone_rect[0] <= -6000 + H + dad.speed:  # if fone is ended then we start with the new one
                level1_fone_rect[0] += 3000

            gone_since_beginning += dad.speed  # count the way gone
            gone_since_last += dad.speed  # gone since last 'event'
            if gone_since_last > 200:  # event appears every 100 pixels
                gone_since_last = 0
                event(gone_since_beginning)  # set the event
            
            enemies.update(dad, dad  , True)  # scroll all the sprites
            items.update(items_ground, True)
            items_ground.update(items_ground, True)
            spikes.update(dad.speed)
            trashcans.update(dad.speed)


        if pygame.sprite.spritecollideany(dad, spikes):
            dad.hurt(1)
        
        sc.blit(level1_fone, level1_fone_rect)  # first we blit fone and enemies
        sc.blit(level_state_lines, level_state_lines_rect)
        arrange_state(dad, sc)
        enemies.update((dad.rect[0], dad.rect[1]), dad, False)
        enemies.draw(sc)

        if dad.hurt_right_now:  # decide whether dad is hurt or changing legs..
            sc.blit(dad.image_hurt, dad.rect)
            dad.hurt_right_now = False
        elif move != '' and change_legs:
            sc.blit(dad.image_run,dad.rect)
            change_legs = False
        elif move != '':    
            sc.blit(dad.image, dad.rect)
            change_legs = True
        else:
            sc.blit(dad.image, dad.rect)

        if pygame.time.get_ticks() - food_clock > 10000:  # dad gets hungry evey 10 sec
            dad.hungry()
            food_clock = pygame.time.get_ticks()
        
        items.update(items_ground, False)  # updating items in player hand
        items.draw(sc)
        items_ground.update(items_ground, False)
        items_ground.draw(sc)
        spikes.update(0)
        spikes.draw(sc)
        trashcans.update(0)
        trashcans.draw(sc)
            
        pygame.display.update()
        pygame.time.delay(10)
    
    death_window(gone_since_beginning)


def death_window(gone_since_beginning):
    items.empty() 
    items_ground.empty()
    spikes.empty()
    trashcans.empty()
    enemies.empty()
    
    sc.blit(dark_surf, dark_rect)
    sc.blit(game_over, game_over_rect)

    textsurface = myfont.render('SCORE: ' + str(gone_since_beginning), False, (255, 255, 255))
    sc.blit(textsurface, (H * 0.5, W * 0.7))
    pygame.display.update()

    finish = False

    while not(finish):
        for i in pygame.event.get():
            if i.type == pygame.QUIT: 
                exit()
            elif i.type == pygame.KEYDOWN and i.key == pygame.K_n:
                finish = True

        pygame.time.delay(20)


def event(gone_since_beginning):
    num = randint(1, 100)
    if num < 50:
        set_enemies(gone_since_beginning)
    elif num < 60:
        set_item(gone_since_beginning)
    elif num < 70:
        set_trap(gone_since_beginning)
    elif num <= 75 and gone_since_beginning >= 1000:
        set_road_repair()


def set_item(gone_since_beginning):
    for _ in range(randint(1, 2)):
        trashcans.add(Object_on_ground(trash_can, (H, randint(200, 500)), open_image=trash_can_open))


def set_trap(gone_since_beginning):
    if gone_since_beginning > 200:
        for _ in range(randint(1, 2)):
            spikes.add(Object_on_ground(spikes_im, (H, randint(300, 500))))
    else:
        spikes.add(Object_on_ground(spikes_im, (H, randint(300, 500))))


def set_road_repair():
    pass


def arrange_state(dad, sc):
    '''arrange health, food and inventory'''
    pygame.draw.rect(sc, (255, 50, 50), (30, 10, dad.health * 10, 40))
    pygame.draw.rect(sc, (250, 150, 5), (730, 10, dad.food * 10, 40))
    for i in range(len(dad.pocket)):
        _ = dad.pocket[i].image.get_rect(topleft=(560 + 80 * i, 620))
        sc.blit(dad.pocket[i].image, _)
        for (num, j) in enumerate(dad.pocket[i].get_info()):
            textsurface = myfont_small.render(j, False, (0, 0, 0))
            sc.blit(textsurface, (550 + 80 * i, 580 - num * 20))
    

def check_take(dad, items_ground, trashcans):
    '''check whether dad can reach some items on the ground or a trashcan'''
    for can in trashcans.sprites():
        if abs(can.rect[0] - dad.rect[0]) <= 200 and\
                abs(can.rect[1] - dad.rect[1]) <= 200 and not(can.open):
            can.image = can.open_image
            can.open = True
            if randint(1, 10) <= 8:
                new_item = choice(items_usual).copy()
                new_item.set_xy((can.rect[0], can.rect[1] + 100))
                items_ground.add(new_item)
                return None
            else:
                new_item = choice(items_rare).copy()
                new_item.set_xy((can.rect[0], can.rect[1] + 200))
                items_ground.add(new_item)
                return None

    for item in items_ground.sprites():
        if abs(item.rect[0] - dad.rect[0]) <= 200 and\
                abs(item.rect[1] - dad.rect[1]) <= 200:
            dad.new_item(item.copy(), items_ground)
            items_ground.remove(item)
            break


def check_shot(dad, enemies):
    '''check every enemy whether it is close enough to
    dad and whether he can hit the enemy'''
    for enemy in enemies.sprites():
        if abs(enemy.rect[0] - dad.rect[0]) <= dad.get_distance() and\
            abs(enemy.rect[1] - dad.rect[1]) <= dad.get_distance():
            enemy.hurt(dad.get_power(), items_ground)
            break


def set_enemies(gone_since_beginning):
    '''create new enemies'''
    if gone_since_beginning > 40:
        get_enemy(1)
    elif gone_since_beginning > 200:
        get_enemy(randint(2, 4))
    elif gone_since_beginning > 1000:
        get_enemy(randint(3, 6))


if __name__ == '__main__':
    menu()