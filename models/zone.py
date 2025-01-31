import pygame


class Background:
    SPEED = 50

    def __init__(self, pic, possition):
        self.x = 0
        self.background_zone_hitbox = pygame.rect.Rect(0, 0, 5000, 465)
        self.background_zone_color = pygame.color.Color((255, 191, 216))

        self.ground_hitbox = pygame.rect.Rect(0, 465, 5000, 135)
        self.ground_color = pygame.color.Color((0, 0, 0))

        self.x, self.y = possition #добавление спрайта задний фон
        self.all_sprites_bc = pygame.sprite.Group()
        sprite_bc = pygame.sprite.Sprite()
        sprite_bc.image = pygame.image.load(f'image/{pic}')
        sprite_bc.image = pygame.transform.scale(sprite_bc.image, (5000, 600))
        sprite_bc.rect = self.background_zone_hitbox
        self.all_sprites = pygame.sprite.GroupSingle()
        self.all_sprites_bc.add(sprite_bc)

        self.x, self.y = possition    #добавление спрайта трава
        self.all_sprites_gr = pygame.sprite.Group()
        sprite_gr = pygame.sprite.Sprite()
        sprite_gr.image = pygame.image.load(f'image/{pic}')
        sprite_gr.image = pygame.transform.scale(sprite_gr.image, (5000, 135))
        sprite_gr.rect = self.ground_hitbox
        self.all_sprites = pygame.sprite.GroupSingle()
        self.all_sprites_gr.add(sprite_gr)

    def move(self, keys):
        if self.x >= -3950:
            if keys[pygame.K_RIGHT]:
                self.x -= (Background.SPEED * 150) / 1000
                self.background_zone_hitbox.x = self.x
            if keys[pygame.K_LEFT]:
                self.x += (Background.SPEED * 150) / 1000
                self.background_zone_hitbox.x = self.x


    def draw_bc(self, screen: pygame.Surface):
        self.all_sprites_bc.draw(screen)

    def draw_gr(self, screen: pygame.Surface):
        self.all_sprites_gr.draw(screen)


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

class Level:
    def __init__(self, number):
        self.level_zone_hitbox = pygame.rect.Rect(800, 0, 200, 100)
        self.level_zone_color = pygame.color.Color((102, 255, 0))

        self.cash_font = pygame.font.Font(None, 40)
        self.cash_text = self.cash_font.render(f'Level {number}', True, (0, 0, 0))


    def text(self, screen: pygame.Surface):
        screen.blit(self.cash_text, (10, 10))

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.level_zone_color, self.level_zone_hitbox, width=2)