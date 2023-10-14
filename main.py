import entity
import pygame
import time
from random import randint


def anmation():
    for i in range(500):
        win.blit(image, (0, 0))
        win.blit(player.model, [player.x, player.y])
        win.blit(main_title, (210, 200 - i ^ 2))
        win.blit(start_button, (340, 500 + i ^ 2))
        win.blit(exit_button, (900 + i, 0))
        pygame.display.update()
        pygame.time.delay(2)


pygame.get_init()
win = pygame.display.set_mode((1000, 1000), )
pygame.display.set_caption('FOXYSHMERTS.INC')

image = pygame.image.load("pictures/bg.jpg")
player = entity.Enemy("pictures/pers.png", 3, 0, 100, 5, 440, 350, 100, 120)
main_title = pygame.transform.scale(pygame.image.load('pictures/title.png'), (600, 80))
start_button = pygame.transform.scale(pygame.image.load('pictures/start_button.png'), (300, 100))
exit_button = pygame.transform.scale(pygame.image.load('pictures/exit_button.png'), (100, 100))

hams = []
bullets = []
start_time = time.time()
x = 0
y = 0

run = False
menu = True
while menu:
    for event in pygame.event.get():
        win.blit(image, (0, 0))
        win.blit(player.model, [player.x, player.y])
        win.blit(main_title, (210, 200))
        win.blit(start_button, (340, 500))
        win.blit(exit_button, (900, 0))
        pygame.display.update()
        if event.type == pygame.QUIT:
            menu = False
        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 340 <= x <= 640 and 500 <= y <= 600:  # Кнопка старта
                menu = False
                run = True
                anmation()
            if 900 <= x <= 1000 and 0 <= y <= 100:  # Кнопка выхода
                menu = False
while run:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.blit(image, (0, 0))
    current_time = time.time()
    entity.Enemy.moving_enemy(hams, player, win)
    entity.Enemy.moving_player(player, win)
    entity.Enemy.touch_kill(hams, player)
    if len(hams) != 0:
        entity.Enemy.shooting(bullets, hams[0], win)
    if current_time - start_time >= 2:
        hams.append(entity.Enemy("pictures/hames.png", 1, 10, 5, 1, randint(0, 1000),
                                 randint(0, 1000), 100, 60))
        bullets.append(entity.Enemy('pictures/bullet.png', 1, 0, 0, 10, player.x, player.y, 10, 10))
        start_time = current_time   # Спавнер
    pygame.display.update()

pygame.quit()
