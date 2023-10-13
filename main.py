import entity
import pygame
import time
from random import randint

pygame.get_init()
win = pygame.display.set_mode((1000, 1000), )
image = pygame.image.load("pictures/bg.jpg")
hams = []
start_time = time.time()
player = entity.Enemy("pictures/pers.png", 3, 0, 100, 5, 50, 50, 100, 120)
run = True
while run:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.blit(image, (0, 0))
    current_time = time.time()
    entity.Enemy.moving_enemy(hams, player, win)
    entity.Enemy.moving_player(player, win)
    if current_time - start_time >= 3:
        hams.append(entity.Enemy("pictures/hames.png", 1, 10, 5, 1, randint(0, 1000),
                                 randint(0, 1000), 100, 60))
        start_time = current_time   # Спавнер
    pygame.display.update()

pygame.quit()
