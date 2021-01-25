# ГЛАВНЫЙ ФАЙЛ


from game_cycle import origin_dino
import string
import pygame
import os
import sqlite3

pygame.init()

FPS = 60
WIDTH = 1200
HEIGHT = 800
DINO_COLOR = (83, 83, 83)
color = 'white'
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
pygame.mouse.set_cursor(*pygame.cursors.tri_left)

# если надо до цикла отобразить объекты на экране
screen.fill('black')

# главный цикл
while True:

    # задержка
    clock.tick(FPS)

    # цикл обработки событий
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            quit()
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_ESCAPE:
                quit()

    # --------
    # изменение объектов и многое др.
    # --------
    screen.fill('black')

    text1 = f1.render('Начать игру', True, 'white')
    screen.blit(text1, (100, 150))
    text2 = f1.render('Настройки', True, 'white')
    screen.blit(text2, (110, 300))

    t += 1

    pressed = pygame.mouse.get_pressed()
    if pressed[0]:  # обработка нажатий левой кнопки мыши
        x1, y1 = pygame.mouse.get_pos()
        if 190 <= x1 <= 500 and 190 <= y1 <= 260:
            pygame.mouse.set_visible(True)
            origin_dino(screen, color, score, HI)  # запуск игры
        elif 200 <= x1 <= 480 and 340 <= y1 <= 410:
            pygame.mouse.set_visible(True)

    # обновление экрана
    pygame.display.update()
