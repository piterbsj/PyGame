import pygame
from pygame import*


if __name__ == '__main__':
    pygame.init()
    size = w, h = 1000, 600
    screen = pygame.display.set_mode(size)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((216, 191, 216))
        pygame.display.flip()