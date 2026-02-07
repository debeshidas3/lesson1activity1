import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 500))
clock=pygame.time.Clock()
pygame.display.set_caption("Debeshi's Game")
running = True

dt=0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)



while running:
      for event in pygame.event.get():
            print("This is event", event)
            if event.type == pygame.QUIT:
                  print("Enter this loop, event type is quit")
                  running = False
      screen.fill("purple")
      pygame.draw.circle(screen, "yellow", player_pos, 30)
      keys = pygame.key.get_pressed()
      if keys[pygame.K_UP]:
          player_pos.y -= 1000 * dt
      if keys[pygame.K_DOWN]:
          player_pos.y += 1000 * dt
      if keys[pygame.K_LEFT]:
          player_pos.x -= 1000 * dt
      if keys[pygame.K_RIGHT]:
          player_pos.x += 1000 * dt

      pygame.display.flip()

      dt = clock.tick(60) / 1000
pygame.quit()
                  
# pygame.QUIT
# size of the screen
# slice(300,300)
# background color of the screen
# GREY = (58,58,58)

# running = True

# running = False
# while not None:
      
#       for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False


# screen.fill(grey)
# pygame.display.flip()               

# pygame.quit()