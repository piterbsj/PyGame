import pygame

class Snail:                   #улитки
    SPEED = 50
    def __init__(self):
        self.zlo_hitbox = pygame.rect.Rect(800, 400, 65, 65)
        self.x = self.zlo_hitbox.x
        self.zlo_color = pygame.color.Color((148, 0, 0))

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.zlo_color, self.zlo_hitbox, width=2)

    def move(self, tick: 10):
        self.x -= (Snail.SPEED * 180) / 1000
        self.zlo_hitbox.x = self.x