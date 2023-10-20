import entity
import pygame
import time
from random import randint


def anmation():
    for i in range(500):
        win.blit(image, (0, 0))
        win.blit(player.model, [player.x, player.y])
        win.blit(main_title.picture, (main_title.x, main_title.y - i))
        win.blit(start_button.picture, (start_button.x, start_button.y + i))
        win.blit(exit_button.picture, (exit_button.x + i, 0))
        pygame.display.update()
        pygame.time.delay(1)


pygame.get_init()
win = pygame.display.set_mode((1000, 1000), )
pygame.display.set_caption('FOXYSHMERTS.INC')

image = pygame.image.load("pictures/bg.jpg")
player = entity.Enemy("pictures/pers.png", 3, 0, 100, 5, 440, 350, 70, 120)

main_title = entity.Menu('pictures/title.png', 210, 200, 600, 80)
start_button = entity.Menu('pictures/start_button.png', 340, 500, 300, 100)
exit_button = entity.Menu('pictures/exit_button.png', 900, 0, 100, 100)

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
        win.blit(main_title.picture, (main_title.x, main_title.y))
        win.blit(start_button.picture, (start_button.x, start_button.y))
        win.blit(exit_button.picture, (exit_button.x, exit_button.y))
        pygame.display.update()
        if event.type == pygame.QUIT:
            menu = False
        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.x <= x <= start_button.x + start_button.height and start_button.y <= y <= start_button.y + start_button.wigth:  # Кнопка старта
                menu = False
                run = True
                anmation()
            if exit_button.x <= x <= exit_button.x + exit_button.height and exit_button.y <= y <= exit_button.y + exit_button.wigth:  # Кнопка выхода
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
    entity.Enemy.touch_kill(hams, player, bullets)
    if len(hams) != 0:
        entity.Enemy.shooting(bullets, hams[0], win)
    if current_time - start_time >= 2:
        for i in range(2):
            hams.append(entity.Enemy("pictures/hames.png", 1, 10, 5, 1, randint(0, 1000),
                                 randint(0, 1000), 100, 60))
        start_time = current_time
        bullets.append(entity.Enemy('pictures/bullet.png', 5, 0, 0, 10, player.x, player.y, 10, 10))
    pygame.display.update()

pygame.quit()
