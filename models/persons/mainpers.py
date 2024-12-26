import pygame
from pygame import *

class Pony:             #главный персонаж
    def __init__(self):
        self.y = 400
        self.image = pygame.image.load('image/ponyy.png')
        self.heig = 480
        self.velocity_y = 0
        self.gravity = 1
        self.jump_strength = -15
        self.is_jumping = False
        self.pony_hitbox = pygame.rect.Rect(200, 400, 80, 80)
        self.pony_color = pygame.color.Color((148, 0, 0))

    def jump(self):                             #прыжок
        if not self.is_jumping:
            self.velocity_y = self.jump_strength
            self.is_jumping = True

    def update(self):                           #обновление пощиции
        if self.is_jumping:
            self.pony_hitbox.y += self.velocity_y
            self.velocity_y += self.gravity

            if self.pony_hitbox.y >= self.heig - self.pony_hitbox.height:
                self.pony_hitbox.y = self.heig - self.pony_hitbox.height
                self.is_jumping = False

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.pony_color, self.pony_hitbox, width=2)