# Анимация бегущего дино

import pygame
from random import randint
from dino import Dino
from bird import Bird
from cactus import Cactus
import sqlite3

FPS = 60
color = 'black'

if __name__ == '__main__':
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
    dino1 = pygame.image.load('imgs/dino1.png')
    dino1.set_colorkey('white')
    cacti = [small_cactus1, small_cactus2, small_cactus3, small_cactus4, small_cactus5]
    all_cacti = pygame.sprite.Group()

    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    screen.fill(color)
    clock = pygame.time.Clock()
    d_y = 210
    d_x = 100
    d = Dino(d_x, d_y)
    birds = pygame.sprite.Group()
    status_dino = 'run'
    fire_status = False
    fire_cor_x = d.x + 89
    fire_cor_y = 230
    water_status = False
    water_cor_x = d.x + 89
    water_cor_y = 230
    jump_status = 0
    road_cord_x1 = 0
    road_cord_x2 = 2398
    running = True
    road_v = 1.0
    road_speed = 10
    score = 0
    num_s = ''
    score_t = 0
    score_cord_x = 570
    score_cord_y = 50
    rand_time = -30
    now_barier = 'cactus'
    next_barier = 'cactus'
    last_cactus = True
    score_str = str(score)
    jump_time = 0
    time = -1
    con = sqlite3.connect('HI.db')
    cur = con.cursor()
    HI_s = cur.execute(
        """Select HI From HI""").fetchall()
    HI = int(HI_s[0][0])
    HI_str = str(HI)
    HI_t = 0
    HI_coard_x = 530
    HI_coard_y = 500
    while running:

        clock.tick(FPS)

        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    fire_status = True
                if event.button == 3:
                    water_status = True
                if status_dino == 'sit':
                    fire_cor_y = 264
                    fire_cor_x = d.x + 120
                elif not fire_status:
                    fire_cor_x = d.x + 89
                    fire_cor_y = 230
                if status_dino == 'sit':
                    water_cor_y = 264
                    water_cor_x = d.x + 120
                elif not water_status:
                    water_cor_x = d.x + 89
                    water_cor_y = 230
            if event.type == pygame.KEYDOWN:
                if event.key == 115:  # if event.unicode == 's':
                    status_dino = 'sit'
                    d.y = d_y + 34  # d.y += 34
                    if not jump_status:
                        d.sit_anim(screen)
                elif event.key == 119:  # elif event.unicode == 'w':
                    if jump_status == 0:
                        jump_status = 1
            if event.type == pygame.KEYUP:
                if event.key == 115:  # if event.unicode == 's':
                    status_dino = 'run'
                    d.y = d_y  # d.y -= 34
                    if not jump_status:
                        d.run_anim(screen)

        time += 1
        if time % 10 == 0:
            screen.fill('black')
            if jump_status == 0 and status_dino == 'run':
                d.run_anim(screen)
            elif jump_status == 0 and status_dino == 'sit':
                d.sit_anim(screen)
            elif jump_status != 0 and status_dino == 'sit':
                if d.y <= 180:
                    d.y += 20
                else:
                    d.y = 200
                    jump_status = 0

        if jump_status == 1:
            jump_time += 1
            if jump_time % 15 != 0:
                d.y -= 10
                d.out = dino1
                # screen.blit(dino1, (d_x, d_y))
            else:
                jump_status = 2
                jump_time = 0
        elif jump_status == 2:
            jump_time += 1
            if jump_time % 3 != 0:
                d.out = dino1
                # screen.blit(dino1, (d_x, d_y))
            else:
                jump_status = 3
                jump_time = 0
        elif jump_status == 3:
            jump_time += 1
            if jump_time % 15 != 0:
                d.y += 10
                d.out = dino1
                # screen.blit(dino1, (d_x, d_y))
            else:
                jump_status = 0
                jump_time = 0
                if status_dino == 'run':
                    d.run_anim(screen)
                elif status_dino == 'sit':
                    d.sit_anim(screen)

            # b.fly_anim(screen)
        if (time % (70 + rand_time) == 0 and next_barier == 'cactus' and last_cactus) or (
                next_barier == 'cactus' and not last_cactus):
            last_cactus = True
            # TODO сделать нормальное время между появлениями кактусов(препятсвий)
            Cactus(800, 226, cacti[randint(0, 4)], all_cacti)
            now_barier = 'cactus'
            time = time % 10
            rand_time = randint(-10, 40)
        elif (time % (70 + rand_time) == 0 and next_barier == 'bird' and last_cactus) or (
                next_barier == 'bird' and not last_cactus):
            last_cactus = False
            Bird(800, 150, birds)
            now_barier = 'bird'
            next_barier = ''

        screen.fill('black')

        q1 = d.collide_check(all_cacti, Cactus, score)
        q2 = d.collide_check(birds, Bird, score)
        if q1 or q2:
            d.die(score)
            running = False

        # screen.blit(d.out, (d.x, d.y))
        d.update(screen)

        all_cacti.update(road_v * road_speed)
        all_cacti.draw(screen)
        if now_barier == 'cactus':
            for cactus in all_cacti:
                if cactus.rect.x < -34:  # только если маленький кактус
                    cactus.kill()
                    if score > 50:
                        choose = randint(1, 4)  # TODO похоже что это нагружает прогу, надо что то сделать
                        if choose == 4:
                            next_barier = 'bird'
                        else:
                            next_barier = 'cactus'
        birds.update(road_v * road_speed, time)
        birds.draw(screen)
        if now_barier == 'bird':

            for bird in birds:
                if bird.rect.x < -94:
                    bird.kill()
            if not birds.spritedict:
                choose = randint(1, 4)  # TODO похоже что это нагружает прогу, надо что то сделать
                if choose == 4:
                    next_barier = 'bird'
                else:
                    next_barier = 'cactus'

        screen.blit(cloud, (200, 100))
        screen.blit(moon, (400, 80))
        screen.blit(star, (500, 130))
        screen.blit(night_sun, (30, 100))

        score_out = []
        for i in range(1, len(score_str) + 1):
            score_out.insert(0, score_str[len(score_str) - i])
        while len(score_out) != 5:
            score_out.insert(0, '0')
        score_cord_x = 570
        for i in range(len(score_out)):
            screen.blit(nums_dict[score_out[i]], (score_cord_x, score_cord_y))
            score_cord_x += 30

        score_out = []
        screen.blit(HI_img, (470, 500))
        for i in range(1, len(HI_str) + 1):
            score_out.insert(0, HI_str[len(HI_str) - i])
        while len(score_out) != 5:
            score_out.insert(0, '0')
        HI_cord_x = 570
        for i in range(len(score_out)):
            screen.blit(nums_dict[score_out[i]], (HI_cord_x, HI_coard_y))
            HI_cord_x += 30

        if score_t % 3 == 0:
            score += 1
            score_str = str(score)
        score_t += 1

        screen.blit(road1, (road_cord_x1, 270))
        screen.blit(road2, (road_cord_x2, 270))
        if road_cord_x2 <= -1400:
            road_cord_x1 = 0
            road_cord_x2 = 2398
        else:
            road_cord_x1 -= int(road_speed * road_v)
            road_cord_x2 -= int(road_speed * road_v)
        if road_v < 1.7:
            road_v += 0.00016

        if fire_status:
            d.fare_ball_anim(screen, fire_cor_x, fire_cor_y)
            fire_cor_x += 10
        if fire_cor_x > 800:
            fire_cor_x = d.x + 89
            fire_status = False

        if water_status:
            d.watter_ball_anim(screen, water_cor_x, water_cor_y)
            water_cor_x += 10
        if water_cor_x > 800:
            water_cor_x = d.x + 89
            water_status = False

        # отрисовка и изменение свойств объектов
        # ...

        # обновление экрана
        pygame.display.flip()

    run = True
    while run:
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()
