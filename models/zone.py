import pygame


class Background:
    SPEED = 100

    def __init__(self):
        self.x = 0
        self.background_zone_hitbox = pygame.rect.Rect(0, 0, 5000, 600)
        self.background_zone_color = pygame.color.Color((216, 191, 216))

        self.ground_hitbox = pygame.rect.Rect(0, 480, 5000, 200)
        self.ground_color = pygame.color.Color((156, 112, 62))

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.background_zone_color, self.background_zone_hitbox, width=0)
        pygame.draw.rect(screen, self.ground_color, self.ground_hitbox, width=0)

    def move(self, tick: float):
        self.x -= (Background.SPEED * tick) / 1000
        self.background_zone_hitbox.x = self.x

class Points:
    def __init__(self):
        self.points_zone_hitbox = pygame.rect.Rect(0, 0, 150, 100)
        self.points_zone_color = pygame.color.Color((179, 40, 33))

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.points_zone_color, self.points_zone_hitbox, width=2)

class Money:
    def __init__(self):
        self.money_zone_hitbox = pygame.rect.Rect(150, 0, 150, 100)
        self.money_zone_color = pygame.color.Color((255, 195, 31))

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.money_zone_color, self.money_zone_hitbox, width=2)

class Time:
    def __init__(self):
        self.time_zone_hitbox = pygame.rect.Rect(800, 0, 200, 100)
        self.time_zone_color = pygame.color.Color((102, 255, 0))


        self.cash_font = pygame.font.Font(None, 30)
        self.cash_text = self.cash_font.render("10", True, (0, 0, 0))

    def text(self, screen: pygame.Surface):
        screen.blit(self.cash_text, (10, 10))


    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.time_zone_color, self.time_zone_hitbox, width=2)