import pygame


class Enemy:
    def __init__(self, model, speed, spawn_rate, hp, damage, x, y, height, width):
        self.model = pygame.transform.scale(pygame.image.load(model), [height, width])
        self.revers_model = pygame.transform.flip(pygame.transform.scale(pygame.image.load(model), [height, width] ), 180, 0)
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
            if enemy[i].x > player.x + player.height/4:
                enemy[i].x -= enemy[i].speed
            if enemy[i].x < player.x + player.height/4:
                enemy[i].x += enemy[i].speed
                rot = True
            if enemy[i].y > player.y + player.width/4:
                enemy[i].y -= enemy[i].speed
            if enemy[i].y < player.y + player.width/4:
                enemy[i].y += enemy[i].speed
            if rot:
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
