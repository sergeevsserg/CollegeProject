import pygame
import time
from random import randint
import math
import threading

class Menu:
    def __init__(self, picture, x, y, height, wigth,):
        self.wigth = wigth
        self.height = height
        self.y = y
        self.x = x
        self.picture = pygame.transform.scale(pygame.image.load(picture), (height, wigth))

class Enemy:
    def __init__(self, model, speed, spawn_rate, hp, damage, x, y, height, width):
        self.model = pygame.transform.scale(pygame.image.load(model), [height, width])
        self.revers_model = pygame.transform.flip(pygame.transform.scale(pygame.image.load(model), [height, width]), 1, 0)
        self.speed = speed
        self.spawn_rate = spawn_rate
        self.hp = hp
        self.damage = damage
        self.x = x
        self.y = y
        self.height = height
        self.width = width


def moving_player():
    rot = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player.x > 0:
        player.x -= player.speed
        rot = True
    if keys[pygame.K_d] and player.x < 880:
        player.x += player.speed
    if keys[pygame.K_w] and player.y > 0:
        player.y -= player.speed
    if keys[pygame.K_s] and player.y < 900:
        player.y += player.speed
    if rot:
        win.blit(player.revers_model, [player.x, player.y])
    else:
        win.blit(player.model, [player.x, player.y])

def shooting():
    for i in range(len(bullets)):
        dx = hams[i].x - bullets[i].x + hams[i].height / 2
        dy = hams[i].y - bullets[i].y + hams[i].width / 2
        distanse = math.sqrt(dx * dx + dy * dy)
        bullets[i].x += bullets[i].speed * dx / distanse
        bullets[i].y += bullets[i].speed * dy / distanse
        win.blit(bullets[i].model, [bullets[i].x, bullets[i].y])
def moving_enemy():
    for i in range(len(hams)):
        dx = player.x - hams[i].x
        dy = player.y - hams[i].y
        distanse = math.sqrt(dx*dx + dy*dy)
        hams[i].x += hams[i].speed * dx / distanse
        hams[i].y += hams[i].speed * dy / distanse
        if dx > 0:
            win.blit(hams[i].revers_model, [hams[i].x, hams[i].y])
        else:
            win.blit(hams[i].model, [hams[i].x, hams[i].y])

def anmation():
    for count in range(500):
        win.blit(image, (0, 0))
        win.blit(player.model, [player.x, player.y])
        win.blit(main_title.picture, (main_title.x, main_title.y - count))
        win.blit(start_button.picture, (start_button.x, start_button.y + count))
        win.blit(exit_button.picture, (exit_button.x + count, 0))
        pygame.display.update()
        pygame.time.delay(1)

def touch_kill():
    kill_list = []
    kill_list2 = []
    for i in range(len(hams)):
        if player.x - player.height/2 <= hams[i].x <= player.x + player.height/2 and player.y - player.width/2.5 <= hams[i].y <= player.y + player.width/1.2:
            player.hp -= hams[i].damage
            kill_list.append(i)
        for j in range(len(bullets)):
            if bullets[j].x - bullets[j].height <= hams[i].x + hams[i].height / 2 <= bullets[j].x + bullets[j].height and bullets[j].y - bullets[j].width <= hams[i].y + hams[i].width / 2 <= bullets[j].y + bullets[j].width:
                hams[i].hp -= bullets[j].damage
                kill_list2.append(j)
        if hams[i].hp <= 0:
            kill_list.append(i)
    for b in kill_list:
        if b < len(hams):
            hams.pop(b)
    for u in kill_list2:
        if u < len(bullets):
            bullets.pop(u)


pygame.get_init()
pygame.font.init()
win = pygame.display.set_mode((1000, 1000), )
pygame.display.set_caption('FOXYSHMERTS.INC')

image = pygame.image.load("pictures/bg.jpg")
player = Enemy("pictures/pers.png", 3, 0, 100, 5, 440, 350, 70, 120)
main_title = Menu('pictures/title.png', 210, 200, 600, 80)
start_button = Menu('pictures/start_button.png', 340, 500, 300, 100)
exit_button = Menu('pictures/exit_button.png', 900, 0, 100, 100)
lose_title1 = Menu('pictures/lose_text1.png', 210, 200, 600, 80)
lose_title2 = Menu('pictures/lose_text_2.png', 400, 400, 600, 80)

hams = []
bullets = []
start_time = time.time()
x = 0
y = 0
f1 = pygame.font.Font(None, 36)

run = False
death = False
menu = True
Game = True

while Game:
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
                Game = False
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.x <= x <= start_button.x + start_button.height and start_button.y <= y <= start_button.y + start_button.wigth:  # Кнопка старта
                    menu = False
                    run = True
                    anmation()
                if exit_button.x <= x <= exit_button.x + exit_button.height and exit_button.y <= y <= exit_button.y + exit_button.wigth:  # Кнопка выхода
                    menu = False
                    Game = False

    while run:
        pygame.time.delay(20)
        text = f1.render('HP: ', 1, (255, 0, 0))
        text1 = f1.render(str(player.hp), 1, (255, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                Game = False
        if player.hp <= 0:
            run = False
            menu = True
            hams.clear()
            bullets.clear()
            player.hp = 100
            player.x = 440
            player.y = 350
        win.blit(image, (0, 0))  # вывод экрана
        current_time = time.time()   # начало отсчёта времени  (очень не удобная вещь, надо найти замену)
        moving_enemy()  # вызов движения врагов
        moving_player()  # вызов движения персонажа
        touch_kill()  # обработка касаний
        win.blit(text, (0, 0))
        win.blit(text1, (40, 0))  # вывод хп
        if len(hams) != 0:
            shooting()  # вызов движения пули
        if current_time - start_time >= 2:  # ужасный костыль, полностью переписать
            for i in range(2):  # спавн врагов
                hams.append(Enemy("pictures/hames.png", 1, 10, 5, 5, randint(0, 1000), randint(0, 1000),  100, 60))
            start_time = current_time
            bullets.append(Enemy('pictures/bullet.png', 10, 0, 0, 4, player.x + player.height / 2, player.y + player.width / 2, 20, 20))  # выстрел
        pygame.display.update()

pygame.quit()
