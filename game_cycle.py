# Анимация бегущего дино

import pygame
from random import randint
from dino import Dino
from bird import Bird
from cactus import Cactus
import sqlite3

pygame.font.init()

FPS = 60
WIDTH = 1200
HEIGHT = 800


def origin_dino(screen, color, score, HI, birthday_code, language, keys):
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
    fare_cactus = pygame.image.load('imgs/fare_cactus.jpg')
    fare_cactus.set_colorkey('white')
    fare_cactus_black = pygame.image.load('imgs/fare_cactus1.jpg')
    fare_cactus_black.set_colorkey('black')
    watter_cactus = pygame.image.load('imgs/watter_cactus.jpg')
    watter_cactus.set_colorkey('white')
    watter_cactus_black = pygame.image.load('imgs/watter_cactus1.jpg')
    watter_cactus_black.set_colorkey('black')
    cacti = [small_cactus1, small_cactus2, small_cactus3, small_cactus4, small_cactus5, fare_cactus, watter_cactus,
             fare_cactus_black, watter_cactus_black]
    all_cacti = pygame.sprite.Group()
    fare_cacti = pygame.sprite.Group()
    watter_cacti = pygame.sprite.Group()

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
    while running:

        clock.tick(FPS)

        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                quit()  # running = False
            if event.type == pygame.MOUSEBUTTONDOWN:  # обработка событий мыши
                if event.button == 1 and not fire_status:
                    fire_status = True
                    fire_cor_x = d.x + 89
                    fire_cor_y = d.y
                if event.button == 3 and not water_status:
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
                    if jump_status == 0 and not stop_status:
                        jump_status = 1
                elif event.key == red_ball_key and not fire_status:
                    fire_status = True
                    fire_cor_x = d.x + 89
                    fire_cor_y = d.y
                    if status_dino == 'sit':
                        fire_cor_y = 234
                        fire_cor_x = d.x + 120
                elif event.key == blue_ball_key and not water_status:
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

        if score < 2000:
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
                if color_must == (255, 255, 255):
                    Cactus(WIDTH, 135, cacti[5], fare_cacti)
                elif color_must == (0, 0, 0):
                    Cactus(WIDTH, 135, cacti[7], fare_cacti)

                now_barier = 'fare_cactus'
                time = time % 10
                rand_time = randint(-10, 40)  # TODO сделать нормальное время между появлениями кактусов(препятсвий)
            elif (time % (70 + rand_time) == 0 and next_barier == 'watter_cactus' and last_cactus) or (
                    next_barier == 'watter_cactus' and not last_cactus):
                # добавляет кактус и определяет время через которе появится следующее препятсвие
                last_cactus = True
                if color_must == (255, 255, 255):
                    Cactus(WIDTH, 135, cacti[6], watter_cacti)
                elif color_must == (0, 0, 0):
                    Cactus(WIDTH, 135, cacti[8], watter_cacti)

                now_barier = 'watter_cactus'
                time = time % 10
                rand_time = randint(-10, 40)  # TODO сделать нормальное время между появлениями кактусов(препятсвий)
        elif not all_cacti.spritedict and not birds.spritedict \
                and not fare_cacti.spritedict and not watter_cacti.spritedict:  # проверка остались ли еще препятсвия
            stop_status = True
            if stop_t % 50 == 0:
                cut_scen_1(screen, color, score, HI, road_cord_x1, birthday_code, language, keys)
            else:
                stop_t += 1

        screen.fill(color)

        # статичные объекты:
        screen.blit(cloud, (200, 100))
        screen.blit(moon, (400, 80))
        screen.blit(star, (500, 130))
        screen.blit(night_sun, (30, 100))

        # Проверка столкновений дино с кактусами и птицами:
        q1 = d.collide_check(all_cacti)
        q2 = d.collide_check(birds)
        q3 = d.collide_check(fare_cacti)
        q4 = d.collide_check(watter_cacti)
        if q1 or q2 or q3 or q4:  # смерть
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
                        choose = randint(1, 6)  # определяет какое препятсвие будет следующим
                        if choose == 4:
                            next_barier = 'bird'
                        elif choose == 5:
                            next_barier = 'fare_cactus'
                        elif choose == 6:
                            next_barier = 'watter_cactus'
                        else:
                            next_barier = 'cactus'

        fare_cacti.update(road_v * road_speed)
        fare_cacti.draw(screen)
        if now_barier == 'fare_cactus':
            for cactus in fare_cacti:
                if cactus.rect.x < -1 * cactus.rect.width:  # только если маленький кактус
                    cactus.kill()  # удаляет спрайт, если он оказался за пределами экрана
                    if score > 50:
                        choose = randint(1, 6)  # определяет какое препятсвие будет следующим
                        if choose == 4:
                            next_barier = 'bird'
                        elif choose == 5:
                            next_barier = 'fare_cactus'
                        elif choose == 6:
                            next_barier = 'watter_cactus'
                        else:
                            next_barier = 'cactus'

        watter_cacti.update(road_v * road_speed)
        watter_cacti.draw(screen)
        if now_barier == 'watter_cactus':
            for cactus in watter_cacti:
                if cactus.rect.x < -1 * cactus.rect.width:  # только если маленький кактус
                    cactus.kill()  # удаляет спрайт, если он оказался за пределами экрана
                    if score > 50:
                        choose = randint(1, 6)  # определяет какое препятсвие будет следующим
                        if choose == 4:
                            next_barier = 'bird'
                        elif choose == 5:
                            next_barier = 'fare_cactus'
                        elif choose == 6:
                            next_barier = 'watter_cactus'
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
                choose = randint(1, 6)  # определяет какое препятсвие будет следующим
                if choose == 4:
                    next_barier = 'bird'
                elif choose == 5:
                    next_barier = 'fare_cactus'
                elif choose == 6:
                    next_barier = 'watter_cactus'
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
        screen.blit(road1, (road_cord_x1, 270))
        screen.blit(road2, (road_cord_x2, 270))
        if road_cord_x2 <= -1400:
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
            fare = pygame.sprite.groupcollide(d.fare_ball_sprites, fare_cacti, True, True)
            if fare:
                choose = randint(1, 6)  # определяет какое препятсвие будет следующим
                if choose == 4:
                    next_barier = 'bird'
                elif choose == 5:
                    next_barier = 'fare_cactus'
                elif choose == 6:
                    next_barier = 'watter_cactus'
                else:
                    next_barier = 'cactus'
                fire_status = False

        if water_status:
            watter = pygame.sprite.groupcollide(d.watter_ball_sprites, watter_cacti, True, True)
            if watter:
                choose = randint(1, 6)  # определяет какое препятсвие будет следующим
                if choose == 4:
                    next_barier = 'bird'
                elif choose == 5:
                    next_barier = 'fare_cactus'
                elif choose == 6:
                    next_barier = 'watter_cactus'
                else:
                    next_barier = 'cactus'
                water_status = False

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
                        origin_dino(screen, color, score, HI, birthday_code, language, keys)
            if event.type == pygame.KEYDOWN:  # обработка событий клавиатуры
                if event.key == pygame.K_ESCAPE:
                    quit()

        screen.blit(rerun_img, (300, 200))

        pygame.display.flip()


def cut_scen_1(screen, color, score, HI, road_cord_x1, birthday_code, language, keys):
    clock = pygame.time.Clock()

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
    cloud = pygame.image.load('imgs/cloud.png')
    cloud.set_colorkey('white')
    night_sun = pygame.image.load('imgs/night_sun.png')
    night_sun.set_colorkey('black')
    moon = pygame.image.load('imgs/moon.png')
    moon.set_colorkey('black')
    star = pygame.image.load('imgs/star.png')
    star.set_colorkey('black')
    HI_img = pygame.image.load('imgs/HI.png')
    HI_img.set_colorkey('white')
    mag_left = pygame.image.load('imgs/water_magic_left.png')
    mag_right = pygame.image.load('imgs/water_magic_right.png')
    road1 = pygame.image.load('imgs/road.png')
    road1.set_colorkey('white')
    dialog_left = pygame.image.load('imgs/dialog_left.png')
    dialog_right = pygame.image.load('imgs/dialog_right.png')
    dialog_left.set_colorkey('white')
    dialog_right.set_colorkey('white')
    if birthday_code:
        dino1 = pygame.image.load('imgs/dino_bd_1.png')
        d_y = 178
        d_x = 100
    else:
        d_y = 210
        d_x = 100
        dino1 = pygame.image.load('imgs/dino1.png')
    dino1.set_colorkey('white')
    d = Dino(d_x, d_y)
    running = True
    mag_cord_x = WIDTH
    mag_cord_y = 184
    t = 1
    t_c = 1
    score_str = str(score)
    score_cord_y = 50
    HI_str = str(HI)
    HI_t = 0
    HI_coard_y = 500
    while running:

        clock.tick(FPS)

        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                quit()  # running = False
            if event.type == pygame.MOUSEBUTTONDOWN:  # обработка событий мыши
                if event.button == 1:
                    if t > 200 and t < 1200:
                        t_c = t // 100
                        t_c += 1
                        t = t_c * 100
            if event.type == pygame.KEYDOWN:  # обработка событий клавиатуры
                if event.key == 32:
                    if t > 200 and t < 1200:
                        t_c = t // 100
                        t_c += 1
                        t = t_c * 100
        screen.fill(color)
        screen.blit(dino1, (d.x, d.y))
        screen.blit(road1, (0, 270))
        screen.blit(cloud, (200, 100))
        screen.blit(moon, (400, 80))
        screen.blit(star, (500, 130))
        screen.blit(night_sun, (30, 100))
        t += 1
        if t < 200:
            # t += 1
            mag_cord_x -= 1
        screen.blit(mag_left, (mag_cord_x, mag_cord_y))
        if t > 200 and t < 300:
            screen.blit(mag_left, (mag_cord_x, mag_cord_y))
            screen.blit(dialog_right, (900, 300))
            if language == 'rus':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Привет, Дино.", False, (0, 0, 0))
                screen.blit(text, (930, 370))
            elif language == 'eng':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Hi, Dino.", False, (0, 0, 0))
                screen.blit(text, (930, 370))
            # t += 1
        elif t >= 300 and t < 400:
            screen.blit(mag_left, (mag_cord_x, mag_cord_y))
            screen.blit(dialog_left, (10, 300))
            if language == 'rus':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Здравствуйте, кто", False, (0, 0, 0))
                screen.blit(text, (40, 370))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("вы? И откуда вы знаете", False, (0, 0, 0))
                screen.blit(text, (40, 390))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("мое имя?", False, (0, 0, 0))
                screen.blit(text, (40, 410))
            elif language == 'eng':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Hello, who are you?", False, (0, 0, 0))
                screen.blit(text, (40, 370))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("And how do you", False, (0, 0, 0))
                screen.blit(text, (40, 390))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("know my name?", False, (0, 0, 0))
                screen.blit(text, (40, 410))
            # t += 1
        elif t >= 400 and t < 500:
            screen.blit(mag_left, (mag_cord_x, mag_cord_y))
            screen.blit(dialog_right, (900, 300))
            if language == 'rus':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Я маг воды, и знаю тебя,", False, (0, 0, 0))
                screen.blit(text, (930, 370))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("потому что ты наша", False, (0, 0, 0))
                screen.blit(text, (930, 390))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("последняя надежда", False, (0, 0, 0))
                screen.blit(text, (930, 410))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("на спасение", False, (0, 0, 0))
                screen.blit(text, (930, 430))
            elif language == 'eng':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("I am a water magician,", False, (0, 0, 0))
                screen.blit(text, (930, 370))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("and I know you because", False, (0, 0, 0))
                screen.blit(text, (930, 390))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("you are our hope for", False, (0, 0, 0))
                screen.blit(text, (930, 410))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("salvation.", False, (0, 0, 0))
                screen.blit(text, (930, 430))
        elif t >= 500 and t < 600:
            screen.blit(mag_left, (mag_cord_x, mag_cord_y))
            screen.blit(dialog_left, (10, 300))
            if language == 'rus':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Надежда на что?", False, (0, 0, 0))
                screen.blit(text, (40, 370))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Чем я могу вам помочь?", False, (0, 0, 0))
                screen.blit(text, (40, 390))
            elif language == 'eng':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Hope for what?", False, (0, 0, 0))
                screen.blit(text, (40, 370))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("How can I help you?", False, (0, 0, 0))
                screen.blit(text, (40, 390))
        elif t >= 600 and t < 700:
            screen.blit(mag_left, (mag_cord_x, mag_cord_y))
            screen.blit(dialog_right, (900, 300))
            if language == 'rus':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("На наш город напало", False,
                                 (0, 0, 0))
                screen.blit(text, (930, 370))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("огромное чудовище,", False,
                                 (0, 0, 0))
                screen.blit(text, (930, 390))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("которое захватило наш", False,
                                 (0, 0, 0))
                screen.blit(text, (930, 410))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("райский островок", False,
                                 (0, 0, 0))
                screen.blit(text, (930, 430))
            elif language == 'eng':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Our city was attacked", False,
                                 (0, 0, 0))
                screen.blit(text, (930, 370))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("by a huge monster", False,
                                 (0, 0, 0))
                screen.blit(text, (930, 390))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("that captured our", False,
                                 (0, 0, 0))
                screen.blit(text, (930, 410))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("island of paradise", False,
                                 (0, 0, 0))
                screen.blit(text, (930, 430))
        elif t >= 700 and t < 800:
            screen.blit(mag_left, (mag_cord_x, mag_cord_y))
            screen.blit(dialog_right, (900, 300))
            if language == 'rus':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Он выгнал нас,", False, (0, 0, 0))
                screen.blit(text, (930, 370))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("и мы надеялись,", False, (0, 0, 0))
                screen.blit(text, (930, 390))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("что ты сможешь", False, (0, 0, 0))
                screen.blit(text, (930, 410))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("победить его.", False, (0, 0, 0))
                screen.blit(text, (930, 430))
            elif language == 'eng':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("He kicked us out,", False, (0, 0, 0))
                screen.blit(text, (930, 370))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("and we hoped, that", False, (0, 0, 0))
                screen.blit(text, (930, 390))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("you can beat him.", False, (0, 0, 0))
                screen.blit(text, (930, 410))
        elif t >= 800 and t < 900:
            screen.blit(mag_left, (mag_cord_x, mag_cord_y))
            screen.blit(dialog_left, (10, 300))
            if language == 'rus':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Как я смогу победить", False, (0, 0, 0))
                screen.blit(text, (40, 370))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("его, если ты", False, (0, 0, 0))
                screen.blit(text, (40, 390))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("не смог этого?", False, (0, 0, 0))
                screen.blit(text, (40, 410))
            elif language == 'eng':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("How can I beat him,", False, (0, 0, 0))
                screen.blit(text, (40, 370))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("if you can't?", False, (0, 0, 0))
                screen.blit(text, (40, 390))
        elif t >= 900 and t < 1000:
            screen.blit(mag_left, (mag_cord_x, mag_cord_y))
            screen.blit(dialog_right, (900, 300))
            if language == 'rus':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Я помогу тебе.", False, (0, 0, 0))
                screen.blit(text, (930, 370))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Сим. Салабим.", False, (0, 0, 0))
                screen.blit(text, (930, 390))
            elif language == 'eng':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Ok.I will help you.", False, (0, 0, 0))
                screen.blit(text, (930, 370))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Sim. Salabim.", False, (0, 0, 0))
                screen.blit(text, (930, 390))
        elif t >= 1000 and t < 1100:
            screen.blit(mag_left, (mag_cord_x, mag_cord_y))
            screen.blit(dialog_right, (900, 300))
            if language == 'rus':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Теперь ты можешь",
                                 False,
                                 (0, 0, 0))
                screen.blit(text, (930, 370))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("извергать водяные шары.",
                                 False,
                                 (0, 0, 0))
                screen.blit(text, (930, 390))
                text = f2.render("Они тебе помогут",
                                 False,
                                 (0, 0, 0))
                screen.blit(text, (930, 410))
                text = f2.render("в битве с чудовищем.",
                                 False,
                                 (0, 0, 0))
                screen.blit(text, (930, 430))
            elif language == 'eng':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Now you can spew",
                                 False,
                                 (0, 0, 0))
                screen.blit(text, (930, 370))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("waterball. They will help",
                                 False,
                                 (0, 0, 0))
                screen.blit(text, (930, 390))
                text = f2.render("you in the battle.",
                                 False,
                                 (0, 0, 0))
                screen.blit(text, (930, 410))
        elif t >= 1100 and t < 1200:
            screen.blit(mag_left, (mag_cord_x, mag_cord_y))
            screen.blit(dialog_left, (10, 300))
            if language == 'rus':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Спасибо. Я помогу вам", False, (0, 0, 0))
                screen.blit(text, (40, 370))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("До свидания.", False, (0, 0, 0))
                screen.blit(text, (40, 390))
            elif language == 'eng':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Thanks. I will try to help.", False, (0, 0, 0))
                screen.blit(text, (40, 370))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Goodbye.", False, (0, 0, 0))
                screen.blit(text, (40, 390))
        elif t >= 1200 and t < 1430:
            # t += 1
            mag_cord_x += 1
            screen.blit(mag_right, (mag_cord_x, mag_cord_y))
        elif t >= 1430:
            running = False
            origin_dino(screen, color, score, HI, birthday_code, language, keys)

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
        HI_coard_y = 500
        screen.blit(HI_img, (870, 500))
        for i in range(1, len(HI_str) + 1):
            score_out.insert(0, HI_str[len(HI_str) - i])
        while len(score_out) != 5:
            score_out.insert(0, '0')
        HI_coard_x = 970
        for i in range(len(score_out)):
            screen.blit(nums_dict[score_out[i]], (HI_coard_x, HI_coard_y))
            HI_coard_x += 30
        pygame.display.flip()


def cut_scen_2(screen, color, score, HI, road_cord_x1, birthday_code, language, keys):
    clock = pygame.time.Clock()

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
    mag_left = pygame.image.load('imgs/fire_magic_left.png')
    mag_right = pygame.image.load('imgs/fire_magic_right.png')
    road1 = pygame.image.load('imgs/road.png')
    road1.set_colorkey('white')
    dialog_left = pygame.image.load('imgs/dialog_left.png')
    dialog_right = pygame.image.load('imgs/dialog_right.png')
    cloud = pygame.image.load('imgs/cloud.png')
    cloud.set_colorkey('white')
    night_sun = pygame.image.load('imgs/night_sun.png')
    night_sun.set_colorkey('black')
    moon = pygame.image.load('imgs/moon.png')
    moon.set_colorkey('black')
    star = pygame.image.load('imgs/star.png')
    star.set_colorkey('black')
    if birthday_code:
        dino1 = pygame.image.load('imgs/dino_bd_1.png')
        d_y = 178
        d_x = 100
    else:
        d_y = 210
        d_x = 100
        dino1 = pygame.image.load('imgs/dino1.png')
    dino1.set_colorkey('white')
    d = Dino(d_x, d_y)
    running = True
    mag_cord_x = WIDTH
    mag_cord_y = 184
    t = 1
    t_c = 1
    score_str = str(score)
    score_cord_y = 50
    HI_str = str(HI)
    HI_t = 0
    HI_coard_y = 500
    while running:

        clock.tick(FPS)

        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                quit()  # running = False
            if event.type == pygame.MOUSEBUTTONDOWN:  # обработка событий мыши
                if event.button == 1:
                    if t > 200 and t < 900:
                        t_c = t // 100
                        t_c += 1
                        t = t_c * 100
            if event.type == pygame.KEYDOWN:  # обработка событий клавиатуры
                if event.key == 32:
                    if t > 200 and t < 1200:
                        t_c = t // 100
                        t_c += 1
                        t = t_c * 100
        screen.fill(color)
        screen.blit(dino1, (d.x, d.y))
        screen.blit(road1, (0, 270))
        screen.blit(cloud, (200, 100))
        screen.blit(moon, (400, 80))
        screen.blit(star, (500, 130))
        screen.blit(night_sun, (30, 100))
        t += 1
        if t < 200:
            # t += 1
            mag_cord_x -= 1
        screen.blit(mag_left, (mag_cord_x, mag_cord_y))
        if t > 200 and t < 300:
            screen.blit(mag_left, (mag_cord_x, mag_cord_y))
            screen.blit(dialog_right, (550, 400))
            if language == 'rus':
                f2 = pygame.font.SysFont('arial', 14)
                text = f2.render("Привет, Дино.", False, (0, 0, 0))
                screen.blit(text, (555, 405))
                # t += 1
        elif t >= 300 and t < 400:
            screen.blit(mag_left, (mag_cord_x, mag_cord_y))
            screen.blit(dialog_left, (100, 400))
            if language == 'rus':
                f2 = pygame.font.SysFont('arial', 14)
                text = f2.render("Здравствуйте.", False, (0, 0, 0))
                screen.blit(text, (105, 405))
                f2 = pygame.font.SysFont('arial', 14)
                text = f2.render("Вы очень похожи на мага воды.", False, (0, 0, 0))
                screen.blit(text, (105, 420))
            elif language == 'eng':
                f2 = pygame.font.SysFont('arial', 14)
                text = f2.render("Hello.", False, (0, 0, 0))
                screen.blit(text, (105, 405))
                f2 = pygame.font.SysFont('arial', 14)
                text = f2.render("You look like a water mag.", False, (0, 0, 0))
                screen.blit(text, (105, 420))
            # t += 1
        elif t >= 400 and t < 500:
            screen.blit(mag_left, (mag_cord_x, mag_cord_y))
            screen.blit(dialog_right, (550, 400))
            if language == 'rus':
                f2 = pygame.font.SysFont('arial', 14)
                text = f2.render("Я его брат.", False, (0, 0, 0))
                screen.blit(text, (555, 405))
                f2 = pygame.font.SysFont('arial', 14)
                text = f2.render("Как я понимаю, он уже", False, (0, 0, 0))
                screen.blit(text, (555, 420))
                f2 = pygame.font.SysFont('arial', 14)
                text = f2.render("рассказал тебе про нашу ситуацию.", False, (0, 0, 0))
                screen.blit(text, (555, 435))
            elif language == 'eng':
                f2 = pygame.font.SysFont('arial', 14)
                text = f2.render("I am his brother.", False, (0, 0, 0))
                screen.blit(text, (555, 405))
                f2 = pygame.font.SysFont('arial', 14)
                text = f2.render("Has he already told you", False, (0, 0, 0))
                screen.blit(text, (555, 420))
                f2 = pygame.font.SysFont('arial', 14)
                text = f2.render("about our situation?", False, (0, 0, 0))
                screen.blit(text, (555, 435))
        elif t >= 500 and t < 600:
            screen.blit(mag_left, (mag_cord_x, mag_cord_y))
            screen.blit(dialog_left, (100, 400))
            if language == 'rus':
                f2 = pygame.font.SysFont('arial', 14)
                text = f2.render("Да.", False, (0, 0, 0))
                screen.blit(text, (105, 405))
            elif language == 'eng':
                f2 = pygame.font.SysFont('arial', 14)
                text = f2.render("Yes.", False, (0, 0, 0))
                screen.blit(text, (105, 405))
        elif t >= 600 and t < 700:
            screen.blit(mag_left, (mag_cord_x, mag_cord_y))
            screen.blit(dialog_right, (550, 400))
            if language == 'rus':
                f2 = pygame.font.SysFont('arial', 14)
                text = f2.render("Я помогу тебе.", False,
                                 (0, 0, 0))
                screen.blit(text, (555, 405))
                f2 = pygame.font.SysFont('arial', 14)
                text = f2.render("Сим. Салабим.", False,
                                 (0, 0, 0))
                screen.blit(text, (555, 420))
            elif language == 'eng':
                f2 = pygame.font.SysFont('arial', 14)
                text = f2.render("I will help you.", False,
                                 (0, 0, 0))
                screen.blit(text, (555, 405))
                f2 = pygame.font.SysFont('arial', 14)
                text = f2.render("Sim. Salabim.", False,
                                 (0, 0, 0))
                screen.blit(text, (555, 420))
        elif t >= 700 and t < 800:
            screen.blit(mag_left, (mag_cord_x, mag_cord_y))
            screen.blit(dialog_right, (550, 400))
            if language == 'rus':
                f2 = pygame.font.SysFont('arial', 14)
                text = f2.render("Теперь ты можешь извергать",
                                 False,
                                 (0, 0, 0))
                screen.blit(text, (555, 405))
                f2 = pygame.font.SysFont('arial', 14)
                text = f2.render("огненные шары. Они тебе",
                                 False,
                                 (0, 0, 0))
                screen.blit(text, (555, 420))
                f2 = pygame.font.SysFont('arial', 14)
                text = f2.render("помогут в битве с чудовищем.",
                                 False,
                                 (0, 0, 0))
                screen.blit(text, (555, 435))
            elif language == 'eng':
                f2 = pygame.font.SysFont('arial', 14)
                text = f2.render("Now you can spew",
                                 False,
                                 (0, 0, 0))
                screen.blit(text, (555, 405))
                f2 = pygame.font.SysFont('arial', 14)
                text = f2.render("fireballs. They will help you",
                                 False,
                                 (0, 0, 0))
                screen.blit(text, (555, 420))
                f2 = pygame.font.SysFont('arial', 14)
                text = f2.render("in the battle with the monster.",
                                 False,
                                 (0, 0, 0))
                screen.blit(text, (555, 435))
        elif t >= 800 and t < 900:
            screen.blit(mag_left, (mag_cord_x, mag_cord_y))
            screen.blit(dialog_left, (100, 400))
            if language == 'rus':
                f2 = pygame.font.SysFont('arial', 14)
                text = f2.render("Я помогу вам.", False, (0, 0, 0))
                screen.blit(text, (105, 405))
                f2 = pygame.font.SysFont('arial', 14)
                text = f2.render("До свидания.", False, (0, 0, 0))
                screen.blit(text, (105, 420))
            elif language == 'eng':
                f2 = pygame.font.SysFont('arial', 14)
                text = f2.render("Thanks. I will try to help.", False, (0, 0, 0))
                screen.blit(text, (105, 405))
                f2 = pygame.font.SysFont('arial', 14)
                text = f2.render("Goodbye.", False, (0, 0, 0))
                screen.blit(text, (105, 420))
        elif t >= 900 and t < 1130:
            # t += 1
            mag_cord_x += 1
            screen.blit(mag_right, (mag_cord_x, mag_cord_y))
        elif t >= 1130:
            running = False
            origin_dino(screen, color, score, HI, birthday_code, language, keys)

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
        HI_coard_y = 500
        screen.blit(HI_img, (870, 500))
        for i in range(1, len(HI_str) + 1):
            score_out.insert(0, HI_str[len(HI_str) - i])
        while len(score_out) != 5:
            score_out.insert(0, '0')
        HI_coard_x = 970
        for i in range(len(score_out)):
            screen.blit(nums_dict[score_out[i]], (HI_coard_x, HI_coard_y))
            HI_coard_x += 30
        pygame.display.flip()


if __name__ == '__main__':
    origin_dino(screen, color, score, HI, birthday_code, language, keys)

    pygame.quit()
