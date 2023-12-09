import pygame
import time
from random import randint
import math
import threading
import sys
class Menu:
    def __init__(self, picture, x, y, height, width,):
        self.width = width
        self.height = height
        self.y = y
        self.x = x
        self.picture = pygame.transform.scale(pygame.image.load(picture), (height, width))

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

class upgrade_card:
    def __init__(self, name, tier, picture, type, damage, cd, speed, hp, prot):
        self.name = name
        self.tier = tier
        self.picture = pygame.transform.scale(pygame.image.load(picture), (300, 600))
        self.type = type
        self.damage = damage
        self.cd = cd
        self.speed = speed
        self.hp = hp
        self.prot = prot
def hard():
    global hard_k
    while working:
        while get_harder:
            hard_k += 0.5
            pygame.time.delay(30000)
def shoot():
    while working:
        while is_shooting:
            bullets.append(Enemy('pictures/bullet.png', 10, 1, 0, 4, player.x + player.height / 2, player.y + player.width / 2, 20, 20))
            pygame.time.delay(bullets[-0].spawn_rate * 1000)
def spawn():
    while working:
        while is_spawning:
            hams.append(Enemy("pictures/hames.png", 1 * hard_k, 1 * hard_k, 5 * hard_k, 5 * hard_k, randint(0, 1000), randint(0, 1000), 100, 60))
            pygame.time.delay(1000)

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

def xp():
    global current_xp, xp_need, choice, Pause, is_spawning, is_shooting
    pygame.draw.rect(win, (37, 245, 165), (0,0, 1000 * current_xp / xp_need, 20))
    if xp_need <= current_xp:
        current_xp = 0
        xp_need *= 2
        choice = True
        Pause = True
        is_shooting = False
        is_spawning = False
        up()

def shooting():
    for i in range(len(bullets)):
        if len(hams) > 0:
            dx = hams[0].x - bullets[i].x + hams[0].height / 2
            dy = hams[0].y - bullets[i].y + hams[0].width / 2
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
    for count in range(50):
        win.blit(image, (0, 0))
        win.blit(player.model, [player.x, player.y])
        win.blit(main_title.picture, (main_title.x, main_title.y - count * 10))
        win.blit(start_button.picture, (start_button.x, start_button.y + count * 10))
        win.blit(exit_button.picture, (exit_button.x + count * 10, 0))
        pygame.display.update()
        pygame.time.delay(1)

def touch_kill():
    global current_xp
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
            current_xp += 20
    for u in kill_list2:
        if u < len(bullets):
            bullets.pop(u)

def up():
    global working, menu, Game, x, y, choice, Pause, is_spawning, is_shooting
    while choice:
        win.blit(upgrades[0].picture, (40, 200))
        win.blit(upgrades[1].picture, (350, 200))
        win.blit(upgrades[2].picture, (660, 200))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
                menu = False
                Game = False
                choice = False
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 40 <= x < 340 and 200 <= x <= 800:
                    Pause = False
                    choice = False
                    is_spawning = True
                    is_shooting = True
        pygame.time.delay(30)

shot = threading.Thread(target=shoot)
sp = threading.Thread(target=spawn)
hd = threading.Thread(target=hard)

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

upgrades = [upgrade_card("Большой калибр", 1, "pictures/up_cards/big_cal.png", 'up_p', 5, 2, 0, 0, 0),
            upgrade_card("Миник", 1, "pictures/up_cards/minic.png", 'up_p', 0, 0, 0, 25, 0),
            upgrade_card("Бронепластина", 1, "pictures/up_cards/armorplate.png", 'up_p', 0, 0, 0, 0, 5)]


#upgrades  = [upgrade_card("Большой калибр", 1, "Большие пушки - большой калибр. Увеличивает урон, увеличивает перезардку", 'up_p', 5, -2, 0, 0, 0),
         #    upgrade_card("Миник", 1, "Выпей миник, немного повысь лимит здоровья", 'up_p', 0, 0, 0, 25, 0),
         #    upgrade_card("Адская плеть", 1,"Раскрутите адскую плеть, наносящую средний урон", 'new_w', 0, 0, 0, 0, 0),
          #   upgrade_card("Усовершенствованный затвор", 1, "Установите улучшеный затвор, увеличив тем самым скорострельнсть, немного уменьшая урон", 'up_p', -2, 2, 0, 0, 0),
          #   upgrade_card("Бронепластина", 1, "Установите дополнительную бронепластину, уменьшающую входящий урон", 'up_p', 0, 0, 0, 0, 5),
          #   upgrade_card("Липкое масло", 1, "Залейте пол липким маслом, замедляющим врагов", 'Weakness', 0, 0, -3, 0, 0),
          #   upgrade_card("Паровые тяги", 2, "Уфффф что за тяги такие, паровые, кэфтэме. Увеличивают вашу скорость", 'up_p', 0, 0, 5, 0, 0),
          #   upgrade_card("Бига", 2, "Бахни бигу, получи ощутимый прирост к здоровью", 'up_p', 0, 0, 0, 75, 0),
          #   upgrade_card("Квантовый щит", 2, "С помощью новейших технологий ощутимо увеличте свою броню", 'up_p', 0, 0, 0 , 0, 12),
          #   upgrade_card("Заряженное копьё", 2, "Бросьте медленное копьё, наносящее высокий урон", 'new_w', 0, 0, 0, 0, 0),
          #   upgrade_card("Калибр бабахи", 2, "Самые огромные фугасы, но и перезарядка тоже огромная. Мощная прибавка к урону и перезарядке", 'up_p', 20, -8, 0, 0, 0),
           #  upgrade_card("Пушка от A10 Thunderbolt", 2, "Тот самый БРРРРРРРРРРРРРРРРРР!!!! Стоп, а где урон?! Огромный прирост к скорострельности, но про урон забудьте", 'up_p', -40, 20, 0, 0, 0),
          #   upgrade_card("Услуги дезинсектора", 2, "Протравите своих врагов, уменьшив их наносимый урон")]

hams = [Enemy("pictures/hames.png", 1, 10, 5, 5, randint(0, 1000), randint(0, 1000),  100, 60)]
bullets = []
start_time = time.time()
hard_k = 0.5
x = 0
y = 0
current_xp = 0
xp_need = 100
f1 = pygame.font.Font(None, 36)

is_spawning = False
get_harder = False
working = True
is_shooting = False
run = False
death = False
menu = True
Game = True
Pause = False
choice = False
shot.start()
sp.start()
hd.start()

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
                working = False
                menu = False
                Game = False
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.x <= x <= start_button.x + start_button.height and start_button.y <= y <= start_button.y + start_button.width:  # Кнопка старта
                    menu = False
                    run = True
                    anmation()
                if exit_button.x <= x <= exit_button.x + exit_button.height and exit_button.y <= y <= exit_button.y + exit_button.width:  # Кнопка выхода
                    menu = False
                    Game = False
                    working = False

    while run:
        is_shooting = True
        is_spawning = True
        get_harder = True
        pygame.time.delay(20)
        text = f1.render('HP: ', 1, (255, 0, 0))
        text1 = f1.render(str(player.hp), 1, (255, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
                run = False
                Game = False
        if player.hp <= 0:
            is_shooting = False
            is_spawning = False
            get_harder = False
            run = False
            menu = True
            hams.clear()
            bullets.clear()
            xp_need = 100
            current_xp = 0
            player.hp = 100
            player.x = 440
            player.y = 350
            hard_k = 1
        win.blit(image, (0, 0))
        if not Pause:
            moving_enemy()
            moving_player()
            touch_kill()
            xp()
        win.blit(text, (0, 0))
        win.blit(text1, (40, 0))
        shooting()
        pygame.display.update()


pygame.quit()
sys.exit()
