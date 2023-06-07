import pygame
import random
from Orc import Orc

pygame.init()
clock = pygame.time.Clock
board = [
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 8, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 9, 3, 3, 3, 3, 0, 5, 5, 5, 5, 0, 3, 3, 3, 3, 10, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 7, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 8, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 9, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 10, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
]

orcs = [Orc(800, 350), Orc(600, 200), Orc(400, 250)]

current_x = -1
current_y = -1
movement_count = 0

timer = 60

SQUARE_SIZE = 50
BOARD_SIZE_X = len(board[0])
BOARD_SIZE_Y = len(board)

cam_x = 0
cam_y = 0
dx = 0
dy = 0
speed = 5
random_movement_speed = 3
True_HP = 8
mana = 160
orc_x, orc_y = 800, 350
keys = None
shoot = False
click = None
Orc1 = True
color_bg = (180, 180, 180)
font = pygame.font.Font('freesansbold.ttf', 18)
duration = random.randrange(0, 15)

image = pygame.image.load("data_Soul/dungeon_tilesTILE16x16.png")
img = pygame.transform.scale(image, (19 * 50, 20 * 50))
K_night = pygame.image.load("data_Soul/Knight.png")
Knight = pygame.transform.scale(K_night, (60, 60))
B_ack_Knight = pygame.image.load("data_Soul/Back_Knight.png")
Back_Knight = pygame.transform.scale(B_ack_Knight, (60, 60))
Or_c = pygame.image.load("data_Soul/Orc.png")
Orc_Left = pygame.transform.scale(Or_c, (55, 55))
B_ack_O = pygame.image.load("data_Soul/Back_Orc .png")
Back_orc = pygame.transform.scale(B_ack_O, (55, 55))
D_ead = pygame.image.load("data_Soul/DeadOrc.png")
DeadOrc = pygame.transform.scale(D_ead, (50, 50))
t_rig = pygame.image.load("data_Soul/trigger.png")
trigger = pygame.transform.scale(t_rig, (30, 30))

knight_dir = Knight
orc_dir = Back_orc
# print(str(img.width) + ' ' + str(img.height))
tiles = [
    (1, 1),  # 0 = podlaha
    (1, 0),  # 1 = zed_s
    (4, 1),  # 2 = zed_v
    (1, 4),  # 3 = zed_j
    (0, 1),  # 4 = zed_z
    (1, 1),  # 5 = dvere ZATÍM JAKO PODLAHA
    (14, 1),  # 6 = void
    (0, 0),  # 7 = LevýHorníRoh
    (4, 0),  # 8 = PravýHorníRoh
    (0, 4),  # 9 = LevýDolníRoh
    (4, 4),  # 10 = PravýDolníRoh
]

screen = pygame.display.set_mode((35 * SQUARE_SIZE, 17 * SQUARE_SIZE))


def game_input():
    global mana, knight_dir, dx, dy, shoot
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            on_mouse_down(event)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        knight_dir = Knight
        dx = 0
        dy = 0
        dx = -speed
    elif keys[pygame.K_a]:
        knight_dir = Back_Knight
        dx = 0
        dy = 0
        dx = speed
    elif keys[pygame.K_w]:
        dx = 0
        dy = 0
        dy = speed
    elif keys[pygame.K_s]:
        dx = 0
        dy = 0
        dy = -speed
    else:
        dx, dy = (0, 0)


def on_mouse_down(event):
    global current, shoot, click, mana
    if mana > 0:
        mana -= 4
        shoot = True
    elif mana <= 0:
        shoot = False
    mx, my = event.pos
    mx -= cam_x
    my -= cam_y
    global current_x
    global current_y
    current_x = mx
    current_y = my
    current = mx, my


def game_update():
    global shoot, click, cam_y, dy, cam_x, dx, timer, movement_count
    cam_x += dx
    cam_y += dy
    global HP
    HP = font.render(str(True_HP) + "/8", True, (0, 0, 0))
    if shoot:
        timer -= 1


orc_lives = 55

enemy_direction = "left"


def game_output():
    global shoot, orc_lives, timer, enemy_direction, orc_x, orc_y, orc_dir, duration, movement_count
    screen.fill((0, 0, 0))
    for y in range(0, BOARD_SIZE_Y):
        for x in range(0, BOARD_SIZE_X):
            draw_tile(board[y][x], x, y)
    for orc in orcs:
        if orc.alive:
            orc.timer += random.randrange(0, 20)
            if orc.timer >= 120:
                orc.direction = random.choice(["left", "right", "up", "down"])
                orc.timer = 0
            if orc.direction == 'left':
                orc.image = Back_orc
                orc.x -= random_movement_speed
            elif orc.direction == 'right':
                orc.image = Orc_Left
                orc.x += random_movement_speed
            elif orc.direction == 'up':
                orc.y -= random_movement_speed
            elif orc.direction == 'down':
                orc.y += random_movement_speed
        orc_cx, orc_cy = (cam_x + orc.x, cam_y + orc.y)
        if orc.alive:
            screen.blit(orc.image, (orc_cx, orc_cy))
        else:
            screen.blit(orc.image, (orc_cx, orc_cy))



    # healthbar_player
    pygame.draw.rect(screen, (80, 80, 80), (30, 30, 160, 20), border_radius=5)
    pygame.draw.rect(screen, (150, 0, 0), (30, 30, 160, 20), border_radius=5)
    pygame.draw.rect(screen, (80, 80, 80), (30, 60, 160, 15), border_radius=5)
    pygame.draw.rect(screen, (0, 150, 150), (30, 60, mana, 15), border_radius=5)
    screen.blit(HP, (100, 31))

    screen.blit(knight_dir, (35 * SQUARE_SIZE // 2 - 35, 17 * SQUARE_SIZE // 2 - 30))
    pygame.draw.circle(screen, (30, 30, 30), (35 * SQUARE_SIZE // 2 - 5, 17 * SQUARE_SIZE // 2), 120, 2)

    # trigger
    if shoot:
        screen.blit(trigger, (current_x + cam_x - 15, current_y + cam_y - 15))
        if timer <= 0:
            shoot = False
            timer = 30
        hit_enemy()
    # healthbar enemy
    for orc in orcs:
        orc_cx, orc_cy = (cam_x + orc.x, cam_y + orc.y)
        pygame.draw.rect(screen, (80, 80, 80), (orc_cx, orc_cy - 16, 55, 8), border_radius=5)
        pygame.draw.rect(screen, (150, 0, 0), (orc_cx, orc_cy - 16, orc.lives, 8), border_radius=5)


def draw_tile(tile, x, y):
    global cam_x
    global cam_y
    position = (x * SQUARE_SIZE + cam_x, y * SQUARE_SIZE + cam_y)

    tx, ty = tiles[tile]
    rectangle = (tx * SQUARE_SIZE, ty * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)

    screen.blit(img, position, rectangle)


def hit_enemy():
    for orc in orcs:
        global shoot, current_x, current_y, Orc1, timer, mana
        if orc.x <= current_x <= orc.x + 55 and orc.y <= current_y <= orc.y + 55:
            orc.lives -= 55 / 3
            current_x = -1 - cam_x
            current_y = -1 - cam_y
        if orc.alive:
            if orc.lives <= 1:
                mana += 10
                Orc.alive = False


while True:
    game_input()
    game_update()
    game_output()
    pygame.display.flip()
