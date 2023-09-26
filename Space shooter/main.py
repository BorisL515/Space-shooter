import pygame
import os

pygame.init()

screen = pygame.display.set_mode((800,600))
Title = pygame.display.set_caption(("Quantum Nova"))

icon_path = os.path.join("Models", "Icon.png")
icon = pygame.image.load(icon_path)
pygame.display.set_icon(icon)

Background_path = os.path.join("Models", "Background.png")
Background = pygame.image.load(Background_path)

running = True

    

while running:
    screen.blit(Background, (0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
    pygame.display.update()
