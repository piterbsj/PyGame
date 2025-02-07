import pygame

class Obstacles:                #препятствия
    SPEED = 50

    def __init__(self, n=1):
        self.readtxt(n)
        self.newcoord = []
        self.newrect()

    def readtxt(self, n):
        if n == 1:
            with open('level/level_1.txt') as file:
                self.coord = [list(map(int, i.split(','))) for i in file]
        elif n == 2:
            with open('level/level_2.txt') as file:
                self.coord = [list(map(int, i.split(','))) for i in file]

    def newrect(self):
        self.all_sprites_obst = pygame.sprite.Group()
        for obst in self.coord:
            box_hitbox = pygame.rect.Rect(obst[0], obst[1], obst[2], obst[3])

            self.x, self.y = 0, 0
            sprite_obst = pygame.sprite.Sprite()
            if obst[4] == 0:
                sprite_obst.image = pygame.image.load('image/obd.jpg')
            else:
                sprite_obst.image = pygame.image.load('image/box.png')

            sprite_obst.image = pygame.transform.scale(sprite_obst.image, (obst[2], obst[3]))
            self.mask = pygame.mask.from_surface(sprite_obst.image)
            sprite_obst.rect = box_hitbox
            self.all_sprites_obst.add(sprite_obst)

            self.newcoord.append([box_hitbox, box_hitbox.x, self.mask])

    def draw(self, screen: pygame.Surface):
        self.all_sprites_obst.draw(screen)


    def moveall(self, keys):
        if keys[pygame.K_RIGHT]:
            for i in self.newcoord:
                i[1] -= (Obstacles.SPEED * 150) / 1000
                i[0].x = i[1]
        if keys[pygame.K_LEFT]:
            for i in self.newcoord:
                i[1] += (Obstacles.SPEED * 150) / 1000
                i[0].x = i[1]