# ГЛАВНЫЙ ФАЙЛ


from game_cycle import origin_dino, game_cycle
from settings import sets
from button import Button
import pygame
import os
import subprocess
import sqlite3

pygame.init()

FPS = 60
WIDTH = 1200
HEIGHT = 800
DINO_COLOR = (83, 83, 83)

color = (255, 255, 255)
size = width, height = WIDTH, HEIGHT
screen = pygame.display.set_mode(size)
cap = pygame.image.load('imgs/caption/caption.png')
cap.set_colorkey('white')
cap = pygame.transform.scale(cap, (32, 32))
pygame.display.set_caption('Dino')
pygame.display.set_icon(cap)
screen.fill(color)
score = 0
con = sqlite3.connect('HI.db')
cur = con.cursor()
HI_s = cur.execute(
    """Select HI From HI""").fetchall()
HI = int(HI_s[0][0])
clock = pygame.time.Clock()
f1 = pygame.font.Font(None, 60)
f1.set_italic(True)
f2 = pygame.font.Font(None, 32)
t = 0
water_number = 0
fire_number = 0
money = 0
birthday_code = False
pygame.mouse.set_cursor(*pygame.cursors.tri_left)
language = 'rus'
keys = [119, 115, 100, 97]  # 1-вверх, 2-вниз, 3-синий шар, 4-красный шар

menu_color = (0, 0, 0)
text_color = (255, 255, 255)

moon_x = 400
star_x1 = 300
star_x2 = 150
star_x3 = 900
star_x4 = 450
star_x5 = 271
star_x6 = 800
star_x7 = 615
star_x8 = 361
star_x9 = 18
star_x10 = 501
sun_x = 30
cloud_x1 = 400
cloud_x2 = 900
cloud_x3 = 11
cloud_x4 = 315
cloud_x5 = 101
cloud_x6 = 212
cloud_x7 = 957
cloud_x8 = 512
cloud_x9 = 845
cloud_x10 = 678
moon_list = [moon_x, star_x1, star_x2, star_x3, star_x4, star_x5, star_x6, star_x7, star_x8, star_x9, star_x10]
sun_list = [cloud_x1, cloud_x2, cloud_x3, cloud_x4, cloud_x5, cloud_x6, cloud_x7, cloud_x8, cloud_x9, cloud_x10, sun_x]

# отложено до более мирных времен
# image_tank1 = pygame.image.load('imgs/tank1.png')
# image_tank1 = pygame.transform.scale(image_tank1, (200, 152))
# image_tank1.set_colorkey('white')
# image_tank2 = pygame.image.load('imgs/tank2.png')
# image_tank2 = pygame.transform.scale(image_tank2, (200, 152))
# image_tank2.set_colorkey('white')
print1 = True

image_dino1 = pygame.image.load('imgs/dino_bd_2.png')
image_dino1 = pygame.transform.scale(image_dino1, (90, 132))
image_dino1.set_colorkey('white')
image_dino2 = pygame.image.load('imgs/dino_bd_3.png')
image_dino2 = pygame.transform.scale(image_dino2, (90, 132))
image_dino2.set_colorkey('white')

filename = 'sounds/mario_sound.mp3'
audio_turn_off = True
pygame.mixer.music.load(filename)
pygame.mixer.music.set_volume(0.5)
if not audio_turn_off:
    pygame.mixer.music.play(-1)

if language == 'rus':
    text1 = f1.render('Начать игру', True, text_color)
    text2 = f1.render('Настройки', True, text_color)
elif language == 'eng':
    text1 = f1.render('Play', True, text_color)
    text2 = f1.render('Settings', True, text_color)
play_button = Button(100, 150, text1, text_color)
settings_button = Button(110, 300, text2, text_color)

road1 = pygame.image.load('imgs/road.png')
road1.set_colorkey('white')
road2 = pygame.image.load('imgs/road.png')
road2.set_colorkey('white')
road_cord_x1 = 0
road_cord_x2 = 2398
road_speed = 10

codes_open = False

menu = True

# если надо до цикла отобразить объекты на экране
screen.fill('black')

# главный цикл
if __name__ == '__main__':
    while True:

        # задержка
        clock.tick(FPS)

        # цикл обработки событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if not menu:
                        menu = True
                    else:
                        quit()

        # --------
        # изменение объектов и многое др.
        # --------
        if menu:
            t += 1
            if t % 10 == 0:
                print1 = not print1

            screen.fill(menu_color)

            # двигает дорожку:
            screen.blit(road1, (road_cord_x1, 450))
            screen.blit(road2, (road_cord_x2, 450))
            if road_cord_x2 <= 0:
                road_cord_x1 = 0
                road_cord_x2 = 2398
            else:
                road_cord_x1 -= road_speed
                road_cord_x2 -= road_speed

            if print1:
                # screen.blit(image_tank1, (570, 315))
                screen.blit(image_dino1, (600, 335))
                pass
            else:
                # screen.blit(image_tank2, (570, 316))
                screen.blit(image_dino2, (600, 335))
                pass

            play_button.draw(screen)
            settings_button.draw(screen)

            if play_button.mouse_check(pygame.mouse.get_pos()):
                play_button.color = 'red'
            else:
                play_button.color = text_color

            if settings_button.mouse_check(pygame.mouse.get_pos()):
                settings_button.color = 'red'
            else:
                settings_button.color = text_color

            pressed = pygame.mouse.get_pressed()
            if pressed[0]:  # обработка нажатий левой кнопки мыши
                x1, y1 = pygame.mouse.get_pos()
                if play_button.mouse_check((x1, y1)):
                    pygame.mouse.set_visible(True)
                    # pygame.mixer.music.stop()
                    # game_cycle(screen, color, score, HI, birthday_code, language, keys, water_number,
                    #           fire_number, money, moon_list, sun_list, audio_turn_off)  # запуск игры
                    menu = False

                    back_surf = pygame.Surface((WIDTH, HEIGHT))
                    back_surf.set_alpha(100)
                    back_surf.fill('black')
                    screen.blit(back_surf, (0, 0))

                    surf = pygame.Surface((400, 200))
                    surf.fill('white')
                    surf.set_alpha(255)
                    screen.blit(surf, (400, 200))

                    if language == 'rus':
                        text_plot = f2.render('Сюжет', True, (0, 0, 0))
                        plot_btn = Button(440, 280, text_plot, 'black')
                        text_inf = f2.render('Бесконечный режим', True, (0, 0, 0))
                        inf_btn = Button(540, 280, text_inf, 'black')
                    elif language == 'eng':
                        text_plot = f2.render('Story mode', True, (0, 0, 0))
                        plot_btn = Button(440, 280, text_plot, 'black')
                        text_inf = f2.render('Endless mode', True, (0, 0, 0))
                        inf_btn = Button(600, 280, text_inf, 'black')

                elif 635 <= x1 <= 670 and 395 <= y1 <= 405 and not codes_open:
                    codes_open = True
                    subprocess.Popen(r'explorer /open, secrets\more_secrets\codes.txt')
                elif settings_button.mouse_check((x1, y1)):
                    pygame.mouse.set_visible(True)
                    birthday_code, score, language, keys, money, \
                    fire_number, water_number, audio_turn_off = sets(screen, score, language, keys, money,
                                                                     fire_number, water_number, False,
                                                                     audio_turn_off)  # настройки
                    if language == 'rus':
                        text1 = f1.render('Начать игру', True, text_color)
                        text2 = f1.render('Настройки', True, text_color)
                    elif language == 'eng':
                        text1 = f1.render('Play', True, text_color)
                        text2 = f1.render('Settings', True, text_color)
                    play_button = Button(100, 150, text1, text_color)
                    settings_button = Button(110, 300, text2, text_color)
        else:
            plot_btn.draw(screen)

            if plot_btn.mouse_check(pygame.mouse.get_pos()):
                plot_btn.color = 'red'
            else:
                plot_btn.color = 'black'

            inf_btn.draw(screen)

            if inf_btn.mouse_check(pygame.mouse.get_pos()):
                inf_btn.color = 'red'
            else:
                inf_btn.color = 'black'

            pressed = pygame.mouse.get_pressed()
            if pressed[0]:  # обработка нажатий левой кнопки мыши
                x1, y1 = pygame.mouse.get_pos()
                if plot_btn.mouse_check((x1, y1)):
                    game_cycle(screen, color, score, HI, birthday_code, language, keys, water_number,
                               fire_number, money, moon_list, sun_list, audio_turn_off, False)  # запуск игры
                    menu = True
                elif inf_btn.mouse_check((x1, y1)):
                    game_cycle(screen, color, score, HI, birthday_code, language, keys, water_number,
                               fire_number, money, moon_list, sun_list, audio_turn_off, True)  # запуск игры
                    menu = True

        # обновление экрана
        pygame.display.update()
