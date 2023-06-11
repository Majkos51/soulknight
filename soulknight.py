import pygame
import random
import math
from orc import Orc

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
mx, my = 0, 0
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
champ_not_selected = True
color_bg = (180, 180, 180)
font = pygame.font.Font('freesansbold.ttf', 18)
font2 = pygame.font.Font('freesansbold.ttf', 35)
champ_pos_x, champ_pos_y = 35 * SQUARE_SIZE // 2 - 35, 17 * SQUARE_SIZE // 2 - 30
attack_rad = 120

image = pygame.image.load("data_Soul/dungeon_tilesTILE16x16.png")
img = pygame.transform.scale(image, (19 * 50, 20 * 50))
K_night = pygame.image.load("data_Soul/Knight.png")
Knight = pygame.transform.scale(K_night, (60, 60))
B_ack_Knight = pygame.image.load("data_Soul/Back_Knight.png")
Back_Knight = pygame.transform.scale(B_ack_Knight, (60, 60))
Or_c = pygame.image.load("data_Soul/Orc.png")
Orc_Right = pygame.transform.scale(Or_c, (55, 55))
B_ack_O = pygame.image.load("data_Soul/Left_Orc.png")
Orc_Left = pygame.transform.scale(B_ack_O, (55, 55))
D_ead = pygame.image.load("data_Soul/DeadOrc.png")
DeadOrc = pygame.transform.scale(D_ead, (50, 50))
t_rig = pygame.image.load("data_Soul/trigger.png")
trigger = pygame.transform.scale(t_rig, (30, 30))
wiz_ard = pygame.image.load("data_Soul/wizard.png")
wizard_Left = pygame.transform.scale(wiz_ard, (60, 60))
wizard_Right = pygame.transform.flip(wizard_Left, True, False)
champion = Knight
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


def champ_select():
    global champ_not_selected, champion
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
                    champ_not_selected = False
                elif p < SQUARE_SIZE * 17:
                    champion = Knight
                    champ_not_selected = False
        screen.blit(champ_bg, (0, 0))
        pygame.draw.circle(screen, (0, 0, 0), (SQUARE_SIZE * 9 + 160, SQUARE_SIZE * 5 + 150), left_circle)
        pygame.draw.circle(screen, (0, 0, 0), (SQUARE_SIZE * 20 + 160, SQUARE_SIZE * 5 + 150), right_circle)
        screen.blit(sel_knight, (SQUARE_SIZE * 9, SQUARE_SIZE * 5))
        screen.blit(sel_wizard, (SQUARE_SIZE * 20, SQUARE_SIZE * 5))
        screen.blit(pick_your_champ_text, (SQUARE_SIZE * 14 + 10, SQUARE_SIZE * 2))
        pygame.display.flip()

def game_input():
    global mana, champion, dx, dy, shoot
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            on_mouse_down(event)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        if champion == wizard_Right or champion == wizard_Left:
            champion = wizard_Right
        if champion == Knight or champion == Back_Knight:
            champion = Knight
        dx = 0
        dy = 0
        dx = -speed
    elif keys[pygame.K_a]:
        if champion == wizard_Right or champion == wizard_Left:
            champion = wizard_Left
        if champion == Knight or champion == Back_Knight:
            champion = Back_Knight
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
    global current, shoot, click, mana, current_x, current_y, mx, my
    if mana > 0:
        mana -= 4
        shoot = True
    elif mana <= 0:
        shoot = False
    mx, my = event.pos
    current_x = mx - cam_x
    current_y = my - cam_y


def game_update():
    global shoot, click, cam_y, dy, cam_x, dx, timer, movement_count, mana
    cam_x += dx
    cam_y += dy
    mana += 0.1
    if mana >= 160:
        mana = 160
    global HP
    HP = font.render(str(True_HP) + "/8", True, (0, 0, 0))
    if shoot:
        timer -= 1

orc_lives = 55

enemy_direction = "left"


def game_output():
    global shoot, orc_lives, timer, enemy_direction, orc_x, orc_y, orc_dir, duration, movement_count, attack_rad
    screen.fill((0, 0, 0))
    for y in range(0, BOARD_SIZE_Y):
        for x in range(0, BOARD_SIZE_X):
            draw_tile(board[y][x], x, y)
    #orcs
    for orc in orcs:
        orc_cx, orc_cy = (cam_x + orc.x, cam_y + orc.y)
        orc.image = Orc_Right
        if orc.alive:
            # orc_cx, orc_cy = (cam_x + orc.x, cam_y + orc.y)
            screen.blit(orc.image, (orc_cx, orc_cy))
            orc.timer += random.randrange(0, 20)
            if orc.timer >= 120:
                orc.direction = random.choice(["left", "right", "up", "down"])
                orc.timer = 0
            if orc.direction == 'left':
                orc.image = Orc_Left
                orc.x -= random_movement_speed
            elif orc.direction == 'right':
                orc.image = Orc_Right
                orc.x += random_movement_speed
            elif orc.direction == 'up':
                orc.y -= random_movement_speed
            elif orc.direction == 'down':
                orc.y += random_movement_speed
            hit_wall(orc)
        if not orc.alive:
            orc.image = DeadOrc
            screen.blit(orc.image, (orc_cx, orc_cy))
        # orc_cx, orc_cy = (cam_x + orc.x, cam_y + orc.y)
        # if orc.alive:
        #     screen.blit(orc.image, (orc_cx, orc_cy))
        # else:
        #     screen.blit(orc.image, (orc_cx, orc_cy))



    # healthbar_player
    pygame.draw.rect(screen, (80, 80, 80), (30, 30, 160, 20), border_radius=5)
    pygame.draw.rect(screen, (150, 0, 0), (30, 30, 160, 20), border_radius=5)
    pygame.draw.rect(screen, (80, 80, 80), (30, 60, 160, 15), border_radius=5)
    pygame.draw.rect(screen, (0, 150, 150), (30, 60, mana, 15), border_radius=5)
    screen.blit(HP, (100, 31))

    
    screen.blit(champion, (champ_pos_x, champ_pos_y))
    pygame.draw.circle(screen, (30, 30, 30), (35 * SQUARE_SIZE // 2 - 5, 17 * SQUARE_SIZE // 2), attack_rad, 2)

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
        if orc.alive:
            pygame.draw.rect(screen, (80, 80, 80), (orc_cx, orc_cy - 16, 55, 8), border_radius=5)
            pygame.draw.rect(screen, (150, 0, 0), (orc_cx, orc_cy - 16, orc.lives, 8), border_radius=5)


#tile = boardtile
def draw_tile(tile, x, y):
    global cam_x
    global cam_y
    position = x * SQUARE_SIZE + cam_x, y * SQUARE_SIZE + cam_y
    position_x, position_y = x * SQUARE_SIZE + cam_x, y * SQUARE_SIZE + cam_y

    tx, ty = tiles[tile]
    #recatngle = tile_image

    rectangle = (tx * SQUARE_SIZE, ty * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)

    screen.blit(img, position, rectangle)


def hit_enemy():
    global shoot, current_x, current_y, Orc1, timer, mana, mx, my, champ_pos_x, champ_pos_y, attack_rad
    in_circle = math.sqrt((champ_pos_x - mx) ** 2 + (champ_pos_y - my) ** 2)
    for orc in orcs:
        if orc.alive and in_circle < attack_rad:
            if orc.x <= current_x <= orc.x + 55 and orc.y <= current_y <= orc.y + 55:
                orc.lives -= 55 / 3
                current_x = -1 - cam_x
                current_y = -1 - cam_y
                if orc.lives < 5:
                    mana += 10
                    orc.alive = False


def hit_wall(orc):
    for y in range(BOARD_SIZE_Y):
        for x in range(BOARD_SIZE_X):
            if y * SQUARE_SIZE - 35 <= orc.y <= y * SQUARE_SIZE + SQUARE_SIZE - 25\
                and x * SQUARE_SIZE - 35 <= orc.x <= x * SQUARE_SIZE + SQUARE_SIZE - 25:
                if orc.direction == 'left' and (board[y][x] == 4 or board[y][x] == 7 or board[y][x] == 9) and x * SQUARE_SIZE + SQUARE_SIZE - 35 >= orc.x:
                    orc.direction = 'right'
                    orc.timer = 0
                elif orc.direction == 'right' and (board[y][x] == 2 or board[y][x] == 8 or board[y][x] == 10) and x * SQUARE_SIZE - 25 <= orc.x:
                    orc.direction = 'left'
                    orc.timer = 0
                elif orc.direction == 'up' and (board[y][x] == 1 or board[y][x] == 7 or board[y][x] == 8) and y * SQUARE_SIZE + SQUARE_SIZE - 35 >= orc.y:
                    orc.direction = 'down'
                    orc.timer = 0
                elif orc.direction == 'down' and (board[y][x] == 3 or board[y][x] == 9 or board[y][x] == 10) and y * SQUARE_SIZE - 25 <= orc.y:
                    orc.direction = 'up'
                    orc.timer = 0



while True:
    if champ_not_selected:
        champ_select()
    game_input()
    game_update()
    game_output()
    pygame.display.flip()

