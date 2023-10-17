import pygame
import math

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

    @staticmethod
    def moving_enemy(enemy, player, win):
        for i in range(len(enemy)):
            rot = False
            dx = player.x - enemy[i].x
            dy = player.y - enemy[i].y
            distanse = math.sqrt(dx*dx + dy*dy)
            enemy[i].x += enemy[i].speed * dx / distanse
            enemy[i].y += enemy[i].speed * dy / distanse
            if dx > 0:
                win.blit(enemy[i].revers_model, [enemy[i].x, enemy[i].y])
            else:
                win.blit(enemy[i].model, [enemy[i].x, enemy[i].y])

    def moving_player(self, win):
        rot = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.x > 0:
            self.x -= self.speed
            rot = True
        if keys[pygame.K_d] and self.x < 880:
            self.x += self.speed
        if keys[pygame.K_w] and self.y > 0:
            self.y -= self.speed
        if keys[pygame.K_s] and self.y < 900:
            self.y += self.speed
        if rot:
            win.blit(self.revers_model, [self.x, self.y])
        else:
            win.blit(self.model, [self.x, self.y])

    def touch_kill(self, player, bullet):
        kill_list = []
        kill_list2 = []
        for i in range(len(self)):
            if player.x - player.height/2 <= self[i].x <= player.x + player.height/2 and player.y - player.width/2.5 <= self[i].y <= player.y + player.width/1.2:
                kill_list.append(i)
            for j in range(len(bullet)):
                if bullet[j].x - bullet[j].height <= self[i].x <= bullet[j].x + bullet[j].height and bullet[j].y - bullet[j].width <= self[i].y <= bullet[j].y + bullet[j].width:
                    kill_list.append(i)
                    kill_list2.append(j)
        for b in kill_list:
            self.pop(b)
        for u in kill_list2:
            bullet.pop(u)


    def shooting(self, enemy, win):
        for i in range(len(self)):
            dx = enemy.x - self[i].x
            dy = enemy.y - self[i].y
            distanse = math.sqrt(dx * dx + dy * dy)
            self[i].x += self[i].speed * dx / distanse
            self[i].y += self[i].speed * dy / distanse
            win.blit(self[i].model, [self[i].x, self[i].y])


class Menu:
    def __init__(self, picture, x, y, height, wigth,):
        self.wigth = wigth
        self.height = height
        self.y = y
        self.x = x
        self.picture = pygame.transform.scale(pygame.image.load(picture), (height, wigth))
