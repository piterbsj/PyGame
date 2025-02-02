import os.path

import pygame
#from PyQt6.QtWidgets.QWidget import window
from pygame import *
from models.methods import load_image

class Pony:             #главный персонаж
    image = "image/ponyy.png"

    def __init__(self, pic, possition):
        self.y = 400
        self.heig = 480
        self.velocity_y = 0
        self.gravity = 1
        self.jump_strength = -20
        self.is_jumping = False
        self.pony_hitbox = pygame.rect.Rect(200, 400, 80, 80)
        self.pony_color = pygame.color.Color((148, 0, 0))

        self.x, self.y = possition    #добавление спрайта
        self.all_sprites = pygame.sprite.Group()
        sprite = pygame.sprite.Sprite()
        sprite.image = pygame.image.load(f'image/{pic}')
        sprite.image = pygame.transform.scale(sprite.image, (80, 80))
        self.mask = pygame.mask.from_surface(sprite.image)
        sprite.rect = self.pony_hitbox
        self.all_sprites = pygame.sprite.GroupSingle()
        self.all_sprites.add(sprite)



    def jump(self):                             #прыжок
        if not self.is_jumping:
            self.velocity_y = self.jump_strength
            self.is_jumping = True

    def under(self):
        pass

    def update(self):                           #обновление пощиции
        if self.is_jumping:
            self.pony_hitbox.y += self.velocity_y
            self.velocity_y += self.gravity

            if self.pony_hitbox.y >= self.heig - self.pony_hitbox.height:
                self.pony_hitbox.y = self.heig - self.pony_hitbox.height
                self.is_jumping = False

        #if self.pony_hitbox.x == из файла кортеж and self.pony_hitbox.y == кортеж блока:




    def draw(self, screen: pygame.Surface,  is_show_hitbox=True):   #отрисовка спрайта
        if is_show_hitbox:
            self.all_sprites.draw(screen)