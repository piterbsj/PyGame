import pygame
from polscreen import startwindow, game, changelevelwindow, stopwindow, winorloss

screen_dict = {1: startwindow,
               2: game,
               3: changelevelwindow,
               4: stopwindow,
               5: winorloss}

if __name__ == '__main__':
    pygame.init()
    size = w, h = 1000, 600
    screen = pygame.display.set_mode(size)
    screen_id = 1

    while screen_id:
        screen_id = screen_dict[screen_id](screen)