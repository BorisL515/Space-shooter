import pygame
import os
import random

# Initialize Pygame
pygame.init()

# Create the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Quantum Nova")

# Load images
icon = pygame.image.load(os.path.join("Models", "Icon.png")).convert()
pygame.display.set_icon(icon)

background = pygame.image.load(os.path.join("Models", "Background.png")).convert()
player_img = pygame.image.load(os.path.join("Models", "Player.png"))
enemy_img = pygame.image.load(os.path.join("Models", "Enemy.png"))

# Game variables
player_x = 370
player_y = 480
player_speed_x = 0.8

enemy_x = random.randint(40, 736)
enemy_y = random.randint(30, 150)
enemy_speed_x = 0.3
enemy_speed_y = 30

running = True

# Define functions
def draw_player():
    screen.blit(player_img, (player_x, player_y))

def draw_enemy():
    screen.blit(enemy_img, (enemy_x, enemy_y))

# Main game loop
while running:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        player_x += player_speed_x
    elif keys[pygame.K_a]:
        player_x -= player_speed_x

    # Ensure player_x stays within defined ranges
    player_x = max(0, min(player_x, 705))
    
    # Adjust enemy movement based on their proximity to specific coordinates
    if enemy_x <= 3:
        enemy_speed_x = 0.3
        enemy_y += enemy_speed_y
    if enemy_x >= 710:
        enemy_speed_x = -0.3
        enemy_y += enemy_speed_y

    # Update enemy position
    enemy_x += enemy_speed_x

    # Render player and enemy
    draw_player()
    draw_enemy()
    pygame.display.flip()

# Quit Pygame
pygame.quit()
