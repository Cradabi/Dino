# Анимация бегущего дино

import pygame
from random import randint
from dino import Dino
from bird import Bird
from cactus import Cactus
from coin import Coin
from col_fire_water import Col_fire_water
from boss import Boss
from scene1 import cut_scen_1
from scene2 import cut_scen_2
from scene3 import cut_scen_3
from scene4 import cut_scen_4
from settings import sets
import sqlite3

pygame.font.init()

FPS = 60
WIDTH = 1200
HEIGHT = 800

menu_exit = False


def origin_dino(screen, color, score, HI, birthday_code, language, keys, water_number, fire_number, money, d, moon_list,
                sun_list, audio_turn_off):
    global menu_exit
    menu_exit = False
    if not pygame.mixer.music.get_busy() and not audio_turn_off:
        pygame.mixer.music.play(-1)
    up_key = keys[0]
    down_key = keys[1]
    blue_ball_key = keys[2]
    red_ball_key = keys[3]

    color_must = color
    color_rgb = 255
    pygame.init()
    road1 = pygame.image.load('imgs/road.png')
    road1.set_colorkey('white')
    road2 = pygame.image.load('imgs/road.png')
    road2.set_colorkey('white')
    cloud = pygame.image.load('imgs/cloud.png')
    cloud.set_colorkey('white')
    night_sun = pygame.image.load('imgs/night_sun.png')
    night_sun.set_colorkey('black')
    moon = pygame.image.load('imgs/moon.png')
    moon.set_colorkey('black')
    star = pygame.image.load('imgs/star.png')
    star.set_colorkey('black')
    num_0 = pygame.image.load('imgs/0.png')
    num_0.set_colorkey('white')
    num_1 = pygame.image.load('imgs/1.png')
    num_1.set_colorkey('white')
    num_2 = pygame.image.load('imgs/2.png')
    num_2.set_colorkey('white')
    num_3 = pygame.image.load('imgs/3.png')
    num_3.set_colorkey('white')
    num_4 = pygame.image.load('imgs/4.png')
    num_4.set_colorkey('white')
    num_5 = pygame.image.load('imgs/5.png')
    num_5.set_colorkey('white')
    num_6 = pygame.image.load('imgs/6.png')
    num_6.set_colorkey('white')
    num_7 = pygame.image.load('imgs/7.png')
    num_7.set_colorkey('white')
    num_8 = pygame.image.load('imgs/8.png')
    num_8.set_colorkey('white')
    num_9 = pygame.image.load('imgs/9.png')
    num_9.set_colorkey('white')
    nums_dict = {
        '0': num_0,
        '1': num_1,
        '2': num_2,
        '3': num_3,
        '4': num_4,
        '5': num_5,
        '6': num_6,
        '7': num_7,
        '8': num_8,
        '9': num_9
    }

    HI_img = pygame.image.load('imgs/HI.png')
    HI_img.set_colorkey('white')

    small_cactus1 = pygame.image.load('imgs/small_cactus1.png')
    small_cactus1.set_colorkey('white')
    small_cactus2 = pygame.image.load('imgs/small_cactus2.png')
    small_cactus2.set_colorkey('white')
    small_cactus3 = pygame.image.load('imgs/small_cactus3.png')
    small_cactus3.set_colorkey('white')
    small_cactus4 = pygame.image.load('imgs/small_cactus4.png')
    small_cactus4.set_colorkey('white')
    small_cactus5 = pygame.image.load('imgs/small_cactus5.png')
    small_cactus5.set_colorkey('white')
    fare_cactus = pygame.image.load('imgs/fare_cactus.png')
    fare_cactus.set_colorkey('white')
    watter_cactus = pygame.image.load('imgs/watter_cactus.png')
    watter_cactus.set_colorkey('white')
    cacti = [small_cactus1, small_cactus2, small_cactus3, small_cactus4, small_cactus5, fare_cactus, watter_cactus]
    all_cacti = pygame.sprite.Group()
    all_coin = pygame.sprite.Group()
    all_col = pygame.sprite.Group()
    fare_cacti = pygame.sprite.Group()
    watter_cacti = pygame.sprite.Group()

    asteroid = pygame.image.load('imgs/asteroid.png')
    asteroid = pygame.transform.scale(asteroid, (150, 67))
    asteroid = pygame.transform.rotate(asteroid, 45)
    asteroid = pygame.transform.flip(asteroid, True, False)
    asteroid.set_colorkey('white')
    asteroid_x = 100
    asteroid_y = -120
    f2 = pygame.font.SysFont('arial', 62)

    jump_sound = pygame.mixer.Sound('sounds/dino_jump_sound.mp3')
    score_1000_sound = pygame.mixer.Sound('sounds/dino_1000_sound.mp3')
    die_sound = pygame.mixer.Sound('sounds/dino_die_sound.mp3')

    small_water_img = pygame.image.load('imgs/watter_ball.png')
    small_water_img = pygame.transform.scale(small_water_img, (25, 17))
    small_water_img.set_colorkey('white')
    small_money_img = pygame.image.load('imgs/coin.png')
    small_money_img = pygame.transform.scale(small_money_img, (14, 18))
    small_money_img.set_colorkey('white')
    small_fire_img = pygame.image.load('imgs/fare_ball2.png')
    small_fire_img = pygame.transform.scale(small_fire_img, (25, 15))
    small_fire_img.set_colorkey('white')
    coin_img = pygame.image.load('imgs/coin.png')
    coin_img = pygame.transform.scale(coin_img, (30, 40))
    coin_img.set_colorkey('white')
    watter_ball_img = pygame.image.load('imgs/watter_ball.png')
    watter_ball_img = pygame.transform.scale(watter_ball_img, (45, 25))
    watter_ball_img.set_colorkey('white')
    fire_ball_img = pygame.image.load('imgs/fare_ball2.png')
    fire_ball_img = pygame.transform.scale(fire_ball_img, (45, 25))
    fire_ball_img.set_colorkey('white')
    fire_x = 35
    fire_y = 30
    water_x = 35
    water_y = 50
    money_x = 35
    money_y = 10
    coin_status = 0
    boss_die_t = 0
    clock = pygame.time.Clock()
    if birthday_code:
        dino1 = pygame.image.load('imgs/dino_bd_1.png')
        d_y = 178 + 200
        d_x = 100
    else:
        d_y = 210 + 200
        d_x = 100
        dino1 = pygame.image.load('imgs/dino1.png')
    dino1.set_colorkey('white')
    # d = Dino(d_x, d_y, birthday_code)
    dino_group = pygame.sprite.GroupSingle(d)
    birds = pygame.sprite.Group()
    status_dino = 'run'
    fire_status = False
    fire_cor_x = d.x + 89
    fire_cor_y = 200 + 200
    water_status = False
    water_cor_x = d.x + 89
    water_cor_y = 200 + 200
    moon_x = moon_list[0]
    star_x1 = moon_list[1]
    star_x2 = moon_list[2]
    star_x3 = moon_list[3]
    star_x4 = moon_list[4]
    star_x5 = moon_list[5]
    star_x6 = moon_list[6]
    star_x7 = moon_list[7]
    star_x8 = moon_list[8]
    star_x9 = moon_list[9]
    star_x10 = moon_list[10]
    sun_x = sun_list[0]
    cloud_x1 = sun_list[1]
    cloud_x2 = sun_list[2]
    cloud_x3 = sun_list[3]
    cloud_x4 = sun_list[4]
    cloud_x5 = sun_list[5]
    cloud_x6 = sun_list[6]
    cloud_x7 = sun_list[7]
    cloud_x8 = sun_list[8]
    cloud_x9 = sun_list[9]
    cloud_x10 = sun_list[10]
    # jump_status = 0
    road_cord_x1 = 0
    road_cord_x2 = 2398
    boss_die_status = 0
    road_v = 1.0
    road_speed = 10
    # num_s = ''
    score_t = 0
    stop_status = False
    stop_t = 1
    score_cord_y = 50
    rand_time = -30
    now_barier = 'cactus'
    next_barier = 'cactus'
    last_cactus = True
    score_str = str(score)
    # jump_time = 0
    time = -1
    HI_str = str(HI)
    HI_t = 0
    HI_coard_y = 500 + 200
    # fast_jump = 0
    bird_height = 2
    fire_strelba = False
    watter_strelba = False
    if score <= 2000:
        was_scene_1 = False
    else:
        was_scene_1 = True
        watter_strelba = True
    if score <= 4000:
        was_scene_2 = False
    else:
        was_scene_2 = True
        fire_strelba = True
    if score <= 6000:
        was_scene_3 = False
    else:
        was_scene_3 = True
    if score <= 8000:
        was_scene_4 = False
        boss_fight = False
    else:
        was_scene_4 = True
        boss_fight = True
        pygame.mixer.music.load('sounds/menu_sound_1.mp3')
        if not audio_turn_off:
            pygame.mixer.music.play(-1)

    b = Boss(600, 366)
    boss_group = pygame.sprite.GroupSingle(b)

    coin_sound = pygame.mixer.Sound('sounds/money_sound.mp3')

    save_score = score
    save_waterballs = water_number
    save_fireballs = fire_number
    save_money = money

    running = True
    while running:

        clock.tick(FPS)

        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений

        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                quit()  # running = False
            if boss_die_status == 0:
                if event.type == pygame.MOUSEBUTTONDOWN:  # обработка событий мыши
                    if event.button == 1 and not fire_status and fire_number and fire_strelba:
                        fire_number -= 1
                        fire_status = True
                        fire_cor_x = d.x + 89
                        fire_cor_y = d.y
                    if event.button == 3 and not water_status and water_number and watter_strelba:
                        water_number -= 1
                        water_status = True
                        water_cor_x = d.x + 89
                        water_cor_y = d.y
                    if status_dino == 'sit' and not fire_status:
                        fire_cor_y = d.y
                        fire_cor_x = d.x + 120
                    if status_dino == 'sit' and not water_status:
                        water_cor_y = d.y
                        water_cor_x = d.x + 120
                if event.type == pygame.KEYDOWN:  # обработка событий клавиатуры
                    if event.key == pygame.K_ESCAPE:
                        menu_exit = True
                        running = False
                    elif event.key == 113:  # q
                        audio_turn_off = sets(screen, score, language, keys, money, fire_number, water_number, True,
                                              audio_turn_off)
                    elif event.key == down_key:  # if event.unicode == 's':
                        status_dino = 'sit'
                        if not d.jump_status:
                            d.y = d_y + 34  # d.y += 34
                        if not d.jump_status:
                            d.sit_anim(screen)
                    elif event.key == up_key and status_dino != 'sit':  # elif event.unicode == 'w':
                        if d.jump_status == 0:  # and not stop_status:
                            d.jump_status = 1
                            jump_sound.play()
                    elif event.key == red_ball_key and not fire_status and fire_number and fire_strelba:
                        fire_number -= 1
                        fire_status = True
                        fire_cor_x = d.x + 89
                        fire_cor_y = d.y
                        if status_dino == 'sit':
                            fire_cor_y = d.y
                            fire_cor_x = d.x + 120
                    elif event.key == blue_ball_key and not water_status and water_number and watter_strelba:
                        water_number -= 1
                        water_status = True
                        water_cor_x = d.x + 89
                        water_cor_y = d.y
                        if status_dino == 'sit':
                            water_cor_y = d.y
                            water_cor_x = d.x + 120
                if event.type == pygame.KEYUP:
                    if event.key == down_key:  # if event.unicode == 's':
                        status_dino = 'run'
                        d.y = d_y  # d.y -= 34
                        if not d.jump_status and boss_die_status == 0:
                            d.run_anim(screen)

        time += 1
        if time % 10 == 0:
            screen.fill(color)
            if d.jump_status == 0 and status_dino == 'run' and boss_die_status == 0:
                d.run_anim(screen)
            elif d.jump_status == 0 and status_dino == 'sit' and boss_die_status == 0:
                d.sit_anim(screen)
            elif d.jump_status != 0 and status_dino == 'sit':
                pass
                # if d.y <= 180:
                #    d.y += 20
                # else:
                #    d.y = 200
                #    jump_status = 0

        # прыжок:
        d.jump(screen, status_dino, dino1, boss_die_status, d_y)

        if not stop_status:
            if (time % (70 + rand_time) == 0 and next_barier == 'cactus' and last_cactus) or (
                    next_barier == 'cactus' and not last_cactus):
                # добавляет кактус и определяет время через которе появится следующее препятсвие
                last_cactus = True
                Cactus(WIDTH, 426, cacti[randint(0, 4)], all_cacti)
                now_barier = 'cactus'
                time = time % 10
                rand_time = randint(-10, 40)  # TODO сделать нормальное время между появлениями кактусов(препятсвий)
            elif (time % (70 + rand_time) == 0 and next_barier == 'bird' and last_cactus) or (
                    next_barier == 'bird' and not last_cactus):
                # добавляет птицу; после птицы следующее препятсвие появляется только когда сама птица умирает
                last_cactus = False
                bird_height = randint(1, 3)
                if bird_height == 1:
                    Bird(WIDTH, 290, birds)
                elif bird_height == 2:
                    if birthday_code:
                        Bird(WIDTH, 320, birds)
                    else:
                        Bird(WIDTH, 350, birds)
                elif bird_height == 3:
                    Bird(WIDTH, 410, birds)
                now_barier = 'bird'
                next_barier = ''
            elif (time % (70 + rand_time) == 0 and next_barier == 'fare_cactus' and last_cactus) or (
                    next_barier == 'fare_cactus' and not last_cactus):
                # добавляет кактус и определяет время через которе появится следующее препятсвие
                last_cactus = True
                Cactus(WIDTH, 335, cacti[5], fare_cacti)
                now_barier = 'fare_cactus'
                time = time % 10
                rand_time = randint(-10, 40)  # TODO сделать нормальное время между появлениями кактусов(препятсвий)
            elif (time % (70 + rand_time) == 0 and next_barier == 'watter_cactus' and last_cactus) or (
                    next_barier == 'watter_cactus' and not last_cactus):
                # добавляет кактус и определяет время через которе появится следующее препятсвие
                last_cactus = True
                Cactus(WIDTH, 335, cacti[6], watter_cacti)
                now_barier = 'watter_cactus'
                time = time % 10
                rand_time = randint(-10, 40)  # TODO сделать нормальное время между появлениями кактусов(препятсвий)
            elif (time % (70 + rand_time) == 0 and next_barier == 'coin' and last_cactus) or (
                    next_barier == 'coin' and not last_cactus):
                # добавляет кактус и определяет время через которе появится следующее препятсвие
                last_cactus = True
                rand_col = randint(1, 4)
                if boss_fight:
                    if rand_col == 1 or rand_col == 2:
                        Col_fire_water(WIDTH, 320, fire_ball_img, 'fire', all_col)
                    else:
                        Col_fire_water(WIDTH, 320, watter_ball_img, 'water', all_col)
                else:
                    if rand_col == 1:
                        Col_fire_water(WIDTH, 320, fire_ball_img, 'fire', all_col)
                    elif rand_col == 2:
                        Col_fire_water(WIDTH, 320, watter_ball_img, 'water', all_col)
                    else:
                        Coin(WIDTH, 350, coin_img, all_coin)
                now_barier = 'coin'
                time = time % 10
                rand_time = randint(-10, 40)
                next_barier = 'cactus'
        elif not all_cacti.spritedict and not birds.spritedict \
                and not fare_cacti.spritedict and not watter_cacti.spritedict and not all_coin and d.jump_status == 0:
            # проверка остались ли еще препятсвия
            stop_status = True
            if stop_t % 50 == 0:
                if not was_scene_1:
                    was_scene_1 = True
                    moon_list, sun_list = cut_scen_1(screen, color, score, HI, road_cord_x1, birthday_code, language,
                                                     keys, water_number, fire_number, money, road_speed, road_v,
                                                     moon_list, sun_list)
                    moon_x = moon_list[0]
                    star_x1 = moon_list[1]
                    star_x2 = moon_list[2]
                    star_x3 = moon_list[3]
                    star_x4 = moon_list[4]
                    star_x5 = moon_list[5]
                    star_x6 = moon_list[6]
                    star_x7 = moon_list[7]
                    star_x8 = moon_list[8]
                    star_x9 = moon_list[9]
                    star_x10 = moon_list[10]
                    sun_x = sun_list[0]
                    cloud_x1 = sun_list[1]
                    cloud_x2 = sun_list[2]
                    cloud_x3 = sun_list[3]
                    cloud_x4 = sun_list[4]
                    cloud_x5 = sun_list[5]
                    cloud_x6 = sun_list[6]
                    cloud_x7 = sun_list[7]
                    cloud_x8 = sun_list[8]
                    cloud_x9 = sun_list[9]
                    cloud_x10 = sun_list[10]
                    stop_status = False
                    road_v = 1.0
                    score_t = 0
                    all_cacti = pygame.sprite.Group()
                    fare_cacti = pygame.sprite.Group()
                    watter_cacti = pygame.sprite.Group()
                    all_coin = pygame.sprite.Group()
                    all_col = pygame.sprite.Group()
                    watter_strelba = True
                    save_score = 2001
                    save_waterballs = water_number
                    save_fireballs = fire_number
                    save_money = money
                elif not was_scene_2 and was_scene_1:
                    was_scene_2 = True
                    moon_list, sun_list = cut_scen_2(screen, color, score, HI, road_cord_x1, birthday_code, language,
                                                     keys, water_number, fire_number, money, road_speed, road_v,
                                                     moon_list, sun_list)
                    moon_x = moon_list[0]
                    star_x1 = moon_list[1]
                    star_x2 = moon_list[2]
                    star_x3 = moon_list[3]
                    star_x4 = moon_list[4]
                    star_x5 = moon_list[5]
                    star_x6 = moon_list[6]
                    star_x7 = moon_list[7]
                    star_x8 = moon_list[8]
                    star_x9 = moon_list[9]
                    star_x10 = moon_list[10]
                    sun_x = sun_list[0]
                    cloud_x1 = sun_list[1]
                    cloud_x2 = sun_list[2]
                    cloud_x3 = sun_list[3]
                    cloud_x4 = sun_list[4]
                    cloud_x5 = sun_list[5]
                    cloud_x6 = sun_list[6]
                    cloud_x7 = sun_list[7]
                    cloud_x8 = sun_list[8]
                    cloud_x9 = sun_list[9]
                    cloud_x10 = sun_list[10]
                    stop_status = False
                    road_v = 1.0
                    score_t = 0
                    all_cacti = pygame.sprite.Group()
                    fare_cacti = pygame.sprite.Group()
                    watter_cacti = pygame.sprite.Group()
                    all_coin = pygame.sprite.Group()
                    all_col = pygame.sprite.Group()
                    fire_strelba = True
                    save_score = 4001
                    save_waterballs = water_number
                    save_fireballs = fire_number
                    save_money = money
                elif not was_scene_3 and was_scene_1 and was_scene_2:
                    was_scene_3 = True
                    money, fire_number, water_number, \
                    moon_list, sun_list = cut_scen_3(screen, color, score, HI, road_cord_x1, birthday_code, language,
                                                     keys, water_number, fire_number, money, road_speed, road_v,
                                                     moon_list, sun_list)
                    moon_x = moon_list[0]
                    star_x1 = moon_list[1]
                    star_x2 = moon_list[2]
                    star_x3 = moon_list[3]
                    star_x4 = moon_list[4]
                    star_x5 = moon_list[5]
                    star_x6 = moon_list[6]
                    star_x7 = moon_list[7]
                    star_x8 = moon_list[8]
                    star_x9 = moon_list[9]
                    star_x10 = moon_list[10]
                    sun_x = sun_list[0]
                    cloud_x1 = sun_list[1]
                    cloud_x2 = sun_list[2]
                    cloud_x3 = sun_list[3]
                    cloud_x4 = sun_list[4]
                    cloud_x5 = sun_list[5]
                    cloud_x6 = sun_list[6]
                    cloud_x7 = sun_list[7]
                    cloud_x8 = sun_list[8]
                    cloud_x9 = sun_list[9]
                    cloud_x10 = sun_list[10]
                    stop_status = False
                    road_v = 1.0
                    score_t = 0
                    all_cacti = pygame.sprite.Group()
                    fare_cacti = pygame.sprite.Group()
                    watter_cacti = pygame.sprite.Group()
                    all_coin = pygame.sprite.Group()
                    all_col = pygame.sprite.Group()
                    save_score = 6001
                    save_waterballs = water_number
                    save_fireballs = fire_number
                    save_money = money
                elif not was_scene_4 and was_scene_1 and was_scene_2 and was_scene_3:
                    was_scene_4 = True
                    moon_list, sun_list = cut_scen_4(screen, color, score, HI, road_cord_x1, birthday_code, language,
                                                     keys, water_number, fire_number, money, road_speed, road_v,
                                                     moon_list, sun_list)
                    moon_x = moon_list[0]
                    star_x1 = moon_list[1]
                    star_x2 = moon_list[2]
                    star_x3 = moon_list[3]
                    star_x4 = moon_list[4]
                    star_x5 = moon_list[5]
                    star_x6 = moon_list[6]
                    star_x7 = moon_list[7]
                    star_x8 = moon_list[8]
                    star_x9 = moon_list[9]
                    star_x10 = moon_list[10]
                    sun_x = sun_list[0]
                    cloud_x1 = sun_list[1]
                    cloud_x2 = sun_list[2]
                    cloud_x3 = sun_list[3]
                    cloud_x4 = sun_list[4]
                    cloud_x5 = sun_list[5]
                    cloud_x6 = sun_list[6]
                    cloud_x7 = sun_list[7]
                    cloud_x8 = sun_list[8]
                    cloud_x9 = sun_list[9]
                    cloud_x10 = sun_list[10]
                    stop_status = False
                    road_v = 1.0
                    score_t = 0
                    all_cacti = pygame.sprite.Group()
                    fare_cacti = pygame.sprite.Group()
                    watter_cacti = pygame.sprite.Group()
                    all_coin = pygame.sprite.Group()
                    all_col = pygame.sprite.Group()
                    boss_fight = True
                    save_score = 8001
                    save_waterballs = water_number
                    save_fireballs = fire_number
                    save_money = money
                    pygame.mixer.music.load('sounds/menu_sound_1.mp3')
                    if not audio_turn_off:
                        pygame.mixer.music.play(-1)
            else:
                stop_t += 1

        screen.fill(color)

        # статичные объекты:
        if color == (0, 0, 0):
            screen.blit(moon, (moon_x, 80))
            screen.blit(star, (star_x1, 125))
            screen.blit(star, (star_x2, 150))
            screen.blit(star, (star_x3, 140))
            screen.blit(star, (star_x4, 110))
            screen.blit(star, (star_x5, 140))
            screen.blit(star, (star_x6, 137))
            screen.blit(star, (star_x7, 135))
            screen.blit(star, (star_x8, 133))
            screen.blit(star, (star_x9, 122))
            screen.blit(star, (star_x10, 147))
        else:
            screen.blit(cloud, (cloud_x1, 123))
            screen.blit(cloud, (cloud_x2, 200))
            screen.blit(cloud, (cloud_x3, 216))
            screen.blit(cloud, (cloud_x4, 147))
            screen.blit(cloud, (cloud_x5, 111))
            screen.blit(cloud, (cloud_x6, 50))
            screen.blit(cloud, (cloud_x7, 91))
            screen.blit(cloud, (cloud_x8, 131))
            screen.blit(cloud, (cloud_x9, 115))
            screen.blit(cloud, (cloud_x10, 100))
            screen.blit(night_sun, (sun_x, 100))

        if boss_die_status == 0:
            moon_x -= 1
            star_x1 -= 1
            star_x2 -= 1
            star_x3 -= 1
            star_x4 -= 1
            star_x5 -= 1
            star_x6 -= 1
            star_x7 -= 1
            star_x8 -= 1
            star_x9 -= 1
            star_x10 -= 1
            cloud_x1 -= 1
            cloud_x2 -= 1
            cloud_x3 -= 1
            cloud_x4 -= 1
            cloud_x5 -= 1
            cloud_x6 -= 1
            cloud_x7 -= 1
            cloud_x8 -= 1
            cloud_x9 -= 1
            cloud_x10 -= 1
            sun_x -= 1
        if star_x1 <= -40:
            star_x1 = 1200
        if star_x2 <= -40:
            star_x2 = 1200
        if star_x3 <= -40:
            star_x3 = 1200
        if star_x4 <= -40:
            star_x4 = 1200
        if star_x5 <= -40:
            star_x5 = 1200
        if star_x6 <= -40:
            star_x6 = 1200
        if star_x7 <= -40:
            star_x7 = 1200
        if star_x8 <= -40:
            star_x8 = 1200
        if star_x9 <= -40:
            star_x9 = 1200
        if star_x10 <= -40:
            star_x10 = 1200
        if sun_x <= - 100:
            sun_x = 1200
        if cloud_x1 <= - 115:
            cloud_x1 = 1200
        if cloud_x2 <= - 115:
            cloud_x2 = 1200
        if cloud_x3 <= - 115:
            cloud_x3 = 1200
        if cloud_x4 <= - 115:
            cloud_x4 = 1200
        if cloud_x5 <= - 115:
            cloud_x5 = 1200
        if cloud_x6 <= - 115:
            cloud_x6 = 1200
        if cloud_x7 <= - 115:
            cloud_x7 = 1200
        if cloud_x8 <= - 115:
            cloud_x8 = 1200
        if cloud_x9 <= - 115:
            cloud_x9 = 1200
        if cloud_x10 <= - 115:
            cloud_x10 = 1200
        if moon_x <= -40:
            moon_x = 1200

        moon_list = [moon_x, star_x1, star_x2, star_x3, star_x4, star_x5, star_x6, star_x7, star_x8, star_x9, star_x10]
        sun_list = [cloud_x1, cloud_x2, cloud_x3, cloud_x4, cloud_x5, cloud_x6, cloud_x7, cloud_x8, cloud_x9, cloud_x10,
                    sun_x]

        # Проверка столкновений дино с кактусами и птицами:
        q1 = d.collide_check(all_cacti)
        q2 = d.collide_check(birds)
        q3 = d.collide_check(fare_cacti)
        q4 = d.collide_check(watter_cacti)
        if q1 or q2 or q3 or q4:  # смерть
            pygame.mixer.music.stop()
            die_sound.play()
            d.die(score)
            if status_dino == 'sit':
                d.x, d.y = d_x, d_y
            road_v = 0
            running = False

        # screen.blit(d.image, (d.x, d.y))
        d.update(screen)

        if score > 2000:
            for cactus in all_cacti:
                if cactus.rect.x <= -1 * cactus.rect.width:  # только если маленький кактус
                    cactus.kill()  # удаляет спрайт, если он оказался за пределами экрана
            for cactus in fare_cacti:
                if cactus.rect.x < -1 * cactus.rect.width:  # только если маленький кактус
                    cactus.kill()  # удаляет спрайт, если он оказался за пределами экрана
            for cactus in watter_cacti:
                if cactus.rect.x < -1 * cactus.rect.width:  # только если маленький кактус
                    cactus.kill()  # удаляет спрайт, если он оказался за пределами экрана
            for bird in birds:
                if bird.rect.x < -94:
                    bird.kill()  # удаляет спрайт, если он оказался за пределами экрана
            for coin in all_coin:
                if coin.rect.x < -30:
                    coin.kill()
            for col in all_col:
                if col.rect.x < -30:
                    col.kill()

        # кактусы:
        all_cacti.update(road_v * road_speed)
        all_cacti.draw(screen)
        if now_barier == 'cactus':
            for cactus in all_cacti:
                if cactus.rect.x <= -1 * cactus.rect.width:  # только если маленький кактус
                    cactus.kill()  # удаляет спрайт, если он оказался за пределами экрана
                    if score > 50:
                        if not boss_fight:
                            choose = randint(1, 7)  # определяет какое препятсвие будет следующим
                            if choose == 4:
                                next_barier = 'bird'
                            elif choose == 5:
                                if water_number != 0 and watter_strelba:
                                    next_barier = 'fare_cactus'
                                else:
                                    next_barier = 'cactus'
                            elif choose == 6:
                                if fire_number != 0 and fire_strelba:
                                    next_barier = 'watter_cactus'
                                else:
                                    next_barier = 'cactus'
                            elif choose == 7:
                                next_barier = 'coin'
                            else:
                                next_barier = 'cactus'
                        else:
                            choose = randint(1, 6)  # определяет какое препятсвие будет следующим
                            if choose == 4:
                                next_barier = 'bird'
                            elif choose == 6:
                                next_barier = 'coin'
                            else:
                                next_barier = 'cactus'
                if boss_fight:
                    if b.rect.x + b.rect.w < cactus.rect.x <= b.rect.w + 40 + int(road_v * 10) + b.rect.x:
                        b.jump_status = 1

        fare_cacti.update(road_v * road_speed)
        fare_cacti.draw(screen)
        if now_barier == 'fare_cactus':
            for cactus in fare_cacti:
                if cactus.rect.x < -1 * cactus.rect.width:  # только если маленький кактус
                    cactus.kill()  # удаляет спрайт, если он оказался за пределами экрана
                    if score > 50:
                        if not boss_fight:
                            choose = randint(1, 7)  # определяет какое препятсвие будет следующим
                            if choose == 4:
                                next_barier = 'bird'
                            elif choose == 5:
                                if water_number != 0 and watter_strelba:
                                    next_barier = 'fare_cactus'
                                else:
                                    next_barier = 'cactus'
                            elif choose == 6:
                                if fire_number != 0 and fire_strelba:
                                    next_barier = 'watter_cactus'
                                else:
                                    next_barier = 'cactus'
                            elif choose == 7:
                                next_barier = 'coin'
                            else:
                                next_barier = 'cactus'
                        else:
                            choose = randint(1, 6)  # определяет какое препятсвие будет следующим
                            if choose == 4:
                                next_barier = 'bird'
                            elif choose == 6:
                                next_barier = 'coin'
                            else:
                                next_barier = 'cactus'

        watter_cacti.update(road_v * road_speed)
        watter_cacti.draw(screen)
        if now_barier == 'watter_cactus':
            for cactus in watter_cacti:
                if cactus.rect.x < -1 * cactus.rect.width:  # только если маленький кактус
                    cactus.kill()  # удаляет спрайт, если он оказался за пределами экрана
                    if score > 50:
                        if not boss_fight:
                            choose = randint(1, 7)  # определяет какое препятсвие будет следующим
                            if choose == 4:
                                next_barier = 'bird'
                            elif choose == 5:
                                if water_number != 0 and watter_strelba:
                                    next_barier = 'fare_cactus'
                                else:
                                    next_barier = 'cactus'
                            elif choose == 6:
                                if fire_number != 0 and fire_strelba:
                                    next_barier = 'watter_cactus'
                                else:
                                    next_barier = 'cactus'
                            elif choose == 7:
                                next_barier = 'coin'
                            else:
                                next_barier = 'cactus'
                        else:
                            choose = randint(1, 6)  # определяет какое препятсвие будет следующим
                            if choose == 4:
                                next_barier = 'bird'
                            elif choose == 6:
                                next_barier = 'coin'
                            else:
                                next_barier = 'cactus'

        # птицы:
        if boss_die_status == 0:
            birds.update(road_v * road_speed, time)
            birds.draw(screen)
            if now_barier == 'bird':

                for bird in birds:
                    if bird.rect.x < -94:
                        bird.kill()  # удаляет спрайт, если он оказался за пределами экрана
                    if b.rect.x + b.rect.w < bird.rect.x <= b.rect.w + 40 + int(
                            road_v * 10) + b.rect.x and bird.rect.y == 410:
                        b.jump_status = 1
                if not birds.spritedict:
                    if not boss_fight:
                        choose = randint(1, 7)  # определяет какое препятсвие будет следующим
                        if choose == 4:
                            next_barier = 'bird'
                        elif choose == 5:
                            if water_number != 0 and watter_strelba:
                                next_barier = 'fare_cactus'
                            else:
                                next_barier = 'cactus'
                        elif choose == 6:
                            if fire_number != 0 and fire_strelba:
                                next_barier = 'watter_cactus'
                            else:
                                next_barier = 'cactus'
                        elif choose == 7:
                            next_barier = 'coin'
                        else:
                            next_barier = 'cactus'
                    else:
                        choose = randint(1, 6)  # определяет какое препятсвие будет следующим
                        if choose == 4:
                            next_barier = 'bird'
                        elif choose == 6:
                            next_barier = 'coin'
                        else:
                            next_barier = 'cactus'

        all_coin.update(road_v * road_speed)
        all_coin.draw(screen)
        for coin in all_coin:
            if coin.collide_check(dino_group):
                coin_sound.play()
                money += 20
                coin.kill()

        all_col.update(road_v * road_speed)
        all_col.draw(screen)
        for col in all_col:
            if col.collide_check(dino_group):
                if col.type == 'fire':
                    fire_number += 10
                elif col.type == 'water':
                    water_number += 10
                col.kill()

        # преобразует текущий счет в поверхность и выводит ее:
        score_out = []
        for i in range(1, len(score_str) + 1):
            score_out.insert(0, score_str[len(score_str) - i])
        while len(score_out) != 5:
            score_out.insert(0, '0')
        score_cord_x = 970
        for i in range(len(score_out)):
            screen.blit(nums_dict[score_out[i]], (score_cord_x, score_cord_y))
            score_cord_x += 30

        # преобразует лучший счет в поверхность и выводит ее:
        score_out = []
        screen.blit(HI_img, (870, 700))
        for i in range(1, len(HI_str) + 1):
            score_out.insert(0, HI_str[len(HI_str) - i])
        while len(score_out) != 5:
            score_out.insert(0, '0')
        HI_coard_x = 970
        for i in range(len(score_out)):
            screen.blit(nums_dict[score_out[i]], (HI_coard_x, HI_coard_y))
            HI_coard_x += 30

        # считает очки:
        if score_t % 3 == 0 and stop_status == False and boss_die_status == 0:
            score += 1
            score_str = str(score)
        score_t += 1

        # двигает дорожку:
        screen.blit(road1, (road_cord_x1, 475))
        screen.blit(road2, (road_cord_x2, 475))
        if boss_die_status == 0:
            if road_cord_x2 <= 0:
                road_cord_x1 = 0
                road_cord_x2 = 2398
            else:
                road_cord_x1 -= int(road_speed * road_v)
                road_cord_x2 -= int(road_speed * road_v)
            if road_v < 1.9:
                road_v += 0.00016

        if boss_fight:
            boss_group.update()
            boss_group.draw(screen)
            bq1 = b.collide_check(all_cacti)
            bq2 = b.collide_check(d.fare_ball_sprites)
            bq3 = b.collide_check(d.watter_ball_sprites)
            if bq2:
                b.hp -= 10
                for ball in d.fare_ball_sprites:
                    ball.kill()
                fire_status = False
            if bq3:
                b.hp -= 10
                # print(b.hp)
                for ball in d.watter_ball_sprites:
                    ball.kill()
                water_status = False
            if b.hp <= 0 and d.jump_status == 0:
                if boss_die_status == 0:
                    boss_die_t = 1
                    boss_die_status = 1
                    road_speed = 0
                b.jump_status = 1
                boss_die_t += 1
                # b.die(boss_die_t)
                for boss in boss_group:
                    if boss.y > HEIGHT:
                        boss.kill()

        if boss_die_status == 1:
            if 0 < boss_die_t <= 300:
                text = f2.render("You win.", False, (83, 83, 83))
                screen.blit(text, (400, 250))
            elif 300 < boss_die_t < 330:
                asteroid_x += 15
                asteroid_y += 25
                screen.blit(asteroid, (asteroid_x, asteroid_y))

        # полет огенного шара:
        if fire_status:
            d.fare_ball_anim(screen, fire_cor_x, fire_cor_y, color_must)
            fire_cor_x += 10
        if fire_cor_x > WIDTH:
            fire_cor_x = d.x + 89
            fire_status = False

        # полет водяного шара:
        if water_status:
            d.watter_ball_anim(screen, water_cor_x, water_cor_y, color_must)
            water_cor_x += 10
        if water_cor_x > WIDTH:
            water_cor_x = d.x + 89
            water_status = False

        if fire_status:
            fare = pygame.sprite.groupcollide(d.fare_ball_sprites, watter_cacti, True, True)
            if fare:
                if not boss_fight:
                    choose = randint(1, 6)  # определяет какое препятсвие будет следующим
                    if choose == 4:
                        next_barier = 'bird'
                    elif choose == 5:
                        if water_number != 0 and watter_strelba:
                            next_barier = 'fare_cactus'
                        else:
                            next_barier = 'cactus'
                    elif choose == 6:
                        if fire_number != 0 and fire_strelba:
                            next_barier = 'watter_cactus'
                        else:
                            next_barier = 'cactus'
                    else:
                        next_barier = 'cactus'
                else:
                    choose = randint(1, 4)  # определяет какое препятсвие будет следующим
                    if choose == 4:
                        next_barier = 'bird'
                    else:
                        next_barier = 'cactus'
                fire_status = False

        if water_status:
            watter = pygame.sprite.groupcollide(d.watter_ball_sprites, fare_cacti, True, True)
            if watter:
                if not boss_fight:
                    choose = randint(1, 6)  # определяет какое препятсвие будет следующим
                    if choose == 4:
                        next_barier = 'bird'
                    elif choose == 5:
                        if water_number != 0 and watter_strelba:
                            next_barier = 'fare_cactus'
                        else:
                            next_barier = 'cactus'
                    elif choose == 6:
                        if fire_number != 0 and fire_strelba:
                            next_barier = 'watter_cactus'
                        else:
                            next_barier = 'cactus'
                    else:
                        next_barier = 'cactus'
                else:
                    choose = randint(1, 4)  # определяет какое препятсвие будет следующим
                    if choose == 4:
                        next_barier = 'bird'
                    else:
                        next_barier = 'cactus'
                water_status = False

        screen.blit(small_fire_img, (10, 30))
        for i in range(len(str(fire_number))):
            num_fire_surf = pygame.transform.scale(nums_dict[str(fire_number)[i]], (15, 18))
            screen.blit(num_fire_surf, (fire_x + num_fire_surf.get_width() * i, fire_y))
        screen.blit(small_water_img, (10, 50))
        for i in range(len(str(water_number))):
            num_water_surf = pygame.transform.scale(nums_dict[str(water_number)[i]], (15, 18))
            screen.blit(num_water_surf, (water_x + num_water_surf.get_width() * i, water_y))
        screen.blit(small_money_img, (17, 10))
        for i in range(len(str(money))):
            money_surf = pygame.transform.scale(nums_dict[str(money)[i]], (15, 18))
            screen.blit(money_surf, (money_x + money_surf.get_width() * i, money_y))

        if boss_fight:
            pygame.draw.rect(screen, 'black', (100, 600, 230, 70), 3)
            pygame.draw.rect(screen, 'red', (105, 605, 40, 60))
            if b.hp > 40:
                pygame.draw.rect(screen, 'red', (150, 605, 40, 60))
            if b.hp > 80:
                pygame.draw.rect(screen, 'red', (195, 605, 40, 60))
            if b.hp > 120:
                pygame.draw.rect(screen, 'red', (240, 605, 40, 60))
            if b.hp > 160:
                pygame.draw.rect(screen, 'red', (285, 605, 40, 60))

            x_print = 340
            if b.hp < 0:
                b.hp = 0
            for i in range(len(str(b.hp))):
                screen.blit(nums_dict[str(b.hp)[i]], (x_print, 618))
                x_print += 30

        if color != color_must:
            if color_must == (255, 255, 255):
                color_rgb += 5
                color = (color_rgb, color_rgb, color_rgb)
            elif color_must == (0, 0, 0):
                color_rgb -= 5
                color = (color_rgb, color_rgb, color_rgb)

        if score == 1000:
            color_must = (0, 0, 0)
        elif score == 1600:
            color_must = (255, 255, 255)
        elif score == 2600:
            color_must = (0, 0, 0)
        elif score == 3400:
            color_must = (255, 255, 255)
        elif score == 4400:
            color_must = (0, 0, 0)
        elif score == 5000:
            color_must = (255, 255, 255)
        elif score == 6200:
            color_must = (0, 0, 0)
        elif score == 6800:
            color_must = (255, 255, 255)

        if score % 1000 == 0 and score:
            score_1000_sound.play()

        if score > 2000 and not was_scene_1:
            stop_status = True
        elif score > 4000 and not was_scene_2:
            stop_status = True
        elif score > 6000 and not was_scene_3:
            stop_status = True
        elif score > 8000 and not was_scene_4:
            stop_status = True
        # отрисовка и изменение свойств объектов
        # ...

        if boss_die_t > 330:
            screen.fill('black')
            running = False
        # обновление экрана
        pygame.display.flip()

    return save_score, save_waterballs, save_fireballs, save_money, audio_turn_off


def infinity_dino(screen, color, score, HI, birthday_code, language, keys, water_number, fire_number, d,
                  moon_list, sun_list, audio_turn_off):
    global menu_exit
    menu_exit = False
    if not pygame.mixer.music.get_busy() and not audio_turn_off:
        pygame.mixer.music.play(-1)
    up_key = keys[0]
    down_key = keys[1]
    blue_ball_key = keys[2]
    red_ball_key = keys[3]

    money = 0

    color_must = color
    color_rgb = 255
    pygame.init()
    road1 = pygame.image.load('imgs/road.png')
    road1.set_colorkey('white')
    road2 = pygame.image.load('imgs/road.png')
    road2.set_colorkey('white')
    cloud = pygame.image.load('imgs/cloud.png')
    cloud.set_colorkey('white')
    night_sun = pygame.image.load('imgs/night_sun.png')
    night_sun.set_colorkey('black')
    moon = pygame.image.load('imgs/moon.png')
    moon.set_colorkey('black')
    star = pygame.image.load('imgs/star.png')
    star.set_colorkey('black')
    num_0 = pygame.image.load('imgs/0.png')
    num_0.set_colorkey('white')
    num_1 = pygame.image.load('imgs/1.png')
    num_1.set_colorkey('white')
    num_2 = pygame.image.load('imgs/2.png')
    num_2.set_colorkey('white')
    num_3 = pygame.image.load('imgs/3.png')
    num_3.set_colorkey('white')
    num_4 = pygame.image.load('imgs/4.png')
    num_4.set_colorkey('white')
    num_5 = pygame.image.load('imgs/5.png')
    num_5.set_colorkey('white')
    num_6 = pygame.image.load('imgs/6.png')
    num_6.set_colorkey('white')
    num_7 = pygame.image.load('imgs/7.png')
    num_7.set_colorkey('white')
    num_8 = pygame.image.load('imgs/8.png')
    num_8.set_colorkey('white')
    num_9 = pygame.image.load('imgs/9.png')
    num_9.set_colorkey('white')
    nums_dict = {
        '0': num_0,
        '1': num_1,
        '2': num_2,
        '3': num_3,
        '4': num_4,
        '5': num_5,
        '6': num_6,
        '7': num_7,
        '8': num_8,
        '9': num_9
    }

    HI_img = pygame.image.load('imgs/HI.png')
    HI_img.set_colorkey('white')

    small_cactus1 = pygame.image.load('imgs/small_cactus1.png')
    small_cactus1.set_colorkey('white')
    small_cactus2 = pygame.image.load('imgs/small_cactus2.png')
    small_cactus2.set_colorkey('white')
    small_cactus3 = pygame.image.load('imgs/small_cactus3.png')
    small_cactus3.set_colorkey('white')
    small_cactus4 = pygame.image.load('imgs/small_cactus4.png')
    small_cactus4.set_colorkey('white')
    small_cactus5 = pygame.image.load('imgs/small_cactus5.png')
    small_cactus5.set_colorkey('white')
    fare_cactus = pygame.image.load('imgs/fare_cactus.png')
    fare_cactus.set_colorkey('white')
    watter_cactus = pygame.image.load('imgs/watter_cactus.png')
    watter_cactus.set_colorkey('white')
    cacti = [small_cactus1, small_cactus2, small_cactus3, small_cactus4, small_cactus5, fare_cactus, watter_cactus]
    all_cacti = pygame.sprite.Group()
    all_coin = pygame.sprite.Group()
    all_col = pygame.sprite.Group()
    fare_cacti = pygame.sprite.Group()
    watter_cacti = pygame.sprite.Group()

    jump_sound = pygame.mixer.Sound('sounds/dino_jump_sound.mp3')
    score_1000_sound = pygame.mixer.Sound('sounds/dino_1000_sound.mp3')
    die_sound = pygame.mixer.Sound('sounds/dino_die_sound.mp3')

    small_water_img = pygame.image.load('imgs/watter_ball.png')
    small_water_img = pygame.transform.scale(small_water_img, (25, 17))
    small_water_img.set_colorkey('white')
    small_fire_img = pygame.image.load('imgs/fare_ball2.png')
    small_fire_img = pygame.transform.scale(small_fire_img, (25, 15))
    small_fire_img.set_colorkey('white')
    coin_img = pygame.image.load('imgs/coin.png')
    coin_img = pygame.transform.scale(coin_img, (30, 40))
    coin_img.set_colorkey('white')
    watter_ball_img = pygame.image.load('imgs/watter_ball.png')
    watter_ball_img = pygame.transform.scale(watter_ball_img, (45, 25))
    watter_ball_img.set_colorkey('white')
    fire_ball_img = pygame.image.load('imgs/fare_ball2.png')
    fire_ball_img = pygame.transform.scale(fire_ball_img, (45, 25))
    fire_ball_img.set_colorkey('white')
    fire_x = 35
    fire_y = 10
    water_x = 35
    water_y = 30
    coin_status = 0
    boss_die_t = 0
    clock = pygame.time.Clock()
    if birthday_code:
        dino1 = pygame.image.load('imgs/dino_bd_1.png')
        d_y = 178 + 200
        d_x = 100
    else:
        d_y = 210 + 200
        d_x = 100
        dino1 = pygame.image.load('imgs/dino1.png')
    dino1.set_colorkey('white')
    # d = Dino(d_x, d_y, birthday_code)
    dino_group = pygame.sprite.GroupSingle(d)
    birds = pygame.sprite.Group()
    status_dino = 'run'
    fire_status = False
    fire_cor_x = d.x + 89
    fire_cor_y = 200 + 200
    water_status = False
    water_cor_x = d.x + 89
    water_cor_y = 200 + 200
    moon_x = moon_list[0]
    star_x1 = moon_list[1]
    star_x2 = moon_list[2]
    star_x3 = moon_list[3]
    star_x4 = moon_list[4]
    star_x5 = moon_list[5]
    star_x6 = moon_list[6]
    star_x7 = moon_list[7]
    star_x8 = moon_list[8]
    star_x9 = moon_list[9]
    star_x10 = moon_list[10]
    sun_x = sun_list[0]
    cloud_x1 = sun_list[1]
    cloud_x2 = sun_list[2]
    cloud_x3 = sun_list[3]
    cloud_x4 = sun_list[4]
    cloud_x5 = sun_list[5]
    cloud_x6 = sun_list[6]
    cloud_x7 = sun_list[7]
    cloud_x8 = sun_list[8]
    cloud_x9 = sun_list[9]
    cloud_x10 = sun_list[10]
    road_cord_x1 = 0
    road_cord_x2 = 2398
    boss_die_status = 0
    road_v = 1.0
    road_speed = 10
    score_t = 0
    score_cord_y = 50
    rand_time = -30
    now_barier = 'cactus'
    next_barier = 'cactus'
    last_cactus = True
    score_str = str(score)
    time = -1
    HI_str = str(HI)
    HI_t = 0
    HI_coard_y = 500 + 200
    fire_strelba = True
    watter_strelba = True

    running = True
    while running:

        clock.tick(FPS)

        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений

        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                quit()  # running = False
            if event.type == pygame.MOUSEBUTTONDOWN:  # обработка событий мыши
                if event.button == 1 and not fire_status and fire_number and fire_strelba:
                    fire_number -= 1
                    fire_status = True
                    fire_cor_x = d.x + 89
                    fire_cor_y = d.y
                if event.button == 3 and not water_status and water_number and watter_strelba:
                    water_number -= 1
                    water_status = True
                    water_cor_x = d.x + 89
                    water_cor_y = d.y
                if status_dino == 'sit' and not fire_status:
                    fire_cor_y = d.y
                    fire_cor_x = d.x + 120
                if status_dino == 'sit' and not water_status:
                    water_cor_y = d.y
                    water_cor_x = d.x + 120
            if event.type == pygame.KEYDOWN:  # обработка событий клавиатуры
                if event.key == pygame.K_ESCAPE:
                    menu_exit = True
                    running = False
                elif event.key == 113:  # q
                    audio_turn_off = sets(screen, score, language, keys, money, fire_number, water_number, True,
                                          audio_turn_off)
                elif event.key == down_key:  # if event.unicode == 's':
                    status_dino = 'sit'
                    if not d.jump_status:
                        d.y = d_y + 34  # d.y += 34
                    if not d.jump_status:
                        d.sit_anim(screen)
                elif event.key == up_key and status_dino != 'sit':  # elif event.unicode == 'w':
                    if d.jump_status == 0:  # and not stop_status:
                        d.jump_status = 1
                        jump_sound.play()
                elif event.key == red_ball_key and not fire_status and fire_number and fire_strelba:
                    fire_number -= 1
                    fire_status = True
                    fire_cor_x = d.x + 89
                    fire_cor_y = d.y
                    if status_dino == 'sit':
                        fire_cor_y = d.y
                        fire_cor_x = d.x + 120
                elif event.key == blue_ball_key and not water_status and water_number and watter_strelba:
                    water_number -= 1
                    water_status = True
                    water_cor_x = d.x + 89
                    water_cor_y = d.y
                    if status_dino == 'sit':
                        water_cor_y = d.y
                        water_cor_x = d.x + 120
            if event.type == pygame.KEYUP:
                if event.key == down_key:  # if event.unicode == 's':
                    status_dino = 'run'
                    d.y = d_y  # d.y -= 34
                    if not d.jump_status and boss_die_status == 0:
                        d.run_anim(screen)

        time += 1
        if time % 10 == 0:
            screen.fill(color)
            if d.jump_status == 0 and status_dino == 'run' and boss_die_status == 0:
                d.run_anim(screen)
            elif d.jump_status == 0 and status_dino == 'sit' and boss_die_status == 0:
                d.sit_anim(screen)
            elif d.jump_status != 0 and status_dino == 'sit':
                pass
                # if d.y <= 180:
                #    d.y += 20
                # else:
                #    d.y = 200
                #    jump_status = 0

        # прыжок:
        d.jump(screen, status_dino, dino1, boss_die_status, d_y)

        if (time % (70 + rand_time) == 0 and next_barier == 'cactus' and last_cactus) or (
                next_barier == 'cactus' and not last_cactus):
            # добавляет кактус и определяет время через которе появится следующее препятсвие
            last_cactus = True
            Cactus(WIDTH, 426, cacti[randint(0, 4)], all_cacti)
            now_barier = 'cactus'
            time = time % 10
            rand_time = randint(-10, 40)  # TODO сделать нормальное время между появлениями кактусов(препятсвий)
        elif (time % (70 + rand_time) == 0 and next_barier == 'bird' and last_cactus) or (
                next_barier == 'bird' and not last_cactus):
            # добавляет птицу; после птицы следующее препятсвие появляется только когда сама птица умирает
            last_cactus = False
            bird_height = randint(1, 3)
            if bird_height == 1:
                Bird(WIDTH, 290, birds)
            elif bird_height == 2:
                if birthday_code:
                    Bird(WIDTH, 320, birds)
                else:
                    Bird(WIDTH, 350, birds)
            elif bird_height == 3:
                Bird(WIDTH, 410, birds)
            now_barier = 'bird'
            next_barier = ''
        elif (time % (70 + rand_time) == 0 and next_barier == 'fare_cactus' and last_cactus) or (
                next_barier == 'fare_cactus' and not last_cactus):
            # добавляет кактус и определяет время через которе появится следующее препятсвие
            last_cactus = True
            Cactus(WIDTH, 335, cacti[5], fare_cacti)
            now_barier = 'fare_cactus'
            time = time % 10
            rand_time = randint(-10, 40)  # TODO сделать нормальное время между появлениями кактусов(препятсвий)
        elif (time % (70 + rand_time) == 0 and next_barier == 'watter_cactus' and last_cactus) or (
                next_barier == 'watter_cactus' and not last_cactus):
            # добавляет кактус и определяет время через которе появится следующее препятсвие
            last_cactus = True
            Cactus(WIDTH, 335, cacti[6], watter_cacti)
            now_barier = 'watter_cactus'
            time = time % 10
            rand_time = randint(-10, 40)  # TODO сделать нормальное время между появлениями кактусов(препятсвий)
        elif (time % (70 + rand_time) == 0 and next_barier == 'coin' and last_cactus) or (
                next_barier == 'coin' and not last_cactus):
            # добавляет кактус и определяет время через которе появится следующее препятсвие
            last_cactus = True
            rand_col = randint(1, 4)
            if rand_col == 1 or rand_col == 2:
                Col_fire_water(WIDTH, 320, fire_ball_img, 'fire', all_col)
            else:
                Col_fire_water(WIDTH, 320, watter_ball_img, 'water', all_col)
            now_barier = 'coin'
            time = time % 10
            rand_time = randint(-10, 40)
            next_barier = 'cactus'

        screen.fill(color)

        # статичные объекты:
        if color == (0, 0, 0):
            screen.blit(moon, (moon_x, 80))
            screen.blit(star, (star_x1, 125))
            screen.blit(star, (star_x2, 150))
            screen.blit(star, (star_x3, 140))
            screen.blit(star, (star_x4, 110))
            screen.blit(star, (star_x5, 140))
            screen.blit(star, (star_x6, 137))
            screen.blit(star, (star_x7, 135))
            screen.blit(star, (star_x8, 133))
            screen.blit(star, (star_x9, 122))
            screen.blit(star, (star_x10, 147))
        else:
            screen.blit(cloud, (cloud_x1, 123))
            screen.blit(cloud, (cloud_x2, 200))
            screen.blit(cloud, (cloud_x3, 216))
            screen.blit(cloud, (cloud_x4, 147))
            screen.blit(cloud, (cloud_x5, 111))
            screen.blit(cloud, (cloud_x6, 50))
            screen.blit(cloud, (cloud_x7, 91))
            screen.blit(cloud, (cloud_x8, 131))
            screen.blit(cloud, (cloud_x9, 115))
            screen.blit(cloud, (cloud_x10, 100))
            screen.blit(night_sun, (sun_x, 100))

        moon_x -= 1
        star_x1 -= 1
        star_x2 -= 1
        star_x3 -= 1
        star_x4 -= 1
        star_x5 -= 1
        star_x6 -= 1
        star_x7 -= 1
        star_x8 -= 1
        star_x9 -= 1
        star_x10 -= 1
        cloud_x1 -= 1
        cloud_x2 -= 1
        cloud_x3 -= 1
        cloud_x4 -= 1
        cloud_x5 -= 1
        cloud_x6 -= 1
        cloud_x7 -= 1
        cloud_x8 -= 1
        cloud_x9 -= 1
        cloud_x10 -= 1
        sun_x -= 1
        if star_x1 <= -40:
            star_x1 = 1200
        if star_x2 <= -40:
            star_x2 = 1200
        if star_x3 <= -40:
            star_x3 = 1200
        if star_x4 <= -40:
            star_x4 = 1200
        if star_x5 <= -40:
            star_x5 = 1200
        if star_x6 <= -40:
            star_x6 = 1200
        if star_x7 <= -40:
            star_x7 = 1200
        if star_x8 <= -40:
            star_x8 = 1200
        if star_x9 <= -40:
            star_x9 = 1200
        if star_x10 <= -40:
            star_x10 = 1200
        if sun_x <= - 100:
            sun_x = 1200
        if cloud_x1 <= - 115:
            cloud_x1 = 1200
        if cloud_x2 <= - 115:
            cloud_x2 = 1200
        if cloud_x3 <= - 115:
            cloud_x3 = 1200
        if cloud_x4 <= - 115:
            cloud_x4 = 1200
        if cloud_x5 <= - 115:
            cloud_x5 = 1200
        if cloud_x6 <= - 115:
            cloud_x6 = 1200
        if cloud_x7 <= - 115:
            cloud_x7 = 1200
        if cloud_x8 <= - 115:
            cloud_x8 = 1200
        if cloud_x9 <= - 115:
            cloud_x9 = 1200
        if cloud_x10 <= - 115:
            cloud_x10 = 1200
        if moon_x <= -40:
            moon_x = 1200

        # Проверка столкновений дино с кактусами и птицами:
        q1 = d.collide_check(all_cacti)
        q2 = d.collide_check(birds)
        q3 = d.collide_check(fare_cacti)
        q4 = d.collide_check(watter_cacti)
        if q1 or q2 or q3 or q4:  # смерть
            pygame.mixer.music.stop()
            die_sound.play()
            d.die(score)
            if status_dino == 'sit':
                d.x, d.y = d_x, d_y
            road_v = 0
            running = False

        # screen.blit(d.image, (d.x, d.y))
        d.update(screen)

        # кактусы:
        all_cacti.update(road_v * road_speed)
        all_cacti.draw(screen)
        if now_barier == 'cactus':
            for cactus in all_cacti:
                if cactus.rect.x <= -1 * cactus.rect.width:  # только если маленький кактус
                    cactus.kill()  # удаляет спрайт, если он оказался за пределами экрана
                    if score > 50:
                        choose = randint(1, 7)  # определяет какое препятсвие будет следующим
                        if choose == 4:
                            next_barier = 'bird'
                        elif choose == 5:
                            if water_number != 0 and watter_strelba:
                                next_barier = 'fare_cactus'
                            else:
                                next_barier = 'cactus'
                        elif choose == 6:
                            if fire_number != 0 and fire_strelba:
                                next_barier = 'watter_cactus'
                            else:
                                next_barier = 'cactus'
                        elif choose == 7:
                            next_barier = 'coin'
                        else:
                            next_barier = 'cactus'

        fare_cacti.update(road_v * road_speed)
        fare_cacti.draw(screen)
        if now_barier == 'fare_cactus':
            for cactus in fare_cacti:
                if cactus.rect.x < -1 * cactus.rect.width:  # только если маленький кактус
                    cactus.kill()  # удаляет спрайт, если он оказался за пределами экрана
                    if score > 50:
                        choose = randint(1, 7)  # определяет какое препятсвие будет следующим
                        if choose == 4:
                            next_barier = 'bird'
                        elif choose == 5:
                            if water_number != 0 and watter_strelba:
                                next_barier = 'fare_cactus'
                            else:
                                next_barier = 'cactus'
                        elif choose == 6:
                            if fire_number != 0 and fire_strelba:
                                next_barier = 'watter_cactus'
                            else:
                                next_barier = 'cactus'
                        elif choose == 7:
                            next_barier = 'coin'
                        else:
                            next_barier = 'cactus'

        watter_cacti.update(road_v * road_speed)
        watter_cacti.draw(screen)
        if now_barier == 'watter_cactus':
            for cactus in watter_cacti:
                if cactus.rect.x < -1 * cactus.rect.width:  # только если маленький кактус
                    cactus.kill()  # удаляет спрайт, если он оказался за пределами экрана
                    if score > 50:
                        choose = randint(1, 7)  # определяет какое препятсвие будет следующим
                        if choose == 4:
                            next_barier = 'bird'
                        elif choose == 5:
                            if water_number != 0 and watter_strelba:
                                next_barier = 'fare_cactus'
                            else:
                                next_barier = 'cactus'
                        elif choose == 6:
                            if fire_number != 0 and fire_strelba:
                                next_barier = 'watter_cactus'
                            else:
                                next_barier = 'cactus'
                        elif choose == 7:
                            next_barier = 'coin'
                        else:
                            next_barier = 'cactus'

        # птицы:
        birds.update(road_v * road_speed, time)
        birds.draw(screen)
        if now_barier == 'bird':

            for bird in birds:
                if bird.rect.x < -94:
                    bird.kill()  # удаляет спрайт, если он оказался за пределами экрана
            if not birds.spritedict:
                choose = randint(1, 7)  # определяет какое препятсвие будет следующим
                if choose == 4:
                    next_barier = 'bird'
                elif choose == 5:
                    if water_number != 0 and watter_strelba:
                        next_barier = 'fare_cactus'
                    else:
                        next_barier = 'cactus'
                elif choose == 6:
                    if fire_number != 0 and fire_strelba:
                        next_barier = 'watter_cactus'
                    else:
                        next_barier = 'cactus'
                elif choose == 7:
                    next_barier = 'coin'
                else:
                    next_barier = 'cactus'

        all_col.update(road_v * road_speed)
        all_col.draw(screen)
        for col in all_col:
            if col.collide_check(dino_group):
                if col.type == 'fire':
                    fire_number += 10
                elif col.type == 'water':
                    water_number += 10
                col.kill()

        # преобразует текущий счет в поверхность и выводит ее:
        score_out = []
        for i in range(1, len(score_str) + 1):
            score_out.insert(0, score_str[len(score_str) - i])
        while len(score_out) != 5:
            score_out.insert(0, '0')
        score_cord_x = 970
        for i in range(len(score_out)):
            screen.blit(nums_dict[score_out[i]], (score_cord_x, score_cord_y))
            score_cord_x += 30

        # преобразует лучший счет в поверхность и выводит ее:
        score_out = []
        screen.blit(HI_img, (870, 700))
        for i in range(1, len(HI_str) + 1):
            score_out.insert(0, HI_str[len(HI_str) - i])
        while len(score_out) != 5:
            score_out.insert(0, '0')
        HI_coard_x = 970
        for i in range(len(score_out)):
            screen.blit(nums_dict[score_out[i]], (HI_coard_x, HI_coard_y))
            HI_coard_x += 30

        # считает очки:
        if score_t % 3 == 0 and boss_die_status == 0:
            score += 1
            score_str = str(score)
        score_t += 1

        # двигает дорожку:
        screen.blit(road1, (road_cord_x1, 475))
        screen.blit(road2, (road_cord_x2, 475))
        if boss_die_status == 0:
            if road_cord_x2 <= 0:
                road_cord_x1 = 0
                road_cord_x2 = 2398
            else:
                road_cord_x1 -= int(road_speed * road_v)
                road_cord_x2 -= int(road_speed * road_v)
            if road_v < 1.9:
                road_v += 0.00016

        # полет огенного шара:
        if fire_status:
            d.fare_ball_anim(screen, fire_cor_x, fire_cor_y, color_must)
            fire_cor_x += 10
        if fire_cor_x > WIDTH:
            fire_cor_x = d.x + 89
            fire_status = False

        # полет водяного шара:
        if water_status:
            d.watter_ball_anim(screen, water_cor_x, water_cor_y, color_must)
            water_cor_x += 10
        if water_cor_x > WIDTH:
            water_cor_x = d.x + 89
            water_status = False

        if fire_status:
            fare = pygame.sprite.groupcollide(d.fare_ball_sprites, watter_cacti, True, True)
            if fare:
                choose = randint(1, 6)  # определяет какое препятсвие будет следующим
                if choose == 4:
                    next_barier = 'bird'
                elif choose == 5:
                    if water_number != 0 and watter_strelba:
                        next_barier = 'fare_cactus'
                    else:
                        next_barier = 'cactus'
                elif choose == 6:
                    if fire_number != 0 and fire_strelba:
                        next_barier = 'watter_cactus'
                    else:
                        next_barier = 'cactus'
                else:
                    next_barier = 'cactus'
                fire_status = False

        if water_status:
            watter = pygame.sprite.groupcollide(d.watter_ball_sprites, fare_cacti, True, True)
            if watter:
                choose = randint(1, 6)  # определяет какое препятсвие будет следующим
                if choose == 4:
                    next_barier = 'bird'
                elif choose == 5:
                    if water_number != 0 and watter_strelba:
                        next_barier = 'fare_cactus'
                    else:
                        next_barier = 'cactus'
                elif choose == 6:
                    if fire_number != 0 and fire_strelba:
                        next_barier = 'watter_cactus'
                    else:
                        next_barier = 'cactus'
                else:
                    next_barier = 'cactus'
                water_status = False

        screen.blit(small_fire_img, (10, 10))
        for i in range(len(str(fire_number))):
            num_fire_surf = pygame.transform.scale(nums_dict[str(fire_number)[i]], (15, 18))
            screen.blit(num_fire_surf, (fire_x + num_fire_surf.get_width() * i, fire_y))
        screen.blit(small_water_img, (10, 30))
        for i in range(len(str(water_number))):
            num_water_surf = pygame.transform.scale(nums_dict[str(water_number)[i]], (15, 18))
            screen.blit(num_water_surf, (water_x + num_water_surf.get_width() * i, water_y))

        if color != color_must:
            if color_must == (255, 255, 255):
                color_rgb += 5
                color = (color_rgb, color_rgb, color_rgb)
            elif color_must == (0, 0, 0):
                color_rgb -= 5
                color = (color_rgb, color_rgb, color_rgb)

        if score == 1000:
            color_must = (0, 0, 0)
        elif score == 1600:
            color_must = (255, 255, 255)
        elif score == 2600:
            color_must = (0, 0, 0)
        elif score == 3400:
            color_must = (255, 255, 255)
        elif score == 4400:
            color_must = (0, 0, 0)
        elif score == 5000:
            color_must = (255, 255, 255)
        elif score == 6200:
            color_must = (0, 0, 0)
        elif score == 6800:
            color_must = (255, 255, 255)

        if score % 1000 == 0 and score:
            score_1000_sound.play()

        # отрисовка и изменение свойств объектов
        # ...

        if boss_die_t > 330:
            screen.fill('black')
            running = False
        # обновление экрана
        pygame.display.flip()

    return audio_turn_off


def game_cycle(screen, color, score, HI, birthday_code, language, keys, water_number, fire_number, money, moon_list,
               sun_list, audio_turn_off, infinity_mode=True):
    global menu_exit
    clock = pygame.time.Clock()
    if birthday_code:
        dino1 = pygame.image.load('imgs/dino_bd_1.png')
        d_y = 178 + 200
        d_x = 100
    else:
        d_y = 210 + 200
        d_x = 100
        dino1 = pygame.image.load('imgs/dino1.png')
    dino1.set_colorkey('white')
    d = Dino(d_x, d_y, birthday_code)

    rerun_img = pygame.image.load('imgs/rerun.png')
    rerun_img.set_colorkey('white')
    game_over_img = pygame.image.load('imgs/game_over.png')
    game_over_img.set_colorkey('white')

    if not infinity_mode:
        score, water_number, fire_number, money, audio_turn_off = origin_dino(screen, color, score, HI, birthday_code,
                                                                              language, keys,
                                                                              water_number, fire_number,
                                                                              money, d, moon_list, sun_list,
                                                                              audio_turn_off)
    else:
        audio_turn_off = infinity_dino(screen, color, score, HI, birthday_code, language, keys, water_number,
                                       fire_number, d, moon_list, sun_list, audio_turn_off)

    if menu_exit:
        run = False
    else:
        run = True
    while run:

        clock.tick(FPS)
        d.die_status = True

        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                quit()  # run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and d.die_status:
                    if int(event.pos[0]) >= 500 and int(event.pos[0]) <= 644 and int(event.pos[1]) >= 270 and int(
                            event.pos[1]) <= 398:
                        if not infinity_mode:
                            if birthday_code:
                                dino1 = pygame.image.load('imgs/dino_bd_1.png')
                                d_y = 178 + 200
                                d_x = 100
                            else:
                                d_y = 210 + 200
                                d_x = 100
                                dino1 = pygame.image.load('imgs/dino1.png')
                            dino1.set_colorkey('white')
                            d = Dino(d_x, d_y, birthday_code)
                            color = (255, 255, 255)
                            score, water_number, fire_number, money, audio_turn_off = origin_dino(screen, color, score,
                                                                                                  HI,
                                                                                                  birthday_code,
                                                                                                  language, keys,
                                                                                                  water_number,
                                                                                                  fire_number,
                                                                                                  money, d, moon_list,
                                                                                                  sun_list,
                                                                                                  audio_turn_off)
                        else:
                            if birthday_code:
                                dino1 = pygame.image.load('imgs/dino_bd_1.png')
                                d_y = 178 + 200
                                d_x = 100
                            else:
                                d_y = 210 + 200
                                d_x = 100
                                dino1 = pygame.image.load('imgs/dino1.png')
                            dino1.set_colorkey('white')
                            d = Dino(d_x, d_y, birthday_code)
                            color = (255, 255, 255)
                            score = 0
                            water_number = 0
                            fire_number = 0
                            audio_turn_off = infinity_dino(screen, color, score, HI, birthday_code, language, keys,
                                                           water_number, fire_number, d,
                                                           moon_list, sun_list, audio_turn_off)
                        if menu_exit:
                            run = False
            if event.type == pygame.KEYDOWN:  # обработка событий клавиатуры
                if event.key == pygame.K_ESCAPE:
                    run = False
                    if not audio_turn_off:
                        pygame.mixer.music.play(-1)

        screen.blit(rerun_img, (500, 270))
        screen.blit(game_over_img, (400, 150))

        pygame.display.flip()


if __name__ == '__main__':
    game_cycle(screen, color, score, HI, birthday_code, language, keys, water_number, fire_number, money)

    pygame.quit()
