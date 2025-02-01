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
            zlo_color = pygame.color.Color((148, 0, 0))
            self.spawn.append([zlo_color, zlo_hitbox, zlo_hitbox.x])

    def draw(self, screen: pygame.Surface):
        for info in self.spawn:
            pygame.draw.rect(screen, info[0], info[1], width=0)

    def move(self, tick: 10):
        for info in self.spawn:
            info[2] -= (Snail.SPEED * 155) / 1000
            info[1].x = info[2]