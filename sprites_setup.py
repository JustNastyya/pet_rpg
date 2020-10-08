import pygame
from classes_setup import *
import sys
import os


def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


pygame.init()
H, W = 950, 700

# _________menu sprites___________
menu_fone = pygame.image.load(
    resource_path(r'sprites\menu_fone.png')
)
menu_fone_rect = menu_fone.get_rect(center=(H // 2, W // 2))  # coor
menu_dad = pygame.image.load(resource_path(r'sprites\menu_dad.png'))
menu_dad_rect = menu_dad.get_rect(topleft=(int(H * 0.15), int(W * 0.6)))  # coor
menu_dad_waving = pygame.image.load(resource_path(r'sprites\menu_dad_waving.png'))
menu_dad_waving_rect = menu_dad_waving.get_rect(topleft=(int(H * 0.15), int(W * 0.6)))  # coor

menu_start_button = Button(resource_path(r'sprites\menu_start_button.png'),
                        resource_path(r'sprites\menu_start_button_pushed.png'),
                        resource_path(r'sprites\menu_start_button_clicked.png'), 
                        (int(H * 0.45), int(W * 0.6)))  # coor

# __________pre-story____________
story_fone = pygame.image.load(resource_path(r'sprites\story_fone.png'))  # add text 
story_fone_rect = story_fone.get_rect(center=(H // 2, W // 2))

story_start_button = Button(resource_path(r'sprites\story_start_button.png'),
                        resource_path(r'sprites\story_start_button_pushed.png'),
                        resource_path(r'sprites\story_start_button_clicked.png'),
                        (int(H * 0.13), int(W * 0.98)))  # coor

# __________level 1________________

level1_fone = pygame.image.load(resource_path(r'sprites\level1_fone.png'))
level1_fone_rect = level1_fone.get_rect(topleft=(0, 0))  # coor

level_state_lines = pygame.image.load(resource_path(r'sprites\state_lines.png'))
level_state_lines_rect = level_state_lines.get_rect(topleft=(0, 0))


# groups

enemies = pygame.sprite.Group()
items = pygame.sprite.Group()
items_ground = pygame.sprite.Group()
spikes = pygame.sprite.Group()
trashcans = pygame.sprite.Group()

# items 
items_usual = [
    Object(resource_path(r'sprites\f_applepart.png'), food=2),
    Object(resource_path(r'sprites\h_book.png'), healing=5),
    Object(resource_path(r'sprites\f_apple.png'), food=5),
    Object(resource_path(r'sprites\trash.png')),
    Object(resource_path(r'sprites\f_cola.png'), food=3),
    Weapon(resource_path(r'sprites\w_pocketknife.png'), power=3),
    Weapon(resource_path(r'sprites\w_bottle.png'), power=5),
    Weapon(resource_path(r'sprites\w_pencil.png'), power=1),
    Weapon(resource_path(r'sprites\w_fryingpan.png'), power=6),
    Weapon(resource_path(r'sprites\w_brassknuckles.png'), power=4),
    Weapon(resource_path(r'sprites\w_cup.png'), power=3)
]

items_rare = [
    Object(resource_path(r'sprites\f_dumplings.png'), food=10),
    Object(resource_path(r'sprites\f_schnizel.png'), food=7),
    Weapon(resource_path(r'sprites\w_hammer.png'), power=10, distance=250),
    Weapon(resource_path(r'sprites\w_bat.png'), power=8),
    Weapon(resource_path(r'sprites\w_russianflag.png'), power=9)
]

items_super_rare = [
    Object(resource_path(r'sprites\fh_bigmac.png'), healing=20, food=20),
    Weapon(resource_path(r'sprites\w_superhammer.png'), power=15, distance=350)
]


# people
def get_dad():
    return MainHero(
            resource_path(r'sprites\dad.png'), resource_path(r'sprites\dad_hurt.png'),
            resource_path(r'sprites\dad_run.png'), (int(H * 0.2), W // 2),
            15, items, pocket=[items_usual[1].copy()])


road_repair = pygame.image.load(resource_path(r'sprites\road_repair.png'))
road_repair_sign = pygame.image.load(resource_path(r'sprites\road_repair_sign.png'))
road_workers = [pygame.image.load(resource_path(r'sprites\road_worker_') + str(i) + '.png') for i in range(1, 5)]
road_workers_hurt = [pygame.image.load(resource_path(r'sprites\road_worker_') + str(i) + '_hurt.png') for i in range(1, 5)]
road_worker_talking = pygame.image.load(resource_path(r'sprites\road_worker_talking.png')) 


def get_enemy(n):
    for _ in range(n):
        i = randint(1, 4)
        number = randint(0, 8)
        if number < 3:
            enemies_pocket = [choice(items_usual).copy()]
        elif number == 6:
            enemies_pocket = [choice(items_rare).copy()]
        else:
            enemies_pocket = []

        if i < 3:
            Enemy(resource_path(r'sprites\homeless_') + str(i) + '.png',
                resource_path(r'sprites\homeless_') + str(i) + '_hurt.png',
                20, enemies, items, speed=5, pocket=enemies_pocket)
        else:    
            Enemy(resource_path(r'sprites\beggar_') + str(i - 2) + '.png',
                resource_path(r'sprites\beggar_') + str(i - 2) + '_hurt.png',
                randint(10, 30), enemies, items, pocket=enemies_pocket
            )
    if randint(1, 30) == 1:
        Enemy(resource_path(r'sprites\homeless_super.png'),
            resource_path(r'sprites\homeless_super_hurt.png'),
            100, enemies, items, speed=4, pocket=[choice(items_super_rare).copy()])  # change pocket


spikes_im = pygame.image.load(resource_path(r'sprites\spikes.png'))

trash_can = pygame.image.load(resource_path(r'sprites\trashcan.png'))
trash_can_open = pygame.image.load(resource_path(r'sprites\trashcan_open.png'))

# gameover section
game_over = pygame.image.load(resource_path(r'sprites\game_over.png'))
game_over_rect = game_over.get_rect(center=(H // 2, W // 2))

myfont = pygame.font.SysFont('Comic Sans MS', 30)
myfont_small = pygame.font.SysFont('Comic Sans MS', 20)

dark_surf = pygame.Surface((H, W))
dark_surf.fill((0, 0, 0))
dark_surf.set_alpha(150)

dark_rect = dark_surf.get_rect(topleft=(0, 0))

