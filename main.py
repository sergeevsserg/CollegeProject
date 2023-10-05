import entity
import pygame
import moving

pygame.get_init()
win = pygame.display.set_mode((1000, 1000), )
image = pygame.image.load("pictures/bg.jpg")
hames = entity.Enemy(pygame.transform.scale(pygame.image.load("pictures/pngwing.com.png"), [40, 40]), 3,
                     10, 5, 1, 800, 800)
player = entity.Enemy(pygame.transform.scale(pygame.image.load("pictures/pers.png"), [120, 100]), 5,
                      0, 100, 5, 50, 50)
width = 120
height = 100
run = True
while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    player.x, player.y = moving.moving_player(player.x, player.y, player.speed)
    hames.x, hames.y = moving.moving_enemy(hames.x, hames.y, player.x, player.y, hames.speed)
    win.blit(image, (0, 0))
    win.blit(hames.model, [hames.x, hames.y])
    win.blit(player.model, [player.x, player.y])
    pygame.display.update()

pygame.quit()
