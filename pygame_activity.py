<<<<<<< Updated upstream
<<<<<<< Updated upstream
import pygame

pygame.init()

screen = pygame.display.set_mode((400,500))

done = False

while not done:
      
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

=======
=======
>>>>>>> Stashed changes
import pygame

pygame.init()

screen = pygame.display.set_mode((400,500))

done = False

while not done:
      
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
      pygame.display.flip()      