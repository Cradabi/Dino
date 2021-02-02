# Анимация бегущего дино

import pygame
from random import randint
from dino import Dino
from bird import Bird
from cactus import Cactus
from boss import Boss
from scene1 import cut_scen_1
from scene2 import cut_scen_2
from scene3 import cut_scen_3
from scene4 import cut_scen_4
import sqlite3

pygame.font.init()

FPS = 60
WIDTH = 1200
HEIGHT = 800


def origin_dino(screen, color, score, HI, birthday_code, language, keys, water_number, fire_number, money):
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
    rerun_img = pygame.image.load('imgs/rerun.png')
    rerun_img.set_colorkey('white')
    game_over_img = pygame.image.load('imgs/game_over.png')
    game_over_img.set_colorkey('white')
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
    fire_x = 35
    fire_y = 10
    water_x = 35
    water_y = 30

    clock = pygame.time.Clock()
    if birthday_code:
        dino1 = pygame.image.load('imgs/dino_bd_1.png')
        d_y = 178
        d_x = 100
    else:
        d_y = 210
        d_x = 100
        dino1 = pygame.image.load('imgs/dino1.png')
    dino1.set_colorkey('white')
    d = Dino(d_x, d_y, birthday_code)
    birds = pygame.sprite.Group()
    status_dino = 'run'
    fire_status = False
    fire_cor_x = d.x + 89
    fire_cor_y = 200
    water_status = False
    water_cor_x = d.x + 89
    water_cor_y = 200
    jump_status = 0
    road_cord_x1 = 0
    road_cord_x2 = 2398
    running = True
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
    jump_time = 0
    time = -1
    HI_str = str(HI)
    HI_t = 0
    HI_coard_y = 500
    fast_jump = 0
    bird_height = 2
    if score <= 2000:
        was_scene_1 = False
    else:
        was_scene_1 = True
    if score <= 4000:
        was_scene_2 = False
    else:
        was_scene_2 = True
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

    b = Boss(600, 166)
    boss_group = pygame.sprite.GroupSingle(b)
    while running:

        clock.tick(FPS)

        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                quit()  # running = False
            if event.type == pygame.MOUSEBUTTONDOWN:  # обработка событий мыши
                if event.button == 1 and not fire_status and fire_number:
                    fire_number -= 1
                    fire_status = True
                    fire_cor_x = d.x + 89
                    fire_cor_y = d.y
                if event.button == 3 and not water_status and water_number:
                    water_number -= 1
                    water_status = True
                    water_cor_x = d.x + 89
                    water_cor_y = d.y
                if status_dino == 'sit' and not fire_status:
                    fire_cor_y = 234
                    fire_cor_x = d.x + 120
                if status_dino == 'sit' and not water_status:
                    water_cor_y = 234
                    water_cor_x = d.x + 120
            if event.type == pygame.KEYDOWN:  # обработка событий клавиатуры
                if event.key == pygame.K_ESCAPE:
                    quit()
                elif event.key == down_key:  # if event.unicode == 's':
                    status_dino = 'sit'
                    if not jump_status:
                        d.y = d_y + 34  # d.y += 34
                    if not jump_status:
                        d.sit_anim(screen)
                elif event.key == up_key and status_dino != 'sit':  # elif event.unicode == 'w':
                    if jump_status == 0:  # and not stop_status:
                        jump_status = 1
                        jump_sound.play()
                elif event.key == red_ball_key and not fire_status and fire_number:
                    fire_number -= 1
                    fire_status = True
                    fire_cor_x = d.x + 89
                    fire_cor_y = d.y
                    if status_dino == 'sit':
                        fire_cor_y = 234
                        fire_cor_x = d.x + 120
                elif event.key == blue_ball_key and not water_status and water_number:
                    water_number -= 1
                    water_status = True
                    water_cor_x = d.x + 89
                    water_cor_y = d.y
                    if status_dino == 'sit':
                        water_cor_y = 234
                        water_cor_x = d.x + 120
            if event.type == pygame.KEYUP:
                if event.key == down_key:  # if event.unicode == 's':
                    status_dino = 'run'
                    d.y = d_y  # d.y -= 34
                    if not jump_status:
                        d.run_anim(screen)

        time += 1
        if time % 10 == 0:
            screen.fill(color)
            if jump_status == 0 and status_dino == 'run':
                d.run_anim(screen)
            elif jump_status == 0 and status_dino == 'sit':
                d.sit_anim(screen)
            elif jump_status != 0 and status_dino == 'sit':
                pass
                # if d.y <= 180:
                #    d.y += 20
                # else:
                #    d.y = 200
                #    jump_status = 0

        # прыжок:
        if running:
            if jump_status == 1:  # дино летит вверх
                jump_time += 1
                if jump_time % 20 != 0:
                    if jump_time % 2 == 0:
                        fast_jump += 1
                    d.y -= 14
                    d.y += fast_jump
                    d.image = dino1
                    # screen.blit(dino1, (d_x, d_y))
                else:
                    jump_status = 2
                    jump_time = 0
                if status_dino == 'sit':
                    jump_status = 4
            elif jump_status == 2:  # дино весит в воздухе
                jump_time += 1
                if jump_time % 1 != 0:
                    d.image = dino1
                    # screen.blit(dino1, (d_x, d_y))
                else:
                    jump_status = 3
                    jump_time = 0
            elif jump_status == 3:  # дино просто опускается
                jump_time += 1
                if jump_time % 20 != 0 and d.y < 210:
                    d.y += 14
                    d.y -= fast_jump
                    if jump_time % 2 == 0:
                        fast_jump -= 1
                    d.image = dino1
                    # screen.blit(dino1, (d_x, d_y))
                else:
                    jump_status = 0
                    jump_time = 0
                    fast_jump = 0
                    # d.y = 210
                    if status_dino == 'run':
                        d.run_anim(screen)
                    elif status_dino == 'sit':
                        d.sit_anim(screen)

                if status_dino == 'sit':
                    jump_status = 4

            elif jump_status == 4:  # дино резко опускается т.к. была нажата клавиша вниз
                jump_time += 2
                if jump_time % 20 != 0 and d.y < 210:
                    d.y += 28
                    d.y -= fast_jump
                    if jump_time % 2 == 0:
                        fast_jump -= 2
                    d.image = dino1
                    # screen.blit(dino1, (d_x, d_y))
                else:
                    jump_status = 0
                    jump_time = 0
                    fast_jump = 0
                    if status_dino == 'run':
                        d.run_anim(screen)
                    elif status_dino == 'sit':
                        if birthday_code:
                            d.y = d_y + 40
                        else:
                            d.y = d_y + 34

                        d.sit_anim(screen)
                    d.sit_anim(screen)

        if not stop_status:
            if (time % (70 + rand_time) == 0 and next_barier == 'cactus' and last_cactus) or (
                    next_barier == 'cactus' and not last_cactus):
                # добавляет кактус и определяет время через которе появится следующее препятсвие
                last_cactus = True
                Cactus(WIDTH, 226, cacti[randint(0, 4)], all_cacti)
                now_barier = 'cactus'
                time = time % 10
                rand_time = randint(-10, 40)  # TODO сделать нормальное время между появлениями кактусов(препятсвий)
            elif (time % (70 + rand_time) == 0 and next_barier == 'bird' and last_cactus) or (
                    next_barier == 'bird' and not last_cactus):
                # добавляет птицу; после птицы следующее препятсвие появляется только когда сама птица умирает
                last_cactus = False
                bird_height = randint(1, 3)
                if bird_height == 1:
                    Bird(WIDTH, 90, birds)
                elif bird_height == 2:
                    if birthday_code:
                        Bird(WIDTH, 120, birds)
                    else:
                        Bird(WIDTH, 150, birds)
                elif bird_height == 3:
                    Bird(WIDTH, 210, birds)
                now_barier = 'bird'
                next_barier = ''
            elif (time % (70 + rand_time) == 0 and next_barier == 'fare_cactus' and last_cactus) or (
                    next_barier == 'fare_cactus' and not last_cactus):
                # добавляет кактус и определяет время через которе появится следующее препятсвие
                last_cactus = True
                Cactus(WIDTH, 135, cacti[5], fare_cacti)
                now_barier = 'fare_cactus'
                time = time % 10
                rand_time = randint(-10, 40)  # TODO сделать нормальное время между появлениями кактусов(препятсвий)
            elif (time % (70 + rand_time) == 0 and next_barier == 'watter_cactus' and last_cactus) or (
                    next_barier == 'watter_cactus' and not last_cactus):
                # добавляет кактус и определяет время через которе появится следующее препятсвие
                last_cactus = True
                Cactus(WIDTH, 135, cacti[6], watter_cacti)
                now_barier = 'watter_cactus'
                time = time % 10
                rand_time = randint(-10, 40)  # TODO сделать нормальное время между появлениями кактусов(препятсвий)
        elif not all_cacti.spritedict and not birds.spritedict \
                and not fare_cacti.spritedict and not watter_cacti.spritedict:  # проверка остались ли еще препятсвия
            stop_status = True
            if stop_t % 50 == 0:
                if not was_scene_1:
                    was_scene_1 = True
                    cut_scen_1(screen, color, score, HI, road_cord_x1, birthday_code, language, keys, water_number,
                               fire_number, money)
                    stop_status = False
                    road_v = 1.0
                    score_t = 0
                    all_cacti = pygame.sprite.Group()
                    fare_cacti = pygame.sprite.Group()
                    watter_cacti = pygame.sprite.Group()
                elif not was_scene_2 and was_scene_1:
                    was_scene_2 = True
                    cut_scen_2(screen, color, score, HI, road_cord_x1, birthday_code, language, keys, water_number,
                               fire_number, money)
                    stop_status = False
                    road_v = 1.0
                    score_t = 0
                    all_cacti = pygame.sprite.Group()
                    fare_cacti = pygame.sprite.Group()
                    watter_cacti = pygame.sprite.Group()
                elif not was_scene_3 and was_scene_1 and was_scene_2:
                    was_scene_3 = True
                    cut_scen_3(screen, color, score, HI, road_cord_x1, birthday_code, language, keys, water_number,
                               fire_number, money)
                    stop_status = False
                    road_v = 1.0
                    score_t = 0
                    all_cacti = pygame.sprite.Group()
                    fare_cacti = pygame.sprite.Group()
                    watter_cacti = pygame.sprite.Group()
                elif not was_scene_4 and was_scene_1 and was_scene_2 and was_scene_3:
                    was_scene_4 = True
                    cut_scen_4(screen, color, score, HI, road_cord_x1, birthday_code, language, keys, water_number,
                               fire_number, money)
                    stop_status = False
                    road_v = 1.0
                    score_t = 0
                    all_cacti = pygame.sprite.Group()
                    fare_cacti = pygame.sprite.Group()
                    watter_cacti = pygame.sprite.Group()
                    boss_fight = True
            else:
                stop_t += 1

        screen.fill(color)

        # статичные объекты:
        if color == (0, 0, 0):
            screen.blit(moon, (400, 80))
            screen.blit(star, (500, 130))
        else:
            screen.blit(cloud, (200, 100))
            screen.blit(night_sun, (30, 100))

        # Проверка столкновений дино с кактусами и птицами:
        q1 = d.collide_check(all_cacti)
        q2 = d.collide_check(birds)
        q3 = d.collide_check(fare_cacti)
        q4 = d.collide_check(watter_cacti)
        if q1 or q2 or q3 or q4:  # смерть
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

        # кактусы:
        all_cacti.update(road_v * road_speed)
        all_cacti.draw(screen)
        if now_barier == 'cactus':
            for cactus in all_cacti:
                if cactus.rect.x <= -1 * cactus.rect.width:  # только если маленький кактус
                    cactus.kill()  # удаляет спрайт, если он оказался за пределами экрана
                    if score > 50:
                        if not boss_fight:
                            choose = randint(1, 6)  # определяет какое препятсвие будет следующим
                            if choose == 4:
                                next_barier = 'bird'
                            elif choose == 5:
                                if fire_number != 0:
                                    next_barier = 'fare_cactus'
                                else:
                                    next_barier = 'cactus'
                            elif choose == 6:
                                if water_number != 0:
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
                            choose = randint(1, 6)  # определяет какое препятсвие будет следующим
                            if choose == 4:
                                next_barier = 'bird'
                            elif choose == 5:
                                if fire_number != 0:
                                    next_barier = 'fare_cactus'
                                else:
                                    next_barier = 'cactus'
                            elif choose == 6:
                                if water_number != 0:
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

        watter_cacti.update(road_v * road_speed)
        watter_cacti.draw(screen)
        if now_barier == 'watter_cactus':
            for cactus in watter_cacti:
                if cactus.rect.x < -1 * cactus.rect.width:  # только если маленький кактус
                    cactus.kill()  # удаляет спрайт, если он оказался за пределами экрана
                    if score > 50:
                        if not boss_fight:
                            choose = randint(1, 6)  # определяет какое препятсвие будет следующим
                            if choose == 4:
                                next_barier = 'bird'
                            elif choose == 5:
                                if fire_number != 0:
                                    next_barier = 'fare_cactus'
                                else:
                                    next_barier = 'cactus'
                            elif choose == 6:
                                if water_number != 0:
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

        # птицы:
        birds.update(road_v * road_speed, time)
        birds.draw(screen)
        if now_barier == 'bird':

            for bird in birds:
                if bird.rect.x < -94:
                    bird.kill()  # удаляет спрайт, если он оказался за пределами экрана
                if b.rect.x + b.rect.w < bird.rect.x <= b.rect.w + 40 + int(
                        road_v * 10) + b.rect.x and bird.rect.y == 210:
                    b.jump_status = 1
            if not birds.spritedict:
                if not boss_fight:
                    choose = randint(1, 6)  # определяет какое препятсвие будет следующим
                    if choose == 4:
                        next_barier = 'bird'
                    elif choose == 5:
                        if fire_number != 0:
                            next_barier = 'fare_cactus'
                        else:
                            next_barier = 'cactus'
                    elif choose == 6:
                        if water_number != 0:
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
        screen.blit(HI_img, (870, 500))
        for i in range(1, len(HI_str) + 1):
            score_out.insert(0, HI_str[len(HI_str) - i])
        while len(score_out) != 5:
            score_out.insert(0, '0')
        HI_coard_x = 970
        for i in range(len(score_out)):
            screen.blit(nums_dict[score_out[i]], (HI_coard_x, HI_coard_y))
            HI_coard_x += 30

        # считает очки:
        if score_t % 3 == 0 and stop_status == False:
            score += 1
            score_str = str(score)
        score_t += 1

        # двигает дорожку:
        screen.blit(road1, (road_cord_x1, 279))
        screen.blit(road2, (road_cord_x2, 279))
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
                b.hp -= 5
                print(b.hp)
                for ball in d.fare_ball_sprites:
                    ball.kill()
                fire_status = False
            if bq3:
                b.hp -= 5
                print(b.hp)
                for ball in d.watter_ball_sprites:
                    ball.kill()
                water_status = False
            if b.hp <= 0:
                b.die()

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
            fare = pygame.sprite.groupcollide(d.fare_ball_sprites, fare_cacti, True, True)
            if fare:
                if not boss_fight:
                    choose = randint(1, 6)  # определяет какое препятсвие будет следующим
                    if choose == 4:
                        next_barier = 'bird'
                    elif choose == 5:
                        if fire_number != 0:
                            next_barier = 'fare_cactus'
                        else:
                            next_barier = 'cactus'
                    elif choose == 6:
                        if water_number != 0:
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
            watter = pygame.sprite.groupcollide(d.watter_ball_sprites, watter_cacti, True, True)
            if watter:
                if not boss_fight:
                    choose = randint(1, 6)  # определяет какое препятсвие будет следующим
                    if choose == 4:
                        next_barier = 'bird'
                    elif choose == 5:
                        if fire_number != 0:
                            next_barier = 'fare_cactus'
                        else:
                            next_barier = 'cactus'
                    elif choose == 6:
                        if water_number != 0:
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

        # обновление экрана
        pygame.display.flip()

    run = True
    while run:

        clock.tick(FPS)

        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                quit()  # run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and d.die_status:
                    if int(event.pos[0]) >= 300 and int(event.pos[0]) <= 444 and int(event.pos[1]) >= 200 and int(
                            event.pos[1]) <= 328:
                        score = 0
                        color = (255, 255, 255)
                        origin_dino(screen, color, score, HI, birthday_code, language, keys, water_number, fire_number,
                                    money)
            if event.type == pygame.KEYDOWN:  # обработка событий клавиатуры
                if event.key == pygame.K_ESCAPE:
                    quit()

        screen.blit(rerun_img, (300, 200))

        pygame.display.flip()


if __name__ == '__main__':
    origin_dino(screen, color, score, HI, birthday_code, language, keys)

    pygame.quit()
