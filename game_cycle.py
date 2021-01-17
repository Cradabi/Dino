# Анимация бегущего дино


import pygame
from dino import Dino
from bird import Bird
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
    rerun_img = pygame.image.load('imgs/rerun.png')
    rerun_img.set_colorkey('white')
    game_over_img = pygame.image.load('imgs/game_over.png')
    game_over_img.set_colorkey('white')
    HI_img = pygame.image.load('imgs/HI.png')
    HI_img.set_colorkey('white')
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    screen.fill(color)
    clock = pygame.time.Clock()
    t_d = 0
    t_b = 0
    time = 0
    d = Dino()
    b = Bird()
    status_dino = 'run'
    fire_status = False
    fire_cor_x = 355
    fire_cor_y = 230
    water_status = False
    water_cor_x = 355
    water_cor_y = 230
    jump_status = 0
    road_cord_x1 = 0
    road_cord_x2 = 2398
    running = True
    road_v = 1.0
    score = 0
    num_s = ''
    score_t = 0
    score_cord = 0
    score_str = str(score)
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
                    fire_cor_x = 380
                elif not fire_status:
                    fire_cor_x = 355
                    fire_cor_y = 230
                if status_dino == 'sit':
                    water_cor_y = 264
                    water_cor_x = 380
                elif not water_status:
                    water_cor_x = 355
                    water_cor_y = 230
            if event.type == pygame.KEYDOWN:
                if event.key == 115:  # if event.unicode == 's':
                    status_dino = 'sit'
                    d.y += 34
                    d.sit_anim(screen)  # time = -1
                elif event.key == 119:  # elif event.unicode == 'w':
                    if jump_status == 0:
                        jump_status = 1
            if event.type == pygame.KEYUP:
                if event.key == 115:  # if event.unicode == 's':
                    status_dino = 'run'
                    d.y -= 34
                    d.run_anim(screen)  # time = -1

        time += 1
        if time % 10 == 0:
            screen.fill('black')
            if status_dino == 'run':
                d.run_anim(screen)
            elif status_dino == 'sit':
                d.sit_anim(screen)
            b.fly_anim(screen)

        screen.fill('black')

        screen.blit(d.out, (d.x, d.y))
        screen.blit(b.out, (b.x, b.y))

        screen.blit(cloud, (200, 100))
        screen.blit(moon, (400, 80))
        screen.blit(star, (500, 130))
        screen.blit(night_sun, (30, 100))
        if score < 10:
            screen.blit(num_0, (570, 50))
            screen.blit(num_0, (600, 50))
            screen.blit(num_0, (630, 50))
            screen.blit(num_0, (660, 50))
            if score == 0:
                screen.blit(num_0, (690, 50))
            elif score == 1:
                screen.blit(num_1, (690, 50))
            elif score == 2:
                screen.blit(num_2, (690, 50))
            elif score == 3:
                screen.blit(num_3, (690, 50))
            elif score == 4:
                screen.blit(num_4, (690, 50))
            elif score == 5:
                screen.blit(num_5, (690, 50))
            elif score == 6:
                screen.blit(num_6, (690, 50))
            elif score == 7:
                screen.blit(num_7, (690, 50))
            elif score == 8:
                screen.blit(num_8, (690, 50))
            elif score == 9:
                screen.blit(num_9, (690, 50))
        elif score < 100:
            screen.blit(num_0, (570, 50))
            screen.blit(num_0, (600, 50))
            screen.blit(num_0, (630, 50))
            score_cord = 630
            for i in range(2):
                score_cord += 30
                if score_str[i] == '0':
                    screen.blit(num_0, (score_cord, 50))
                elif score_str[i] == '1':
                    screen.blit(num_1, (score_cord, 50))
                elif score_str[i] == '2':
                    screen.blit(num_2, (score_cord, 50))
                elif score_str[i] == '3':
                    screen.blit(num_3, (score_cord, 50))
                elif score_str[i] == '4':
                    screen.blit(num_4, (score_cord, 50))
                elif score_str[i] == '5':
                    screen.blit(num_5, (score_cord, 50))
                elif score_str[i] == '6':
                    screen.blit(num_6, (score_cord, 50))
                elif score_str[i] == '7':
                    screen.blit(num_7, (score_cord, 50))
                elif score_str[i] == '8':
                    screen.blit(num_8, (score_cord, 50))
                elif score_str[i] == '9':
                    screen.blit(num_9, (score_cord, 50))
        elif score < 1000:
            screen.blit(num_0, (570, 50))
            screen.blit(num_0, (600, 50))
            score_cord = 600
            for i in range(3):
                score_cord += 30
                if score_str[i] == '0':
                    screen.blit(num_0, (score_cord, 50))
                elif score_str[i] == '1':
                    screen.blit(num_1, (score_cord, 50))
                elif score_str[i] == '2':
                    screen.blit(num_2, (score_cord, 50))
                elif score_str[i] == '3':
                    screen.blit(num_3, (score_cord, 50))
                elif score_str[i] == '4':
                    screen.blit(num_4, (score_cord, 50))
                elif score_str[i] == '5':
                    screen.blit(num_5, (score_cord, 50))
                elif score_str[i] == '6':
                    screen.blit(num_6, (score_cord, 50))
                elif score_str[i] == '7':
                    screen.blit(num_7, (score_cord, 50))
                elif score_str[i] == '8':
                    screen.blit(num_8, (score_cord, 50))
                elif score_str[i] == '9':
                    screen.blit(num_9, (score_cord, 50))
        elif score < 10000:
            screen.blit(num_0, (570, 50))
            score_cord = 570
            for i in range(4):
                score_cord += 30
                if score_str[i] == '0':
                    screen.blit(num_0, (score_cord, 50))
                elif score_str[i] == '1':
                    screen.blit(num_1, (score_cord, 50))
                elif score_str[i] == '2':
                    screen.blit(num_2, (score_cord, 50))
                elif score_str[i] == '3':
                    screen.blit(num_3, (score_cord, 50))
                elif score_str[i] == '4':
                    screen.blit(num_4, (score_cord, 50))
                elif score_str[i] == '5':
                    screen.blit(num_5, (score_cord, 50))
                elif score_str[i] == '6':
                    screen.blit(num_6, (score_cord, 50))
                elif score_str[i] == '7':
                    screen.blit(num_7, (score_cord, 50))
                elif score_str[i] == '8':
                    screen.blit(num_8, (score_cord, 50))
                elif score_str[i] == '9':
                    screen.blit(num_9, (score_cord, 50))
        elif score < 100000:
            score_cord = 540
            for i in range(5):
                score_cord += 30
                if score_str[i] == '0':
                    screen.blit(num_0, (score_cord, 50))
                elif score_str[i] == '1':
                    screen.blit(num_1, (score_cord, 50))
                elif score_str[i] == '2':
                    screen.blit(num_2, (score_cord, 50))
                elif score_str[i] == '3':
                    screen.blit(num_3, (score_cord, 50))
                elif score_str[i] == '4':
                    screen.blit(num_4, (score_cord, 50))
                elif score_str[i] == '5':
                    screen.blit(num_5, (score_cord, 50))
                elif score_str[i] == '6':
                    screen.blit(num_6, (score_cord, 50))
                elif score_str[i] == '7':
                    screen.blit(num_7, (score_cord, 50))
                elif score_str[i] == '8':
                    screen.blit(num_8, (score_cord, 50))
                elif score_str[i] == '9':
                    screen.blit(num_9, (score_cord, 50))
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
            road_cord_x1 -= int(10 * road_v)
            road_cord_x2 -= int(10 * road_v)
        if road_v < 1.7:
            road_v += 0.00016

        if fire_status:
            pygame.draw.circle(screen, (245, 109, 12), (fire_cor_x, fire_cor_y), 20)
            fire_cor_x += 10
        if fire_cor_x > 800:
            fire_cor_x = 355
            fire_status = False

        if water_status:
            pygame.draw.circle(screen, (0, 128, 255), (water_cor_x, water_cor_y), 20)
            water_cor_x += 10
        if water_cor_x > 800:
            water_cor_x = 355
            water_status = False

        # отрисовка и изменение свойств объектов
        # ...

        # обновление экрана
        pygame.display.flip()

    pygame.quit()
