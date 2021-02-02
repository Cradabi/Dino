# ГЛАВНЫЙ ФАЙЛ


from game_cycle import origin_dino
from settings import sets
import string
import pygame
import os
import sqlite3

pygame.init()

FPS = 60
WIDTH = 1200
HEIGHT = 800
DINO_COLOR = (83, 83, 83)

color = (255, 255, 255)
size = width, height = WIDTH, HEIGHT
screen = pygame.display.set_mode(size)
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
f2 = pygame.font.Font(None, 18)
t = 0
water_number = 0
fire_number = 5
money = 100
birthday_code = False
pygame.mouse.set_cursor(*pygame.cursors.tri_left)
language = 'rus'
keys = [119, 115, 100, 97]  # 1-вверх, 2-вниз, 3-синий шар, 4-красный шар

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
                    quit()

        # --------
        # изменение объектов и многое др.
        # --------
        screen.fill('black')

        text1 = f1.render('Начать игру', True, 'white')
        screen.blit(text1, (100, 150))
        text2 = f1.render('Настройки', True, 'white')
        screen.blit(text2, (110, 300))

        # t += 1

        pressed = pygame.mouse.get_pressed()
        if pressed[0]:  # обработка нажатий левой кнопки мыши
            x1, y1 = pygame.mouse.get_pos()
            if 90 <= x1 <= 360 and 140 <= y1 <= 210:
                pygame.mouse.set_visible(True)
                origin_dino(screen, color, score, HI, birthday_code, language, keys, water_number,
                            fire_number, money)  # запуск игры
            elif 100 <= x1 <= 350 and 290 <= y1 <= 360:
                pygame.mouse.set_visible(True)
                birthday_code, score, language, keys = sets(screen, score, language, keys)  # настройки

        # обновление экрана
        pygame.display.update()
