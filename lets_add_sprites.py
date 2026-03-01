import pygame
pygame.init
# Screen setup
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Two Rectangles")

running = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True

    screen.fill((0, 0, 0))  # Fill background with black

    # Draw first rectangle (red)
    pygame.draw.rect(screen, (255, 0, 0), (100, 100, 150, 100))

    # Draw second rectangle (green)
    pygame.draw.rect(screen, (0, 255, 0), (300, 200, 120, 80))

    pygame.display.flip()  # Update the display

pygame.quit()
import pygame
pygame.init
# Screen setup
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Two Rectangles")

running = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True

    screen.fill((0, 0, 0))  # Fill background with black

    # Draw first rectangle (red)
    pygame.draw.rect(screen, (255, 0, 0), (100, 100, 150, 100))

    # Draw second rectangle (green)
    pygame.draw.rect(screen, (0, 255, 0), (300, 200, 120, 80))

    pygame.display.flip()  # Update the display

pygame.quit()