import pygame
import os

pygame.init()
running = True

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Quantum Nova")

# The path to images.
icon_path = os.path.join("Models", "Icon.png")
player_path = os.path.join("Models", "Player.png")
background_path = os.path.join("Models", "Background.png")
enemy_path = os.path.join("Models", "Enemy.png")

# The icon for the app
icon = pygame.image.load(icon_path).convert()
pygame.display.set_icon(icon)

player_img_x = 370
player_img_y = 480
change_x = 0

# This stores the images into the data
background = pygame.image.load(background_path).convert()
player_img = pygame.image.load(player_path)
enemy_img = pygame.image.load(enemy_path)
# This displays the images on the X and Y coordinates I want them to be.
def player():
    screen.blit(player_img, (player_img_x, player_img_y))

while running:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        change_x = 1
    elif keys[pygame.K_a]:
        change_x = -1
    else:
        change_x = 0

    player_img_x += change_x

    if player_img_x<= -3:
        player_img_x = -3
    elif player_img_x>= 705:
        player_img_x = 705

    screen.blit(enemy_img, (400,500))
    
    player()
    pygame.display.flip()


pygame.quit()
