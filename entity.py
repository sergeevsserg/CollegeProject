import pygame
class Enemy:
    def __init__(self, model, speed, spawn_rate, hp, damage, x, y):
        self.model = model
        self.speed = speed
        self.spawn_rate = spawn_rate
        self.hp = hp
        self.damage = damage
        self.x = x
        self.y = y