import pygame
from pygame import*
from datetime import datetime

from models.zone import Background, Time, Money, Points
from models.persons.mainpers import Pony
from models.methods import load_image


if __name__ == '__main__':
    pygame.init()
    size = w, h = 1000, 600
    screen = pygame.display.set_mode(size)

    background_zone = Background('background1.jpg',(0,0))
    ground = Background('ground.png',(0,0))
    time_zone = Time()
    money_zone = Money()
    points_zone = Points()
    pony = Pony('ponyy.png', (0,0))
    move = Background('background1.jpg', (0,0))

    running = True
    isJumping = False
    clock = pygame.time.Clock()
    timer = clock.tick()
    stopBack = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not isJumping:
                    pony.jump()
                if event.key == pygame.K_d:
                    stopBack = not stopBack

        timer += clock.tick()

        pony.update()

        screen.fill((0, 191, 216))

        background_zone.draw_bc(screen)
        if stopBack:
            background_zone.move(screen)
        ground.draw_gr(screen)
        time_zone.draw(screen)
        money_zone.draw(screen)
        points_zone.draw(screen)
        pony.draw(screen)
        time_zone.text(screen)

        pygame.display.flip()
        clock.tick(30)

