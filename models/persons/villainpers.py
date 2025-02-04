import pygame

from models.persons.mainpers import Pony

pony = Pony()

class Snail:                   #улитки
    SPEED = 50
    def __init__(self, n=1):
        self.levels = {1: [1700, 2100, 3200],
                       2: []}
        self.spawn = []
        self.newrect(n)


    def newrect(self, n):
        sp = self.levels[n]
        for i in sp:
            self.enemy_hitbox = pygame.rect.Rect(i, 400, 65, 65)
            self.x, self.y = 0, 0
            self.all_sprites_evil = pygame.sprite.Group()
            sprite_evil = pygame.sprite.Sprite()
            sprite_evil.image = pygame.image.load('image/devil.png')
            sprite_evil.image = pygame.transform.scale(sprite_evil.image, (70, 70))
            self.mask = pygame.mask.from_surface(sprite_evil.image)
            sprite_evil.rect = self.enemy_hitbox
            self.all_sprites_evil = pygame.sprite.GroupSingle()
            self.all_sprites_evil.add(sprite_evil)

            self.spawn.append([self.all_sprites_evil, self.enemy_hitbox, self.enemy_hitbox.x])

    def draw(self, screen: pygame.Surface):
        for i in self.spawn:
            i[0].draw(screen)

    def move(self, screen: pygame.Surface, keys):
        if keys[pygame.K_RIGHT]:
            for info in self.spawn:
                info[2] -= (Snail.SPEED * 170) / 1000
                info[1].x = info[2]
        elif keys[pygame.K_LEFT]:
            for info in self.spawn:
                info[2] -= (Snail.SPEED * 80) / 1000
                info[1].x = info[2]
        else:
            for info in self.spawn:
                info[2] -= (Snail.SPEED * 120) / 1000
                info[1].x = info[2]


    def update1(self):
        if not pygame.sprite.collide_mask(self, pony.mask):
            self.enemy_hitbox = self.enemy_hitbox.move(0, 1)
