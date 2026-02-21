import pygame
pygame.init()

s = pygame.display.set_mode((640,480))
p = pygame.Rect(300,220,40,40)
c = pygame.time.Clock()

running = True
while running:
    dt = clock.tick(60)/1000
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: p.y -= 300*dt
    if keys[pygame.K_s]: p.y += 300*dt
    if keys[pygame.K_a]: p.x -= 300*dt
    if keys[pygame.K_d]: p.x += 300*dt

    s.fill("pink")
    pygame.draw.rect(s, "purple", p)
    pygame.display.flip()

pygame.quit()