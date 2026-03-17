import pygame
import random

pygame.init()

# Screen
screen = pygame.display.set_mode((800, 600))

# Enemy setup
enemy_img = pygame.Surface((40, 40))  # simple square enemy
enemy_img.fill((255, 0, 0))

enemyX = []
enemyY = []

# Create 7 enemies
for i in range(7):
    enemyX.append(random.randint(0, 760))
    enemyY.append(random.randint(50, 150))

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw all enemies
    for i in range(7):
        screen.blit(enemy_img, (enemyX[i], enemyY[i]))

    pygame.display.update()

pygame.quit()