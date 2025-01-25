import pygame
from pygame import*
from datetime import datetime

from pygame.examples.go_over_there import running

from models.zone import Background, Time, Money, Points
from models.persons.mainpers import Pony
from models.methods import load_image


def game(screen):
    background_zone = Background('background1.jpg',(0,0))
    ground = Background('ground.png',(0,0))
    time_zone = Time()
    money_zone = Money()
    points_zone = Points()
    pony = Pony('ponyy.png', (0,0))
    move = Background('background1.jpg', (0,0))

    running = True
    isJumping = False
    clock = pygame.time.Clock()
    timer = clock.tick()
    stopBack = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not isJumping:
                    pony.jump()
                if event.key == pygame.K_d:
                    stopBack = not stopBack

        timer += clock.tick()

        pony.update()

        screen.fill((0, 191, 216))

        background_zone.draw_bc(screen)
        if stopBack:
            background_zone.move(screen)
        ground.draw_gr(screen)
        time_zone.draw(screen)
        money_zone.draw(screen)
        points_zone.draw(screen)
        pony.draw(screen)
        time_zone.text(screen)

        pygame.display.flip()
        clock.tick(30)

def startwindow(screen):
    clock = pygame.time.Clock()
    listoftext = ['Play', 'Change level', 'Exit']
    backgroundphoto = pygame.rect.Rect(350, 130, 300, 60)
    backgroundphoto_color = pygame.color.Color((156, 130, 174))
    startgame = pygame.rect.Rect(300, 300, 100, 100)
    changelevel = pygame.rect.Rect(450, 300, 100, 100)
    exit = pygame.rect.Rect(600, 300, 100, 100)

    font_size, font_pushs = 54, 25
    sp = [350, 410]
    font = pygame.font.Font(None, font_size)
    font_push = pygame.font.Font(None, font_pushs)

    text_surface = font.render("Let's play!", True, pygame.Color('black'))
    text_rect = text_surface.get_rect(center=(500, 150))

    push_surface1 = font_push.render(listoftext[0], True, pygame.Color('black'))
    push_rect1 = push_surface1.get_rect(center=(sp[0], sp[1]))
    push_surface2 = font_push.render(listoftext[1], True, pygame.Color('black'))
    push_rect2 = push_surface2.get_rect(center=(sp[0] + 150, sp[1]))
    push_surface3 = font_push.render(listoftext[2], True, pygame.Color('black'))
    push_rect3 = push_surface3.get_rect(center=(sp[0] + 300, sp[1]))

    running = True
    while running:
        # Просматриваем все события
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 300 < x < 400 and 300 < y < 400:
                    return 2
                if 450 < x < 600 and 300 < y < 400:
                    pass
                if 650 < x < 800 and 300 < y < 400:
                    return 0

        tick = clock.tick()
        screen.fill(pygame.Color(156, 110, 174))
        count = 0
        pygame.draw.rect(screen, backgroundphoto_color, backgroundphoto)
        screen.blit(text_surface, text_rect)
        screen.blit(push_surface1, push_rect1)
        screen.blit(push_surface2, push_rect2)
        screen.blit(push_surface3, push_rect3)

        pygame.draw.rect(screen, pygame.Color('white'), startgame)
        pygame.draw.rect(screen, pygame.Color('black'), changelevel)
        pygame.draw.rect(screen, pygame.Color('white'), exit)
        pygame.display.flip()

def changelevelwindow(screen):
    clock = pygame.time.Clock()

    font_size = 54
    font = pygame.font.Font(None, font_size)
    text_surface = font.render('Which level will you choose?', True, pygame.Color('black'))
    text_rect = text_surface.get_rect(center=(380, 50))

    levelone = pygame.rect.Rect(100, 120, 150, 150)
    leveltwo = pygame.rect.Rect(280, 120, 150, 150)
    exitmenu = pygame.rect.Rect(10, 10, 70, 70)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 10 < x < 80 and 10 < y < 80:
                    return 1

        tick = clock.tick()
        screen.fill(pygame.Color(156, 110, 174))
        screen.blit(text_surface, text_rect)

        pygame.draw.rect(screen, pygame.color.Color((156, 130, 174)), levelone)
        pygame.draw.rect(screen, pygame.color.Color((156, 130, 174)), leveltwo)
        pygame.draw.rect(screen, pygame.color.Color((156, 130, 174)), exitmenu)
        pygame.display.flip()

def stopwindow(screen):
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
