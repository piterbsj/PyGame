import pygame
from pygame import*
from datetime import datetime


from models.zone import Background, Level, Money, Points
from models.persons.mainpers import Pony
from models.persons.villainpers import Snail
from models.methods import load_image
from models.interface import Obstacles

LEVEL = 1

def game(screen):
    background_zone = Background('backgroundnew.jpg',(0, 0))
    ground = Background('ground.jpg',(0, 0))
    level_zone = Level(str(LEVEL))
    money_zone = Money()
    points_zone = Points()
    boxes = Obstacles(LEVEL)
    zlo = Snail(LEVEL)
    pony = Pony('ponyy.png', (0, 0))
    move = Background('backgroundnew.jpg', (0, 0))

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
                if event.key == pygame.K_TAB:
                    return 4
        for  i in zlo.spawn:
            flag = sprite.groupcollide(pony.all_sprites, i[0], True, False)
            if not flag == {}:
                print('убило')


        timer += clock.tick()

        pony.update()
        #zlo.update1()

        screen.fill((0, 191, 216))

        keys = pygame.key.get_pressed()
        background_zone.draw_bc(screen)
        background_zone.move(keys)
        boxes.moveall(keys)

        boxes.draw(screen)
        zlo.draw(screen)
        zlo.move(screen)
        ground.draw_gr(screen)
        pony.draw(screen)
        level_zone.text(screen)
        pygame.display.flip()
        clock.tick(30)

def startwindow(screen, numlevel=1):
    clock = pygame.time.Clock()
    listoftext = ['Play', 'Change level', 'Exit']
    backgroundphoto = pygame.rect.Rect(350, 130, 300, 60)
    backgroundphoto_color = pygame.color.Color((156, 130, 174))
    startgame = pygame.rect.Rect(300, 300, 100, 100)
    changelevel = pygame.rect.Rect(450, 300, 100, 100)
    exit = pygame.rect.Rect(600, 300, 100, 100)

    sprite_play = pygame.sprite.Sprite()
    sprite_play.image = pygame.image.load('image/starticon.png')
    sprite_play.image = pygame.transform.scale(sprite_play.image, (100, 100))
    sprite_play.rect = startgame
    all_sprites_play = pygame.sprite.GroupSingle()
    all_sprites_play.add(sprite_play)

    sprite_ch = pygame.sprite.Sprite()
    sprite_ch.image = pygame.image.load('image/levelicon.png')
    sprite_ch.image = pygame.transform.scale(sprite_ch.image, (100, 100))
    sprite_ch.rect = changelevel
    all_sprites_ch = pygame.sprite.GroupSingle()
    all_sprites_ch.add(sprite_ch)

    sprite_e = pygame.sprite.Sprite()
    sprite_e.image = pygame.image.load('image/exiticon.png')
    sprite_e.image = pygame.transform.scale(sprite_e.image, (100, 100))
    sprite_e.rect = exit
    all_sprites_e = pygame.sprite.GroupSingle()
    all_sprites_e.add(sprite_e)

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
                    return 3
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

        all_sprites_play.draw(screen)
        all_sprites_ch.draw(screen)
        all_sprites_e.draw(screen)

        pygame.display.flip()

def changelevelwindow(screen, numlevel=1):
    global LEVEL

    clock = pygame.time.Clock()
    font_size = 54
    font = pygame.font.Font(None, font_size)
    text_surface = font.render('Which level will you choose?', True, pygame.Color('black'))
    text_rect = text_surface.get_rect(center=(380, 50))

    levelone = pygame.rect.Rect(100, 120, 150, 150)
    leveltwo = pygame.rect.Rect(280, 120, 150, 150)
    exitmenu = pygame.rect.Rect(10, 10, 70, 70)

    sprite_levelone = pygame.sprite.Sprite()
    sprite_levelone.image = pygame.image.load('image/level1.png')
    sprite_levelone.image = pygame.transform.scale(sprite_levelone.image, (150, 150))
    sprite_levelone.rect = levelone
    all_sprites_levelone = pygame.sprite.GroupSingle()
    all_sprites_levelone.add(sprite_levelone)

    sprite_leveltwo = pygame.sprite.Sprite()
    sprite_leveltwo.image = pygame.image.load('image/level2.png')
    sprite_leveltwo.image = pygame.transform.scale(sprite_leveltwo.image, (150, 150))
    sprite_leveltwo.rect = leveltwo
    all_sprites_leveltwo = pygame.sprite.GroupSingle()
    all_sprites_leveltwo.add(sprite_leveltwo)

    sprite_exitmenu = pygame.sprite.Sprite()
    sprite_exitmenu.image = pygame.image.load('image/exit2.png')
    sprite_exitmenu.image = pygame.transform.scale(sprite_exitmenu.image, (70, 70))
    sprite_exitmenu.rect = exitmenu
    all_sprites_exitmenu = pygame.sprite.GroupSingle()
    all_sprites_exitmenu.add(sprite_exitmenu)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 10 < x < 80 and 10 < y < 80:
                    return 1
                if 100 < x < 250 and 120 < y < 270:
                    LEVEL = 1
                    return 2
                if 300 < x < 450 and 120 < y < 270:
                    LEVEL = 2
                    return 2

        tick = clock.tick()
        screen.fill(pygame.Color(156, 110, 174))
        screen.blit(text_surface, text_rect)

        all_sprites_levelone.draw(screen)
        all_sprites_leveltwo.draw(screen)
        all_sprites_exitmenu.draw(screen)
        pygame.display.flip()

def stopwindow(screen, numlevel=1):
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0

def win(screen, numlevel=1):
    pass