import sys

import pygame
from pygame.constants import QUIT, K_ESCAPE, KEYDOWN

from models.methods import load_image


def my_animation(w1, h1, k, fps, name, position):
    animation_frames = []
    timer = pygame.time.Clock()
    image = load_image("Firework.png")

    sprite = pygame.image.load("Firework.png".format(name)).convert_alpha()

    width, height = sprite.get_size()
    w, h = width / w1, height / h1

    row = 0

    for j in range(int(height / h)):
        for i in range(int(width / w)):
            animation_frames.append(image.subsurface(pygame.Rect(i * w, row, w, h)))
        row += int(h)

    counter = 0

    while True:
        for evt in pygame.event.get():
            if evt.type == QUIT or (evt.type == KEYDOWN and evt.key == K_ESCAPE):
                sys.exit()

        scr.blit(animation_frames[counter], position) #отрисовка на экран надо добавить как-то

        counter = (counter + 1) % k

        pygame.display.update()
        timer.tick(fps)


if __name__ == "__main__":
    x = 20
    my_animation(6, 5, 24, x, "Firework.png", (300, 300))