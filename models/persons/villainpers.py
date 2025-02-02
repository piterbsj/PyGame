import pygame

class Snail:                   #улитки
    SPEED = 50
    def __init__(self, n=1):
        self.levels = {1: [1700, 1900, 3200],
                       2: []}
        self.spawn = []
        self.newrect(1)


    def newrect(self, n):
        sp = self.levels[n]
        for i in sp:
            zlo_hitbox = pygame.rect.Rect(i, 400, 65, 65)

            self.x, self.y = 0, 0 # добавление спрайта трава
            self.all_sprites_evil = pygame.sprite.Group()
            sprite_evil = pygame.sprite.Sprite()
            sprite_evil.image = pygame.image.load('image/devil.png')
            sprite_evil.image = pygame.transform.scale(sprite_evil.image, (65, 65))
            self.mask = pygame.mask.from_surface(sprite_evil.image)
            sprite_evil.rect = zlo_hitbox
            self.all_sprites_evil = pygame.sprite.GroupSingle()
            self.all_sprites_evil.add(sprite_evil)

            self.spawn.append([self.all_sprites_evil, zlo_hitbox, zlo_hitbox.x])

    def draw(self, screen: pygame.Surface):
        for i in self.spawn:
            i[0].draw(screen)

    def move(self, tick: 10):
        for info in self.spawn:
            info[2] -= (Snail.SPEED * 155) / 1000
            info[1].x = info[2]