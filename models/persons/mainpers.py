import os.path

import pygame
#from PyQt6.QtWidgets.QWidget import window
from pygame import *
from pygame import Rect

from models.methods import load_image
from models.interface import Obstacles

obs = Obstacles()

pygame.init()

class Pony(pygame.sprite.Sprite):   #главный персонаж

    image = load_image("image/ponyy.png")
    image_pony = load_image("image/retry.png")

    def __init__(self, *groups):
        super().__init__(*groups)
        self.y = 400
        self.heig = 480
        self.velocity_y = 0
        self.gravity = 1
        self.jump_strength = -20
        self.is_jumping = False
        self.pony_hitbox = pygame.rect.Rect(200, 400, 80, 80)
        self.pony_color = pygame.color.Color((148, 0, 0))

        self.x, self.y = 0, 0    #добавление спрайта
        self.all_sprites = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite()
        self.image = Pony.image
        self.sprite.image = pygame.transform.scale(self.image, (80, 80))
        self.mask = pygame.mask.from_surface(self.sprite.image)
        self.sprite.rect = self.pony_hitbox
        self.mask = pygame.mask.from_surface(self.sprite.image)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.sprite)

    def jump(self):                             #прыжок
        if not self.is_jumping:
            self.velocity_y = self.jump_strength
            self.is_jumping = True


    def under(self):
        pass

    def update(self, enemies):                           #обновление пощиции
        if self.is_jumping:
            self.pony_hitbox.y += self.velocity_y
            self.velocity_y += self.gravity

            if self.pony_hitbox.y >= self.heig - self.pony_hitbox.height:
                self.pony_hitbox.y = self.heig - self.pony_hitbox.height
                self.is_jumping = False

        collided_enemy = pygame.sprite.spritecollideany(self.sprite, enemies.all_sprites_evil)
        if collided_enemy != None:
            self.sprite.image = Pony.image_pony


    def change_image(self):
        pass


    def draw(self, screen: pygame.Surface,  is_show_hitbox=True):   #отрисовка спрайта
        if is_show_hitbox:
            self.all_sprites.draw(screen)

