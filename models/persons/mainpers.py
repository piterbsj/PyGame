import pygame
from pygame import *

class Pony:             #главный персонаж
    def __init__(self):
        self.pony_hitbox = pygame.rect.Rect(200, 400, 80, 80)
        self.pony_color = pygame.color.Color((148, 0, 0))

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.pony_color, self.pony_hitbox, width=2)