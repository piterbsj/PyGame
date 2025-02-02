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
        for obst in self.coord:
            box_hitbox = pygame.rect.Rect(obst[0], obst[1], obst[2], obst[3])

            self.x, self.y = 0, 0
            self.all_sprites_obst = pygame.sprite.Group()
            sprite_obst = pygame.sprite.Sprite()
            sprite_obst.image = pygame.image.load('image/obd.jpg')
            sprite_obst.image = pygame.transform.scale(sprite_obst.image, (50, 50))
            self.mask = pygame.mask.from_surface(sprite_obst.image)
            sprite_obst.rect = box_hitbox
            self.all_sprites_obst = pygame.sprite.GroupSingle()
            self.all_sprites_obst.add(sprite_obst)

            self.newcoord.append([self.all_sprites_obst, box_hitbox, box_hitbox.x])

    def draw(self, screen: pygame.Surface):
        for obst in self.newcoord:
            obst[0].draw(screen)

    def moveall(self, keys):
        if keys[pygame.K_RIGHT]:
            for i in self.newcoord:
                i[2] -= (Obstacles.SPEED * 150) / 1000
                i[1].x = i[2]
        if keys[pygame.K_LEFT]:
            for i in self.newcoord:
                i[2] += (Obstacles.SPEED * 150) / 1000
                i[1].x = i[2]