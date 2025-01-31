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
            pass

    def newrect(self):
        for obst in self.coord:
            box_hitbox = pygame.rect.Rect(obst[0], obst[1], obst[2], obst[3])
            box_color = pygame.color.Color((253, 233, 16))
            self.newcoord.append([box_hitbox, box_color, box_hitbox.x])

    def draw(self, screen: pygame.Surface):
        for obst in self.newcoord:
            pygame.draw.rect(screen, obst[1], obst[0], width=0)

    def moveall(self, tick: 10):
        for i in self.newcoord:
            i[2] -= (Obstacles.SPEED * 150) / 1000
            i[0].x = i[2]