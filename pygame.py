import pygame, sys

pygame.init()
pencere = pygame.display.set_mode((300,300))

beyaz = (255,255,255)

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    pygame.draw.rect(pencere, beyaz, (50,50,100,150), 1)

    pygame.display.flip()
