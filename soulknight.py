import pygame
pygame.init()
clock = pygame.time.Clock
board = [
[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
[6, 6, 6, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 8, 6, 6, 6],
[6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6],
[6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6],
[6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6],
[6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6],
[6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6],
[6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6],
[6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6],
[6, 6, 6, 9, 3, 3, 3, 3, 0, 5, 5, 5, 5, 0, 3, 3, 3, 3,10, 6, 6, 6],
[6, 6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6, 6, 6],
[6, 6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6, 6, 6],
[6, 6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6, 6, 6],
[6, 6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6, 6, 6],
[6, 6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6, 6, 6],
[6, 6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6, 6, 6],
[6, 6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6, 6, 6],
[6, 6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6, 6, 6],
[6, 6, 6, 7, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 8, 6, 6, 6],
[6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6],
[6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6],
[6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6],
[6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6],
[6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6],
[6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6],
[6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6],
[6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6],
[6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6],
[6, 6, 6, 9, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,10, 6, 6, 6],
[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
]

current = (-1, -1)
current_x = -1
current_y = -1
timer = 60


SQUARE_SIZE = 50
BOARD_SIZE_X = len(board[0])
BOARD_SIZE_Y = len(board)

cam_x = 0
cam_y = 0
dx = 0
dy = 0
speed = 5
True_HP = 8
mana = 160
keys = None
shoot = False
click = None
color_bg = (180, 180, 180)
font = pygame.font.Font('freesansbold.ttf', 18)

image = pygame.image.load("data_Soul/dungeon_tilesTILE16x16.png")
img = pygame.transform.scale(image, (19 * 50, 20 * 50))
K_night = pygame.image.load("data_Soul/Knight.png")
Knight = pygame.transform.scale(K_night, (60, 60))
B_ack_Knight = pygame.image.load("data_Soul/Back_Knight.png")
Back_Knight = pygame.transform.scale(B_ack_Knight, (60, 60))
Or_c = pygame.image.load("data_Soul/Orc.png")
Orc = pygame.transform.scale(Or_c, (55, 55))
t_rig = pygame.image.load("data_Soul/trigger.png")
trigger = pygame.transform.scale(t_rig, (30, 30))

knight_dir = Knight
# print(str(img.width) + ' ' + str(img.height))
tiles = [
    (1, 1),  # 0 = podlaha
    (1, 0),  # 1 = zed_s
    (4, 1),  # 2 = zed_v
    (1, 4),  # 3 = zed_j
    (0, 1),  # 4 = zed_z
    (1, 1),  # 5 = dvere ZATÍM JAKO PODLAHA
    (14, 1), # 6 = void
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
    mana -= 4
    shoot = True
    mx, my = event.pos
    mx -= cam_x
    my -= cam_y
    global current_x
    global current_y
    current_x = mx
    current_y = my
    current = mx, my
    if event.type == pygame.MOUSEBUTTONDOWN:
        click = pygame.time.get_ticks()



def game_update():
    global shoot, click, cam_y, dy, cam_x, dx, timer
    cam_x += dx
    cam_y += dy
    global HP
    HP = font.render(str(True_HP) + "/8", True, (0, 0, 0))

    if shoot:
        timer -= 1
        if timer <= 0:
            shoot = False
            timer = 60

def game_output():
    global shoot
    screen.fill((0, 0, 0))
    for y in range(0, BOARD_SIZE_Y):
        for x in range(0, BOARD_SIZE_X):
            draw_tile(board[y][x], x, y)
    screen.blit(Orc, (cam_x + 800, cam_y + 350))
    pygame.draw.rect(screen, (80, 80, 80), (30, 30, 160, 20), border_radius=5)
    pygame.draw.rect(screen, (150, 0, 0), (30, 30, 160, 20), border_radius=5)
    pygame.draw.rect(screen, (80, 80, 80), (30, 60, 160, 15), border_radius=5)
    pygame.draw.rect(screen, (0, 150, 150), (30, 60, mana, 15), border_radius=5)
    screen.blit(HP, (100, 31))
    screen.blit(knight_dir, (35 * SQUARE_SIZE // 2 - 35, 17 * SQUARE_SIZE // 2 - 30))
    if shoot:
        screen.blit(trigger, (current_x + cam_x, current_y + cam_y))
    pygame.display.flip()

def draw_tile(tile, x, y):
    global cam_x
    global cam_y
    position = (x * SQUARE_SIZE + cam_x, y * SQUARE_SIZE + cam_y)

    tx, ty = tiles[tile]
    rectangle = (tx * SQUARE_SIZE, ty * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)

    screen.blit(img, position, rectangle)


while True:
    game_input()
    game_update()
    game_output()
