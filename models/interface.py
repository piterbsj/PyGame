import pygame

class Obstacles:                #препятствия
    SPEED = 50


    def __init__(self, n=1):
        self.readtxt(n)
        self.newcoord = []
        self.newrect()

        self.box1_hitbox = pygame.rect.Rect(500, 200, 50, 50)
        self.x1 = self.box1_hitbox.x
        self.box1_color = pygame.color.Color((253, 233, 16))

        self.box2_hitbox = pygame.rect.Rect(1000, 300, 300, 50)
        self.x2 = self.box2_hitbox.x
        self.box2_color = pygame.color.Color((253, 233, 16))

        self.box3_hitbox = pygame.rect.Rect(1125, 100, 50, 50)
        self.x3 = self.box3_hitbox.x
        self.box3_color = pygame.color.Color((253, 233, 16))

        self.box4_hitbox = pygame.rect.Rect(1900, 400, 70, 80)
        self.x4 = self.box4_hitbox.x
        self.box4_color = pygame.color.Color((253, 233, 16))

        self.box5_hitbox = pygame.rect.Rect(2700, 365, 70, 100)
        self.x5 = self.box5_hitbox.x
        self.box5_color = pygame.color.Color((253, 233, 16))

        self.box6_hitbox = pygame.rect.Rect(3400, 275, 70, 190)
        self.x6 = self.box6_hitbox.x
        self.box6_color = pygame.color.Color((253, 233, 16))

    def draw1(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.box1_color, self.box1_hitbox, width=0)

    def move1(self, tick: 10):
        self.x1 -= (Obstacles.SPEED * 150) / 1000
        self.box1_hitbox.x = self.x1

    def draw2(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.box2_color, self.box2_hitbox, width=0)

    def move2(self, tick: 10):
        self.x2 -= (Obstacles.SPEED * 150) / 1000
        self.box2_hitbox.x = self.x2

    def draw3(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.box3_color, self.box3_hitbox, width=0)

    def move3(self, tick: 10):
        self.x3 -= (Obstacles.SPEED * 150) / 1000
        self.box3_hitbox.x = self.x3

    def draw4(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.box4_color, self.box4_hitbox, width=0)

    def move4(self, tick: 10):
        self.x4 -= (Obstacles.SPEED * 150) / 1000
        self.box4_hitbox.x = self.x4

    def draw5(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.box5_color, self.box5_hitbox, width=0)

    def move5(self, tick: 10):
        self.x5 -= (Obstacles.SPEED * 150) / 1000
        self.box5_hitbox.x = self.x5

    def draw6(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.box6_color, self.box6_hitbox, width=0)

    def move6(self, tick: 10):
        self.x6 -= (Obstacles.SPEED * 150) / 1000
        self.box6_hitbox.x = self.x6

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
            self.newcoord.append((box_hitbox, box_color))

    def drawhz(self, screen: pygame.Surface):
        for obst in self.newcoord:
            pygame.draw.rect(screen, obst[1], obst[0], width=0)