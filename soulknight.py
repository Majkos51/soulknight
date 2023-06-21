import pygame
import random
import math
from orc import Orc

pygame.init()
clock = pygame.time.Clock()
board = [
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
     6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
     6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
     6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 8, 6, 6, 6, 6, 6, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 8, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 9, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 10, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 9, 3, 3, 3, 3, 0, 0, 0, 0, 0,
     3, 3, 3, 3, 3, 3, 10, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 2,
     6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 2,
     6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 2,
     6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 2,
     6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 7, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 8, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 2,
     6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 2,
     6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 2,
     6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6, 6, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 8, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 9, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 10, 6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 9, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
     3, 10, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
     6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
     6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
     6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
     6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
     6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
     6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
     6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
     6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
     6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
]
orcs = [Orc(900, 250)]
for orc in orcs:
    orc.direction = random.choice(["right", "left", "up", "down"])

current_x = -1
current_y = -1
mx, my = 0, 0
movement_count = 0
boss_HP = 16

timer = 60
wait = 30

SQUARE_SIZE = 50
BOARD_SIZE_X = len(board[0])
BOARD_SIZE_Y = len(board)

boss_x, boss_y = 30 * SQUARE_SIZE, 12 * SQUARE_SIZE
timer_boss = 160
boss_dir = 2

cam_x = 0
cam_y = 0
dx = 0
dy = 0
speed = 5
orc_speed = 3.5
True_HP = 8
mana = 160
mana_cost = 4
champ_dmg = 55/3
orc_cx = 0
orc_cy = 0

move_up = True
move_left = True
move_right = True
move_down = True
wave = True
wave_go = False
keys = None
shoot = False
click = None
Orc1 = True
ability = None
on_cooldown = False
ability_cooldown = 300
champ_not_selected = True
boss_show = False
dead = []
wave_num = 1

color_bg = (180, 180, 180)
font = pygame.font.Font('freesansbold.ttf', 18)
font2 = pygame.font.Font('freesansbold.ttf', 35)
champ_pos_x, champ_pos_y = 35 * SQUARE_SIZE // 2 - 35, 17 * SQUARE_SIZE // 2 - 30
knight_dir = 2
attack_rad = 120

screen = pygame.display.set_mode((35 * SQUARE_SIZE, 17 * SQUARE_SIZE))

image = pygame.image.load("data_Soul/dungeon_tilesTILE16x16.png")
img = pygame.transform.scale(image, (19 * 50, 20 * 50)).convert_alpha()
K_night = pygame.image.load("data_Soul/Knight.png")
Knight = pygame.transform.scale(K_night, (60, 60)).convert_alpha()
B_ack_Knight = pygame.image.load("data_Soul/Back_Knight.png")
Back_Knight = pygame.transform.scale(B_ack_Knight, (60, 60)).convert_alpha()
Or_c = pygame.image.load("data_Soul/Orc.png")
Orc_Right = pygame.transform.scale(Or_c, (55, 55)).convert_alpha()
B_ack_O = pygame.image.load("data_Soul/Left_Orc.png")
Orc_Left = pygame.transform.scale(B_ack_O, (55, 55)).convert_alpha()
D_ead = pygame.image.load("data_Soul/DeadOrc.png")
DeadOrc = pygame.transform.scale(D_ead, (50, 50)).convert_alpha()
t_rig = pygame.image.load("data_Soul/trigger.png")
trigger = pygame.transform.scale(t_rig, (30, 30)).convert_alpha()
wiz_ard = pygame.image.load("data_Soul/wizard.png")
wizard_Left = pygame.transform.scale(wiz_ard, (60, 60)).convert_alpha()
wizard_Right = pygame.transform.flip(wizard_Left, True, False)
wizab = pygame.image.load("data_Soul/thunder_wizard.png")
ability = pygame.transform.scale(wizab, (70, 70)).convert_alpha()
champion = Knight
bos_s = pygame.image.load("data_Soul/boss.png")
boss = pygame.transform.scale(bos_s, (200, 200)).convert_alpha()
# print(str(img.width) + ' ' + str(img.height))
wall_s = (1, 4)
floor = (1, 1)

tiles = [
    (1, 1),  # 0 = podlaha
    (1, 0),  # 1 = zed_s
    (4, 1),  # 2 = zed_v
    (1, 4),  # 3 = zed_j
    (0, 1),  # 4 = zed_z
    wall_s,  # 5 = dvere ZATÍM JAKO PODLAHA
    (14, 1),  # 6 = void
    (0, 0),  # 7 = LevýHorníRoh
    (4, 0),  # 8 = PravýHorníRoh
    (0, 4),  # 9 = LevýDolníRoh
    (4, 4)  # 10 = PravýDolníRoh
]


def champ_select():
    global champ_not_selected, champion, attack_rad, mana_cost, champ_dmg, speed
    right_circle = 200
    left_circle = 200
    p, r = (0, 0)
    sel_knight = pygame.transform.scale(Knight, (300, 300))
    sel_wizard = pygame.transform.scale(wiz_ard, (300, 300))
    champ__bg = pygame.image.load("data_Soul/champ_bg.jpg")
    champ_bg = pygame.transform.scale(champ__bg, (2000, 1000))
    pick_your_champ_text = font2.render("Pick your Champion", True, (0, 0, 0))
    while champ_not_selected:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEMOTION:
                p, r = event.pos
                if p > SQUARE_SIZE * 17:
                    right_circle = 250
                    left_circle = 200
                elif p < SQUARE_SIZE * 17:
                    left_circle = 250
                    right_circle = 200
            if event.type == pygame.MOUSEBUTTONUP:
                if p > SQUARE_SIZE * 17:
                    champion = wizard_Right
                    attack_rad += 100
                    mana_cost += 12
                    champ_dmg = 55/2
                    champ_not_selected = False
                elif p < SQUARE_SIZE * 17:
                    champion = Knight
                    speed += 2
                    champ_not_selected = False
        screen.blit(champ_bg, (0, 0))
        pygame.draw.circle(screen, (0, 0, 0), (SQUARE_SIZE * 9 + 160, SQUARE_SIZE * 5 + 150), left_circle)
        pygame.draw.circle(screen, (0, 0, 0), (SQUARE_SIZE * 20 + 160, SQUARE_SIZE * 5 + 150), right_circle)
        screen.blit(sel_knight, (SQUARE_SIZE * 9, SQUARE_SIZE * 5))
        screen.blit(sel_wizard, (SQUARE_SIZE * 20, SQUARE_SIZE * 5))
        screen.blit(pick_your_champ_text, (SQUARE_SIZE * 14 + 10, SQUARE_SIZE * 2))
        pygame.display.flip()


def on_mouse_down(event):
    global current, shoot, click, mana, current_x, current_y, mx, my
    if mana > 0:
        mana -= mana_cost
        shoot = True
    elif mana <= 0:
        shoot = False
    mx, my = event.pos
    current_x = mx - cam_x
    current_y = my - cam_y


def knight_wall():
    global speed, dx, dy, move_up, move_down, move_left, move_right, passed
    for y in range(BOARD_SIZE_Y):
        for x in range(BOARD_SIZE_X):
            if x * SQUARE_SIZE + SQUARE_SIZE - 30 >= champ_pos_x - cam_x >= x * SQUARE_SIZE - 30:
                if y * SQUARE_SIZE + SQUARE_SIZE - 30 >= champ_pos_y - cam_y >= y * SQUARE_SIZE - 30:
                    if (board[y][x] == 1 or ((board[y][x] == 7 or board[y][x] == 8) and knight_dir == 1))\
                            and y * SQUARE_SIZE + SQUARE_SIZE - 35 >= champ_pos_y - cam_y:
                        move_up = False
                    elif (board[y][x] == 3 or ((board[y][x] == 9 or board[y][x] == 10) and knight_dir == 3))\
                        and champ_pos_y - cam_y >= y * SQUARE_SIZE - 25:
                        move_down = False
                    elif (board[y][x] == 4 or ((board[y][x] == 7 or board[y][x] == 9) and knight_dir == 4))\
                            and x * SQUARE_SIZE + SQUARE_SIZE  - 35 >= champ_pos_x - cam_x:
                        move_left = False
                    elif (board[y][x] == 2 or ((board[y][x] == 8 or board[y][x] == 10) and knight_dir == 2))\
                            and x * SQUARE_SIZE - 25 <= champ_pos_x - cam_x:
                        move_right = False

                    else:
                        move_up = True
                        move_left = True
                        move_right = True
                        move_down = True

def game_input():
    global mana, champion, dx, dy, shoot, move_up, move_down, move_left, move_right, knight_dir, on_cooldown, set_alpha, passed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            on_mouse_down(event)

    knight_wall()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        knight_dir = 2
        if move_right:
            if champion == wizard_Right or champion == wizard_Left:
                champion = wizard_Right
            if champion == Knight or champion == Back_Knight:
                champion = Knight
            dx = 0
            dy = 0
            dx = -speed
            move_left = True

        else:
            dx, dy = 0, 0
    elif keys[pygame.K_a]:
        knight_dir = 4
        if move_left:
            if champion == wizard_Right or champion == wizard_Left:
                champion = wizard_Left
            if champion == Knight or champion == Back_Knight:
                champion = Back_Knight
            dx = 0
            dy = 0
            dx = speed
            move_right = True


        else:
            dx, dy = 0, 0
    elif keys[pygame.K_w]:
        knight_dir = 1
        if move_up:
            dx = 0
            dy = 0
            dy = speed
            move_down = True

        else:
            dx, dy = 0, 0
    elif keys[pygame.K_s]:
        knight_dir = 3
        if move_down:
            dx = 0
            dy = 0
            dy = -speed
            move_up = True

        else:
            dx, dy = 0, 0
    elif keys[pygame.K_1]:
        on_cooldown = True
        set_alpha = 100
    else:
        dx, dy = 0, 0


def game_update():
    global shoot, click, cam_y, dy, cam_x, dx, timer, movement_count, mana, wait, timer_boss
    cam_x += dx
    cam_y += dy
    mana += 0.1
    if mana >= 160:
        mana = 160
    global HP
    HP = font.render(str(True_HP) + "/8", True, (0, 0, 0))
    if shoot:
        timer -= 1
    if boss_show:
        timer_boss -= random.randrange(0, 20)
    wait += 1
    print(wave_num)

orc_lives = 55

enemy_direction = "left"


# tile = boardtile
def draw_tile(tile, x, y):
    global cam_x
    global cam_y
    position = x * SQUARE_SIZE + cam_x, y * SQUARE_SIZE + cam_y
    position_x, position_y = x * SQUARE_SIZE + cam_x, y * SQUARE_SIZE + cam_y

    tx, ty = tiles[tile]

    # recatngle = tile_image

    rectangle = (tx * SQUARE_SIZE, ty * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)

    screen.blit(img, position, rectangle)


def open_door():
    global wave_num
    for y in range(BOARD_SIZE_Y):
        for x in range(BOARD_SIZE_X):
            if wave_num == 1:
                if y == 13 and 15 >= x >= 11 and board[y][x] == 3:
                    board[y][x] = 0

            elif wave_num == 2:
                if x == 19 and 26 <= y <= 30 and board[y][x] == 2:
                    board[y][x] = 0

            elif wave_num == 3:
                if y == 23 and 33 <= x <= 37 and board[y][x] == 1:
                    board[y][x] = 0


def close_door(x, y):
    global wave, board, wave_go
    if y == 20 and 11 <= x <= 15 and wave_num == 2 and wave:
        if y * SQUARE_SIZE + SQUARE_SIZE - 38 < champ_pos_y - cam_y and x * SQUARE_SIZE < champ_pos_x - cam_x < x * SQUARE_SIZE + SQUARE_SIZE:
            wave_go = True
            for i in range(BOARD_SIZE_Y):
                for j in range(BOARD_SIZE_X):
                    if i == 20 and 11 <= j <= 15:
                        board[i][j] = 1

    elif x == 27 and 26 <= y <= 30 and wave_num == 3 and wave:
        if y * SQUARE_SIZE < champ_pos_y - cam_y < y * SQUARE_SIZE + SQUARE_SIZE and x * SQUARE_SIZE + SQUARE_SIZE - 43 < champ_pos_x - cam_x:
            wave_go = True
            for i in range(BOARD_SIZE_Y):
                for j in range(BOARD_SIZE_X):
                    if j == 27 and 26 <= i <= 30:
                        board[i][j] = 4

    elif y == 15 and 33 <= x <= 37 and wave_num == 4 and wave:
        if y * SQUARE_SIZE - 22 > champ_pos_y - cam_y and x * SQUARE_SIZE < champ_pos_x - cam_x < x * SQUARE_SIZE + SQUARE_SIZE:
            wave_go = True
            for i in range(BOARD_SIZE_Y):
                for j in range(BOARD_SIZE_X):
                    if i == 15 and 33 <= j <= 37:
                        board[i][j] = 3


def draw_orcs():
    global orcs
    for orc in orcs:
        orc_cx, orc_cy = (cam_x + orc.x, cam_y + orc.y)
        orc.image = Orc_Right
        if orc.alive:
            # orc_cx, orc_cy = (cam_x + orc.x, cam_y + orc.y)
            screen.blit(orc.image, (orc_cx, orc_cy))
            orc.timer += random.randrange(0, 20)
            if orc.timer >= 240:
                orc.direction = random.choice(["left", "right", "up", "down"])
                orc.timer = 0
            if orc.direction == 'left':
                orc.image = Orc_Left
                orc.x -= orc_speed
            elif orc.direction == 'right':
                orc.image = Orc_Right
                orc.x += orc_speed
            elif orc.direction == 'up':
                orc.y -= orc_speed
            elif orc.direction == 'down':
                orc.y += orc_speed
            hit_wall(orc)
        if not orc.alive:
            orc.image = DeadOrc
            screen.blit(orc.image, (orc_cx, orc_cy))


def new_wave():
    global orcs, dead, wave, wave_num, wave_go, boss_show
    if wave_go:
        dead = []
        if wave_num == 2:
            orcs = [Orc(13 * SQUARE_SIZE, 25 * SQUARE_SIZE)]

        if wave_num == 3:
            orcs = [Orc(30 * SQUARE_SIZE, 25 * SQUARE_SIZE)]

        if wave_num == 4:
            boss_show = True


        wave = False
        wave_go = False


def hit_wall(orc):
    for y in range(BOARD_SIZE_Y):
        for x in range(BOARD_SIZE_X):
            if y * SQUARE_SIZE - 30 <= orc.y <= y * SQUARE_SIZE + SQUARE_SIZE - 30 \
                    and x * SQUARE_SIZE - 30 <= orc.x <= x * SQUARE_SIZE + SQUARE_SIZE - 30:
                if orc.direction == 'left' and (board[y][x] == 4 or board[y][x] == 7 or board[y][
                    x] == 9) and x * SQUARE_SIZE + SQUARE_SIZE - 38 >= orc.x:
                    orc.direction = 'right'
                    orc.timer = 0
                elif orc.direction == 'right' and (board[y][x] == 2 or board[y][x] == 8 or board[y][x] == 10) and x * SQUARE_SIZE - 20 <= orc.x:
                    orc.direction = 'left'
                    orc.timer = 0
                elif orc.direction == 'up' and (board[y][x] == 1 or board[y][x] == 7 or board[y][
                    x] == 8) and y * SQUARE_SIZE + SQUARE_SIZE - 38 >= orc.y:
                    orc.direction = 'down'
                    orc.timer = 0
                elif orc.direction == 'down' and (
                        board[y][x] == 3 or board[y][x] == 9 or board[y][x] == 10) and y * SQUARE_SIZE - 23 <= orc.y:
                    orc.direction = 'up'
                    orc.timer = 0


def hit_enemy():
    global shoot, current_x, current_y, Orc1, timer, mana, mx, my, champ_pos_x, champ_pos_y, attack_rad, shot, orcs, door, wave_num, dead, wave, boss_HP, boss_x, boss_y
    in_circle = math.sqrt((champ_pos_x + 30 - mx) ** 2 + (champ_pos_y + 30 - my) ** 2)
    for orc in orcs:
        if orc.alive and in_circle < attack_rad:
            if orc.x <= current_x <= orc.x + 45 and orc.y <= current_y <= orc.y + 45:
                orc.lives -= champ_dmg
                if shoot:
                    screen.blit(trigger, (current_x + cam_x - 15, current_y + cam_y - 15))
                if timer <= 0:
                    shoot = False
                    timer = 15
                current_x = -1 - cam_x
                current_y = -1 - cam_y
                if orc.lives < 5:
                    mana += 10
                    orc.alive = False
                    dead.append(1)
                    if len(dead) >= len(orcs):
                        open_door()
                        wave = True
                        dead = []
                        wave_num += 1
            else:
                screen.blit(trigger, (current_x + cam_x - 15, current_y + cam_y - 15))

    if boss_x <= current_x <= boss_x + 200 and boss_y <= current_y <= boss_y + 200:
        boss_HP -= 1
        if shoot:
            screen.blit(trigger, (current_x + cam_x - 15, current_y + cam_y - 15))
        if timer <= 0:
            shoot = False
            timer = 15
        current_x = -1 - cam_x
        current_y = -1 - cam_y

        if boss_HP <= 0:
            exit()

    else:
        screen.blit(trigger, (current_x + cam_x - 15, current_y + cam_y - 15))


def orcs_damage():
    global orcs, orc_cx, orc_cy, True_HP, wait
    for orc in orcs:
        if wait > 30:
            if orc.x + cam_x - 50 < champ_pos_x < orc.x + cam_x + 50 and orc.y + cam_y - 50 < champ_pos_y < orc.y + cam_y + 50 and orc.alive:
                True_HP -= 1
                wait = 0
            if boss_x + cam_x - 50 < champ_pos_x < boss_x + cam_x + 50 and boss_y + cam_y - 50 < champ_pos_y <boss_y + cam_y + 50:
                True_HP -= 1

        if True_HP <= 0:
            exit()


def boss_movement():
    global timer_boss, boss_x, boss_y, boss_dir
    if boss_dir == 1:
        boss_y -= 3

    if boss_dir == 2:
        boss_x += 3

    if boss_dir == 4:
        boss_x -= 3

    if boss_dir == 3:
        boss_y += 3

    if timer_boss <= 0:
        boss_dir = random.randrange(1, 5)
        timer_boss = 160

    for y in range(BOARD_SIZE_Y):
        for x in range(BOARD_SIZE_X):
            if x * SQUARE_SIZE <= boss_x <= x * SQUARE_SIZE + SQUARE_SIZE\
                and y * SQUARE_SIZE <= boss_y <= y * SQUARE_SIZE + SQUARE_SIZE:
                if (board[y][x] == 1 or board[y][x] == 7 or board[y][x] == 8) and boss_dir == 1:
                    boss_dir = 3
                    timer_boss = 160
                elif (board[y][x] == 2 or board[y][x] == 8 or board[y][x] == 10) and boss_dir == 2:
                    boss_dir = 4
                    timer_boss = 160
                elif (board[y][x] == 3 or board[y][x] == 9 or board[y][x] == 10) and boss_dir == 3:
                    boss_dir = 1
                    timer_boss = 160
                elif (board[y][x] == 4 or board[y][x] == 7 or board[y][x] == 9) and boss_dir == 4:
                    boss_dir = 2
                    timer_boss = 160



def game_output():
    global shoot, orc_lives, timer, enemy_direction, orc_x, orc_y, orc_dir, duration,\
        movement_count, attack_rad, ability, ability_cooldown, on_cooldown, mana, HP, boss_show, boss_x, boss_y, boss_HP
    screen.fill((0, 0, 0))
    for y in range(0, BOARD_SIZE_Y):
        for x in range(0, BOARD_SIZE_X):
            draw_tile(board[y][x], x, y)
            close_door(x, y)
    if on_cooldown:
        pygame.draw.circle(screen, (0, 50, 200), (35 * SQUARE_SIZE // 2 - 5, 17 * SQUARE_SIZE // 2), attack_rad)

    # orcs
    new_wave()
    draw_orcs()

    if boss_show:
        boss_movement()
        screen.blit(boss, (boss_x + cam_x, boss_y + cam_y))
        #healthbar boss
        pygame.draw.rect(screen, (80, 80, 80), (boss_x + cam_x, boss_y + 20 + cam_y, 160, 20), border_radius=5)
        pygame.draw.rect(screen, (150, 0, 0), (boss_x + cam_x, boss_y + 20 + cam_y, boss_HP * 10, 20), border_radius=5)
        # orc_cx, orc_cy = (cam_x + orc.x, cam_y + orc.y)
        # if orc.alive:
        #     screen.blit(orc.image, (orc_cx, orc_cy))
        # else:
        #     screen.blit(orc.image, (orc_cx, orc_cy))

    # healthbar_player
    pygame.draw.rect(screen, (80, 80, 80), (30, 30, 160, 20), border_radius=5)
    if True_HP >= 0:
        pygame.draw.rect(screen, (150, 0, 0), (30, 30, True_HP * 20, 20), border_radius=5)
    pygame.draw.rect(screen, (80, 80, 80), (30, 60, 160, 15), border_radius=5)
    pygame.draw.rect(screen, (0, 150, 150), (30, 60, mana, 15), border_radius=5)
    screen.blit(HP, (100, 31))

    # ABILITY
    if not on_cooldown:
        set_alpha = 255
        ability_cooldown = 300
    if on_cooldown:
        set_alpha = 100
        ability_cooldown -= 1
        if ability_cooldown == 0:
            on_cooldown = False
    ability.set_alpha(set_alpha)
    pygame.draw.rect(screen, (80, 80, 80), (1600, 700, 70, 70))
    screen.blit(ability, (1600, 700))

    screen.blit(champion, (champ_pos_x, champ_pos_y))
    pygame.draw.circle(screen, (30, 30, 30), (35 * SQUARE_SIZE // 2 - 5, 17 * SQUARE_SIZE // 2), attack_rad, 2)

    # trigger
    if shoot:
        if timer <= 0:
            shoot = False
            timer = 15
        hit_enemy()
    #ability
    for orc in orcs:
        in_circle = math.sqrt((champ_pos_x + cam_x - orc.x) ** 2 + (champ_pos_y + cam_y - orc.y) ** 2)
        if orc.alive and in_circle < attack_rad:
            if on_cooldown:
                orc.lives -= 5 / 30
                mana -= 0.5 / 30
                if orc.lives < 1:
                    orc.alive = False
        #orc deal damage
        if orc.alive:
            orcs_damage()

        # healthbar enemy
        orc_cx, orc_cy = (cam_x + orc.x, cam_y + orc.y)
        if orc.alive:
            pygame.draw.rect(screen, (80, 80, 80), (orc_cx, orc_cy - 16, 55, 8), border_radius=5)
            pygame.draw.rect(screen, (150, 0, 0), (orc_cx, orc_cy - 16, orc.lives, 8), border_radius=5)



while True:
    if champ_not_selected:
        champ_select()
    game_input()
    game_update()
    game_output()
    pygame.display.flip()
    clock.tick(30)



#TODO: Bos shooting missiles/ occasionally rockets or some stronger more damaging stuff, change of speed