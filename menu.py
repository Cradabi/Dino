# ГЛАВНЫЙ ФАЙЛ


from game_cycle import origin_dino
from settings import sets
import string
import pygame
import os
import sqlite3


class Button:
    def __init__(self, x, y, text, text_color):
        self.x = x - 10
        self.y = y - 10
        self.w = text.get_width() + 20
        self.h = text.get_height() + 20
        self.border_width = 3
        self.color = text_color
        self.text = text

    def draw(self, surf):
        pygame.draw.rect(surf, self.color, (self.x, self.y, self.w, self.h), self.border_width)
        screen.blit(self.text, (self.x + 10, self.y + 10))

    def mouse_check(self, cort):
        x, y = cort
        if self.x <= x <= self.x + self.w and self.y <= y <= self.y + self.h:
            return True
        return False


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
fire_number = 0
money = 0
birthday_code = False
pygame.mouse.set_cursor(*pygame.cursors.tri_left)
language = 'rus'
keys = [119, 115, 100, 97]  # 1-вверх, 2-вниз, 3-синий шар, 4-красный шар

menu_color = (0, 0, 0)
text_color = (255, 255, 255)

image_tank1 = pygame.image.load('imgs/tank1.png')
image_tank1.set_colorkey('white')
image_tank2 = pygame.image.load('imgs/tank2.png')
image_tank2.set_colorkey('white')

if language == 'rus':
    text1 = f1.render('Начать игру', True, text_color)
    text2 = f1.render('Настройки', True, text_color)
elif language == 'eng':
    text1 = f1.render('Play', True, text_color)
    text2 = f1.render('Settings', True, text_color)
play_button = Button(100, 150, text1, text_color)
settings_button = Button(110, 300, text2, text_color)

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
        screen.fill(menu_color)

        play_button.draw(screen)
        settings_button.draw(screen)

        # t += 1
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
                origin_dino(screen, color, score, HI, birthday_code, language, keys, water_number,
                            fire_number, money)  # запуск игры
            elif settings_button.mouse_check((x1, y1)):
                pygame.mouse.set_visible(True)
                birthday_code, score, language, keys = sets(screen, score, language, keys)  # настройки
                if language == 'rus':
                    text1 = f1.render('Начать игру', True, text_color)
                    text2 = f1.render('Настройки', True, text_color)
                elif language == 'eng':
                    text1 = f1.render('Play', True, text_color)
                    text2 = f1.render('Settings', True, text_color)
                play_button = Button(100, 150, text1, text_color)
                settings_button = Button(110, 300, text2, text_color)

        # обновление экрана
        pygame.display.update()
