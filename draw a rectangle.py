import pygame

pygame.init()

screen = pygame.display.set_mode((400, 300))

clock = pygame.time.Clock()

done = False

while not done:

    for event in pygame.event.get():

       if event.type == pygame.QUIT:

          done = True

     screen.fill((0, 0, 0))

     pygame.draw.rect(screen, (0, 125, 255), pygame.Rect(30, 30, 60, 60))

      pygame.display.flip() # MUST be inside loop

      clock.tick(60)

pygame.quit()