# main.py

import pygame
pygame.init()

WIDTH = 800
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))

inUse = True
while inUse:
    pygame.time.delay(50)
    print("running")

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                inUse = False


pygame.quit()
