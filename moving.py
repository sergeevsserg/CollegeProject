import pygame


def moving_enemy(x, y, xx, yy, speed):
    if x > xx:
        x -= speed
    if x < xx:
        x += speed
    if y > yy:
        y -= speed
    if y < yy:
        y += speed
    return x, y


def moving_player(x, y, speed):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x < 880:
        x += speed
    if keys[pygame.K_UP] and y > 0:
        y -= speed
    if keys[pygame.K_DOWN] and y < 900:
        y += speed
    return x, y
