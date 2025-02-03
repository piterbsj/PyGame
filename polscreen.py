import pygame
from pygame import*


from models.zone import Background, Level, Money, Points
from models.persons.mainpers import Pony
from models.persons.villainpers import Snail
from models.methods import load_image
from models.interface import Obstacles

LEVEL = 1
LOSE = False
POINTS = 0

pygame.init()

def game(screen):
    global LOSE
    global POINTS

    background_zone = Background('backgroundnew.jpg',(0, 0))
    ground = Background('ground.jpg',(0, 0))
    level_zone = Level(str(LEVEL))
    money_zone = Money()
    points_zone = Points()
    boxes = Obstacles(LEVEL)
    zlo = Snail(LEVEL)
    pony = Pony()
    move = Background('backgroundnew.jpg', (0, 0))

    running = True
    isJumping = False
    clock = pygame.time.Clock()
    timer = clock.tick()
    while running:
        if LOSE:
            return 5
        elif background_zone.win:
            background_zone.win = False
            return 5

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not isJumping:
                    pony.jump()
                if event.key == pygame.K_TAB:
                    return 4
            if event.type == pygame.MOUSEBUTTONDOWN:
                pony.image = pony.image_pony
                pony.update()

        for im in boxes.newcoord[1::]:
            if pony.pony_hitbox.colliderect(im[1]):
                if pony.velocity_y > 0:  # Проверка, движется ли игрок вниз
                    pony.pony_hitbox.bottom = im[1].top
                    pony.velocity_y = 6
                    pony.update()

        for  i in zlo.spawn:
            flag = sprite.groupcollide(pony.all_sprites, i[0], True, False)
            if not flag == {}:
                LOSE = True
                print('убило')

        for  i in boxes.newcoord:
            if pygame.Rect.colliderect(pony.pony_hitbox, i[1]):
                print("помогите")

        timer += clock.tick()

        pony.update()


        #zlo.update1()

        screen.fill((0, 191, 216))

        keys = pygame.key.get_pressed()
        background_zone.move(keys)
        background_zone.draw_bc(screen)
        boxes.moveall(keys)
        points_zone.text(screen)
        points_zone.update(screen, keys)
        POINTS = points_zone.points
        boxes.draw(screen)
        zlo.draw(screen)
        zlo.move(screen)
        ground.draw_gr(screen)
        pony.draw(screen)
        level_zone.text(screen)
        pygame.display.flip()
        clock.tick(30)

def startwindow(screen):
    clock = pygame.time.Clock()

    listoftext = ["Let's play!", 'Play', 'Change level', 'Exit']
    sizes_text = [54, 25, 25, 25]
    coord_text = [(500, 150), (350, 410), (500, 410), (650, 410)]

    listsurfacetext = textforwindow(listoftext, sizes_text, coord_text)

    backgroundphoto = pygame.rect.Rect(350, 130, 300, 60)
    backgroundphoto_color = pygame.color.Color((156, 130, 174))

    startgame = pygame.rect.Rect(300, 300, 100, 100)
    changelevel = pygame.rect.Rect(450, 300, 100, 100)
    exit = pygame.rect.Rect(600, 300, 100, 100)

    rects = [startgame, changelevel, exit]
    pics = ['image/starticon.png', 'image/levelicon.png', 'image/exiticon.png']
    sizes = [(100, 100), (100, 100), (100, 100)]

    all_sprites_group = allsprites(pics, rects, sizes)

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

        for i in listsurfacetext:
            screen.blit(i[0], i[1])
        all_sprites_group.draw(screen)

        pygame.display.flip()

def changelevelwindow(screen):
    global LEVEL

    clock = pygame.time.Clock()
    font_size = 54
    font = pygame.font.Font(None, font_size)
    text_surface = font.render('Which level will you choose?', True, pygame.Color('black'))
    text_rect = text_surface.get_rect(center=(380, 50))

    levelone = pygame.rect.Rect(100, 120, 150, 150)
    leveltwo = pygame.rect.Rect(280, 120, 150, 150)
    exitmenu = pygame.rect.Rect(10, 10, 70, 70)

    rects = [levelone, leveltwo, exitmenu]
    pics = ['image/level1.png', 'image/level2.png', 'image/exit2.png']
    sizes = [(150, 150), (150, 150), (70, 70)]

    all_sprites_group = allsprites(pics, rects, sizes)

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

        all_sprites_group.draw(screen)
        pygame.display.flip()

def stopwindow(screen):
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0

def winorloss(screen):
    global LOSE
    winorloss = {'w': "You've won! The next level?",
                 'l': "You've lost! Anew?"}
    if LOSE:
        LOSE = False
        result = 'l'
    else:
        result = 'w'

    listoftext = [winorloss[result], 'Retry', 'Change level', 'Score:', str(POINTS)]
    sizes_text = [60, 25, 25, 40, 40]
    coord_text = [(500, 200), (390, 400), (600, 400), (50, 20), (50, 50)]

    texts = textforwindow(listoftext, sizes_text, coord_text)

    reset = pygame.rect.Rect(320, 250, 150, 150)
    changelevel = pygame.rect.Rect(520, 250, 150, 150)

    rects = [reset, changelevel]
    pics = ['image/retry.png', 'image/levelicon.png']
    sizes = [(150, 150), (150, 150)]

    group_all_sprites = allsprites(pics, rects, sizes)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 320 < x < 470 and 250 < y < 400:
                    return 2
                if 520 < x < 770 and 250 < y < 400:
                    return 3

        screen.fill(pygame.Color(156, 110, 174))
        for i in texts:
            screen.blit(i[0], i[1])
        group_all_sprites.draw(screen)
        pygame.display.flip()


def allsprites(pics, rects, sizes):                #создание групп спрайтов для каждого окна
    all_sprites_group = pygame.sprite.Group()
    for pic in range(len(pics)):
        sprite1 = pygame.sprite.Sprite()
        sprite1.image = pygame.image.load(pics[pic])
        sprite1.image = pygame.transform.scale(sprite1.image, sizes[pic])
        sprite1.rect = rects[pic]
        all_sprites_group.add(sprite1)
    return all_sprites_group

def textforwindow(text, size, coord):
    texts = []
    for i in range(len(text)):
        font = pygame.font.Font(None, size[i])
        text_surface = font.render(text[i], True, pygame.Color('black'))
        text_rect = text_surface.get_rect(center=coord[i])
        texts.append([text_surface, text_rect])
    return texts