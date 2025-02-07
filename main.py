import pygame

import polscreen
from polscreen import start_window, game, win_or_loss, change_level_window, Animation

screen_dict = {1: start_window,
               2: game,
               3: change_level_window,
               4: win_or_loss}

if __name__ == '__main__':
    pygame.init()
    size = w, h = 1000, 600
    screen = pygame.display.set_mode(size)
    screen_id = 1

    while screen_id:
        screen_id = screen_dict[screen_id](screen)