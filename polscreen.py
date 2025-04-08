import pygame
from pygame import*

from models.zone import Background, Level, Money, Points
from models.persons.mainpers import Pony
from models.persons.villainpers import Snail
from models.methods import load_image
from models.obstacles import Obstacles
from models.zone import Money, MoneyCounter
from animation.firework import Animation

LEVEL = 1
LOSE = False
POINTS = 0
COINS = 0

pygame.init()

def game(screen):
    global LOSE
    global POINTS
    global COINS

    counter_for_animation = 0

    background_zone = Background('backgroundnew.jpg',(0, 0))
    ground = Background('ground.jpg',(0, 0))
    level_zone = Level(str(LEVEL))
    money = Money()
    money_zone = MoneyCounter('game')
    points_zone = Points()
    boxes = Obstacles(LEVEL)
    enemy = Snail(LEVEL)
    pony = Pony()
    x = 20                                  #частота кадров анимации
    animation = Animation(6, 5, 24, x, "animation/Firework.png", (500, 200))

    running = True
    clock = pygame.time.Clock()

    all_sound = pygame.mixer.Sound('music/music_for_game.mp3')
    all_sound.set_volume(0.2)
    all_sound.play()

    jump_sound = pygame.mixer.Sound('music/jump_sound.wav')
    jump_sound.set_volume(0.2)

    game_over = pygame.mixer.Sound('music/game_over.wav')
    game_over.set_volume(0.2)

    win_sound = pygame.mixer.Sound('music/win_sound.wav')
    win_sound.set_volume(0.2)

    while running:
        if LOSE:
            all_sound.stop()
            game_over.play()
            pygame.time.delay(3000)
            pony.update(enemy)
            return 4
        elif background_zone.win:
            all_sound.stop()
            win_sound.play()
            while counter_for_animation < 100:
                animation.update(screen)
                pygame.display.update()
                animation.timer.tick(animation.fps)
                time.delay(10)
                counter_for_animation += 1
            background_zone.win = False
            return 4

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    stop_window(screen)
                if event.key == pygame.K_SPACE:
                    jump_sound.play()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pony.image = pony.image_pony
                pony.update(enemy)

        for im in boxes.newcoord:
            if pony.pony_hitbox.colliderect(im[0]):
                if pony.velocity_y > 0:  # Проверка, движется ли игрок вниз
                    pony.pony_hitbox.bottom = im[0].top + 10
                    pony.velocity_y = 6
                    pony.is_jumping = False
                    pony.update(enemy)

        for i in money.newcoord:
            flag = sprite.groupcollide(i[3], pony.all_sprites,True,False)
            if not flag == {}:
                money_zone.update(screen)

        for i in enemy.all_sprites_evil:
            flag = pony.pony_hitbox.colliderect(i)
            if not flag == False:
                LOSE = True

        keys = pygame.key.get_pressed()

        for i in boxes.all_sprites_boxes:
            f = pony.pony_hitbox.colliderect(i)                 #флаг для проверки коллайда
            if f:
                pony.is_jumping = False
                pony.jump(screen, keys)
            if not f:
                pony.is_jumping = True

        pony.update(enemy)


        screen.fill((0, 191, 216))
        keys = pygame.key.get_pressed()
        background_zone.move(keys)
        background_zone.draw_bc(screen)
        boxes.moveall(keys)
        money.moveall(keys)
        points_zone.text(screen)
        points_zone.update(screen, keys)
        POINTS = points_zone.points
        COINS = money_zone.money_counter
        boxes.draw(screen)
        money_zone.draw(screen)
        money_zone.text(screen)
        money.draw(screen)
        enemy.draw(screen)
        enemy.move(screen, keys)
        ground.draw_gr(screen)
        pony.draw(screen)
        pony.jump(screen, keys)
        level_zone.text(screen)
        pygame.display.flip()
        clock.tick(30)

def start_window(screen):
    clock = pygame.time.Clock()

    list_of_text = ["Let's play!", 'Play', 'Change level', 'Exit']
    sizes_text = [54, 25, 25, 25]
    coord_text = [(500, 150), (350, 410), (500, 410), (650, 410)]

    list_surface_text = text_for_window(list_of_text, sizes_text, coord_text)

    backgroundphoto = pygame.rect.Rect(350, 130, 300, 60)
    backgroundphoto_color = pygame.color.Color((156, 130, 174))

    start_game = pygame.rect.Rect(300, 300, 100, 100)
    change_level = pygame.rect.Rect(450, 300, 100, 100)
    exit_from_game = pygame.rect.Rect(600, 300, 100, 100)

    rects = [start_game, change_level, exit_from_game]
    pics = ['image/starticon.png', 'image/levelicon.png', 'image/exiticon.png']
    sizes = [(100, 100), (100, 100), (100, 100)]

    all_sprites_group = all_sprites(pics, rects, sizes)

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

        for i in list_surface_text:
            screen.blit(i[0], i[1])
        all_sprites_group.draw(screen)

        pygame.display.flip()

def change_level_window(screen):
    global LEVEL

    font_size = 54
    font = pygame.font.Font(None, font_size)
    text_surface = font.render('Which level will you choose?', True, pygame.Color('black'))
    text_rect = text_surface.get_rect(center=(380, 50))

    level_one = pygame.rect.Rect(100, 120, 150, 150)
    level_two = pygame.rect.Rect(280, 120, 150, 150)
    exit_menu = pygame.rect.Rect(10, 10, 70, 70)

    rects = [level_one, level_two, exit_menu]
    pics = ['image/level1.png', 'image/level2.png', 'image/exit2.png']
    sizes = [(150, 150), (150, 150), (70, 70)]

    all_sprites_group = all_sprites(pics, rects, sizes)

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

        screen.fill(pygame.Color(156, 110, 174))
        screen.blit(text_surface, text_rect)

        all_sprites_group.draw(screen)
        pygame.display.flip()

def stop_window(screen):                                                #пауза
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        screen.fill(pygame.Color(156, 110, 174))

        font = pygame.font.Font(None, 74)
        text = font.render('PAUSE', True, pygame.Color('black'))
        text_rect = text.get_rect(center=(500, 200))
        screen.blit(text, text_rect)

        pygame.display.flip()

def win_or_loss(screen):
    global LOSE
    winorloss = {'w': "Ты молодец!",
                 'l': "You've lost! Anew?"}
    if LOSE:
        LOSE = False
        result = 'l'
    else:
        result = 'w'

    money_zone = MoneyCounter('final', COINS)

    list_of_text = [winorloss[result],'Иди на общий балкон и скинь оттуда фотографию', 'Retry', 'Change level', 'Score:', str(POINTS)]
    sizes_text = [50, 50, 25, 25, 40, 40]
    coord_text = [(500, 180), (500, 230), (390, 400), (600, 400), (50, 20), (50, 50)]

    texts = text_for_window(list_of_text, sizes_text, coord_text)

    reset = pygame.rect.Rect(320, 250, 150, 150)
    change_level = pygame.rect.Rect(520, 250, 150, 150)

    rects = [reset, change_level]
    pics = ['image/retry.png', 'image/levelicon.png']
    sizes = [(150, 150), (150, 150)]

    group_all_sprites = all_sprites(pics, rects, sizes)

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
        money_zone.draw(screen)
        money_zone.text(screen)
        pygame.display.flip()


def all_sprites(pics, rects, sizes):                #создание групп спрайтов для каждого окна
    all_sprites_group = pygame.sprite.Group()
    for pic in range(len(pics)):
        every_sprite = pygame.sprite.Sprite()
        every_sprite.image = pygame.image.load(pics[pic])
        every_sprite.image = pygame.transform.scale(every_sprite.image, sizes[pic])
        every_sprite.rect = rects[pic]
        all_sprites_group.add(every_sprite)
    return all_sprites_group

def text_for_window(text, size, coord):
    texts = []
    for i in range(len(text)):
        font = pygame.font.Font(None, size[i])
        text_surface = font.render(text[i], True, pygame.Color('black'))
        text_rect = text_surface.get_rect(center=coord[i])
        texts.append([text_surface, text_rect])
    return texts