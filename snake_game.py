import sys

import pygame
from random import randint

pygame.init()
sw = 640
sh = 480
wind = pygame.display.set_mode((sw,sh))


bg_color = pygame.color.Color(22, 41, 81)


tiles_x = 32
tile_y = 24

tile_w = sw//tiles_x
tile_h = sh//tile_y

#serpent
snk_x,snk_y = tiles_x//4,tile_y//2
snake = [
    [snk_x,snk_y],
    [snk_x-1,snk_y],
    [snk_x-2,snk_y]
]

#bouffe
food = [tiles_x//2, tile_y//2]

def drawfood():
    food_color = pygame.color.Color(210,45,60)
    food_rec = pygame.Rect((food[0]*tile_w, food[1]*tile_h), (tile_w,tile_h))
    pygame.draw.rect(wind,food_color,food_rec)

def drawsnake():
    snk_color = pygame.color.Color(60, 215, 60)
    for cell in snake:
        cell_rec = pygame.Rect((cell[0] * tile_w, cell[1] * tile_h), (tile_w, tile_h))
        pygame.draw.rect(wind, snk_color, cell_rec)

score = 0
def texte():
    pygame.init()
    police = pygame.font.SysFont("arial", 30)
    image_texte = police.render("Votre score est de "+str(score), 1, ("Green"))
    wind.blit(image_texte, (200, 40))

    police = pygame.font.SysFont("arial", 20)
    image_texte = police.render("Appuyer sur Enter pour commencer ", 1, ("Green"))
    wind.blit(image_texte, (190, 300))
    pygame.display.flip()

a = True
def updatesnake(direction):
    global food,score,a
    if a == True:
        dir_x, dir_y = direction
        head = snake[0].copy()
        head[0] = (head[0]+dir_x)%tiles_x
        head[1] = (head[1]+dir_y)%tile_y

        if head in  snake:
            return False
        elif head == food:
            food = None
            while food is None:
                newfood = [
                    randint(0,tiles_x-1),
                    randint(0,tile_y-1)
                ]
                food = newfood if newfood not in snake else None
                score += 1
        else:
            snake.pop()

        snake.insert(0, head)
        return True


#gamel loop
running = False
direction = [1,0]
x = 300
y = 100


def drawbutton():
    btn_color = pygame.color.Color("darkblue")
    cell_rec = pygame.Rect((8 * tile_w, 9 * tile_h), (x, y))
    pygame.draw.rect(wind, btn_color, cell_rec)
    police = pygame.font.SysFont("century", 40)
    image_texte = police.render("Commencer", 1, ("green"))
    wind.blit(image_texte, (190, 200))
    pygame.display.update()


game = True
while game:
    while not running:
        pygame.time.Clock().tick(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_RETURN:
                    running = True


                    print(running)
        wind.fill(bg_color)
        drawbutton()
        texte()
        pygame.display.update()

    while running:
        pygame.time.Clock().tick(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_RIGHT and not direction == [-1, 0]:  # 100=d to right
                    direction = [1, 0]
                if event.key == pygame.K_LEFT and not direction == [1, 0]:  # 100=d to right
                    direction = [-1, 0]
                if event.key == pygame.K_UP and not direction == [0, 1]:  # 100=d to right
                    direction = [0, -1]
                if event.key == pygame.K_DOWN and not direction == [0, -1]:  # 100=d to right
                    direction = [0, 1]

        # update
        if updatesnake(direction) == False:
            running = False
        # dessin
        wind.fill(bg_color)
        drawfood()
        drawsnake()
        pygame.display.update()

pygame.quit()