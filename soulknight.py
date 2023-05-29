import pygame
from PIL import Image
pygame.init()

board = [
[6, 6, 6, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[6, 6, 6, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
]

SQUARE_SIZE = 30
BOARD_SIZE_X = len(board[0])
BOARD_SIZE_Y = len(board)

cam_x = 0
cam_y = 0
dx = 0
dy = 0
speed = 2
keys = None
color_bg = (180, 180, 180)

image = pygame.image.load("soul_data/dungeon_tilesTILE16x16.png")
filepath = "soul_data/dungeon_tilesTILE16x16.png"
img = Image.open(filepath)
image = pygame.transform.scale(image, (img.width * (SQUARE_SIZE/16), img.height * (SQUARE_SIZE/16)))

#print(str(img.width) + ' ' + str(img.height))
tiles = [
    (1, 1), #0 = podlaha
    (1, 0), #1 = zed_s
    (4, 1), #2 = zed_v
    (1, 4), #3 = zed_j
    (0, 1), #4 = zed_z
    (1, 1), #5 = dvere ZATÍM JAKO PODLAHA
    (14, 1)#6 = void
]

screen = pygame.display.set_mode((50 * SQUARE_SIZE, 25 * SQUARE_SIZE))


def game_input():
    global dx, dy
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        dx = -speed
    elif keys[pygame.K_a]:
        dx = speed
    elif keys[pygame.K_w]:
        dy = speed
    elif keys[pygame.K_s]:
        dy = -speed
    else:
        dx, dy = (0, 0)


def game_update():
    global cam_x, dx
    global cam_y, dy
    cam_x += dx
    cam_y += dy 


def game_output():
    screen.fill((0, 0, 0))
    for y in range(0, BOARD_SIZE_Y):
        for x in range(0, BOARD_SIZE_X):
            draw_tile(board[y][x], x, y)
    pygame.display.flip()

def draw_tile(tile, x, y):
    global cam_x
    global cam_y
    position = (x * SQUARE_SIZE + cam_x, y * SQUARE_SIZE + cam_y)
    
    tx, ty = tiles[tile]
    rectangle = (tx * SQUARE_SIZE, ty * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)

    screen.blit(image,  position, rectangle)


while True:
    game_input()
    game_update()
    game_output()



