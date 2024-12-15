import pygame
from pygame import*
from datetime import datetime

from models.zone import Background, Time, Money, Points
from models.persons.mainpers import Pony

if __name__ == '__main__':
    pygame.init()
    size = w, h = 1000, 600
    screen = pygame.display.set_mode(size)

    background_zone = Background()
    time_zone = Time()
    money_zone = Money()
    points_zone = Points()
    pony = Pony()

    running = True
    begin = datetime.now()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            now = datetime.now()
            ch = now - begin
            print(str(ch))


        screen.fill((216, 191, 216))

        background_zone.draw(screen)
        time_zone.draw(screen)
        money_zone.draw(screen)
        points_zone.draw(screen)
        pony.draw(screen)

        pygame.display.flip()
print('для коммита')