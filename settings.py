from time import sleep
from button import Button
import pygame
import easygui

FPS = 60
WIDTH = 1200
HEIGHT = 800

BLACK = (0, 0, 0)


# filename = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "files (*.wav *.mp3 *.ogg)")
# input_file = easygui.fileopenbox(filetypes=['*.wav', '*.mp3', '*.ogg'])

def sets(screen, score, language, keys, is_from_game_cycle):
    clock = pygame.time.Clock()

    time = 0

    up_key = keys[0]
    down_key = keys[1]
    blue_ball_key = keys[2]
    red_ball_key = keys[3]

    back_surf = pygame.Surface((WIDTH, HEIGHT))
    back_surf.set_alpha(130)
    back_surf.fill('black')
    screen.blit(back_surf, (0, 0))

    surf = pygame.Surface((800, 700))
    surf.fill('white')
    surf.set_alpha(255)
    screen.blit(surf, (200, 25))

    button_color = (133, 133, 133)

    birth_day_code = False

    font = pygame.font.Font(None, 32)
    standart_width = 600
    standart_height = 32
    input_box = pygame.Rect(250, 75, standart_width, standart_height)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    f1 = pygame.font.Font(None, 32)
    text1 = 'код не найден'
    text1_x = 510
    text1_y = 120
    text1_print = False
    text1_surf = f1.render(text1, True, BLACK)

    f2 = pygame.font.Font(None, 40)
    text_lang1 = 'Язык'
    text_lang_rus = 'Русский'
    text_lang_eng = 'English'
    if language == 'rus':
        text_lang_rus_surf = f2.render(text_lang_rus, True, 'blue')
        text_lang_eng_surf = f2.render(text_lang_eng, True, BLACK)
        text_lang1 = 'Язык'
    elif language == 'eng':
        text_lang_rus_surf = f2.render(text_lang_rus, True, BLACK)
        text_lang_eng_surf = f2.render(text_lang_eng, True, 'blue')
        text_lang1 = 'Language'
    text_lang1_surf = f2.render(text_lang1, True, BLACK)

    control_settings = False
    control_text1 = 'Управление'
    control_text1_x = 490
    control_text1_y = 170
    control_text1_w = 200
    control_text1_h = 35
    f3 = pygame.font.Font(None, 48)
    if language == 'rus':
        control_text1 = 'Управление'
        control_text1_x = 490
        control_text1_y = 170
        control_text1_w = 200
        control_text1_h = 35
    elif language == 'eng':
        control_text1 = 'Control'
        control_text1_x = 530
        control_text1_y = 170
        control_text1_w = 125
        control_text1_h = 35
    control_text1_surf = f3.render(control_text1, True, BLACK)

    f4 = pygame.font.Font(None, 60)
    control_text2_surf = f4.render(control_text1, True, BLACK)
    control_text_upkey = 'Прыжок'
    control_text_downkey = 'Присядка'
    control_text_blueballkey = 'Стрельба водяным шаром'
    control_text_redballkey = 'Стрельба огненным шаром'
    control_text_upkey_x = 250
    control_text_upkey_y = 150
    control_text_downkey_x = 250
    control_text_downkey_y = 250
    control_text_blueballkey_x = 250
    control_text_blueballkey_y = 350
    control_text_redballkey_x = 250
    control_text_redballkey_y = 450
    if language == 'rus':
        control_text_upkey = 'Прыжок'
        control_text_downkey = 'Присядка'
        control_text_blueballkey = 'Стрельба водяным шаром'
        control_text_redballkey = 'Стрельба огненным шаром'
    elif language == 'eng':
        control_text_upkey = 'Jump'
        control_text_downkey = 'Sit'
        control_text_blueballkey = 'Water ball shooting'
        control_text_redballkey = 'Fire ball shooting'

    control_upkey_x = 900
    control_upkey_y = 150
    control_downkey_x = 900
    control_downkey_y = 250
    control_blueballkey_x = 900
    control_blueballkey_y = 350
    control_redballkey_x = 900
    control_redballkey_y = 450
    control_upkey = chr(up_key)
    control_downkey = chr(down_key)
    control_blueballkey = chr(blue_ball_key)
    control_redballkey = chr(red_ball_key)
    control_upkey_surf = f2.render(control_upkey, True, BLACK)
    control_downkey_surf = f2.render(control_downkey, True, BLACK)
    control_blueballkey_surf = f2.render(control_blueballkey, True, BLACK)
    control_redballkey_surf = f2.render(control_redballkey, True, BLACK)

    upkey_choose = False
    downkey_choose = False
    blueballkey_choose = False
    redballkey_choose = False
    key_choose = False

    control_text_upkey_surf = f2.render(control_text_upkey, True, BLACK)
    control_text_downkey_surf = f2.render(control_text_downkey, True, BLACK)
    control_text_blueballkey_surf = f2.render(control_text_blueballkey, True, BLACK)
    control_text_redballkey_surf = f2.render(control_text_redballkey, True, BLACK)

    choose_box = False
    choose_box_x = 0
    choose_box_y = 0

    warning_text = 'Произошла ошибка'
    warning_text_x = 470
    warning_text_y = 550
    if language == 'rus':
        warning_text = 'Произошла ошибка'
        warning_text_x = 470
        warning_text_y = 550
    elif language == 'eng':
        warning_text = 'Error'
        warning_text_x = 560
        warning_text_y = 550
    warning_text_surf = f2.render(warning_text, True, BLACK)
    warning = False

    cursor_x = 255
    cursor_y = 80
    cursor_w = 15
    cursor_h = 23
    cursor_active = False

    music_load_button = Button(450, 250, f3.render('Загрузить музыку', True, BLACK), BLACK)
    if language == 'rus':
        music_load_button = Button(450, 250, f3.render('Загрузить музыку', True, BLACK), BLACK)
    elif language == 'eng':
        music_load_button = Button(500, 250, f3.render('Load music', True, BLACK), BLACK)
    filename = ''

    error_sound = pygame.mixer.Sound('sounds/error_sound.mp3')

    running = True
    while running:

        # задержка
        clock.tick(FPS)

        # цикл обработки событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if not control_settings:
                        running = False
                    else:
                        control_settings = False
                        if language == 'rus':
                            control_text1 = 'Управление'
                            control_text1_x = 490
                            control_text1_y = 170
                            control_text1_w = 200
                            control_text1_h = 35
                        elif language == 'eng':
                            control_text1 = 'Control'
                            control_text1_x = 530
                            control_text1_y = 170
                            control_text1_w = 125
                            control_text1_h = 35
                        control_text1_surf = f3.render(control_text1, True, BLACK)
                if event.key == pygame.K_RETURN:
                    if is_from_game_cycle:
                        if language == 'rus':
                            text1 = 'код не найден'
                            text1_x = 510
                            text1_y = 120
                        else:
                            text1 = 'code not found'
                            text1_x = 515
                            text1_y = 120
                    else:
                        if text.lower() == 'dino birthday':  # код для внешнего вида дино
                            text = ''
                            if language == 'rus':
                                text1 = 'код успесшно активирован'
                                text1_x = 450
                                text1_y = 120
                            else:
                                text1 = 'code has been activated'
                                text1_x = 465
                                text1_y = 120
                            birth_day_code = True
                        elif ' '.join(text.lower().split()[:2:]) == 'set score' and len(text.lower().split()) == 3:
                            # комманда, устанавливающая введенное значение для score
                            try:
                                if int(text.lower().split()[2]) < 0:
                                    raise Exception
                                score = int(text.lower().split()[2])
                                text = ''
                                if language == 'rus':
                                    text1 = 'код успесшно активирован'
                                    text1_x = 450
                                    text1_y = 120
                                else:
                                    text1 = 'code has been activated'
                                    text1_x = 465
                                    text1_y = 120
                            except Exception:
                                if language == 'rus':
                                    text1 = 'код не найден'
                                    text1_x = 510
                                    text1_y = 120
                                else:
                                    text1 = 'code not found'
                                    text1_x = 515
                                    text1_y = 120
                        else:
                            if language == 'rus':
                                text1 = 'код не найден'
                                text1_x = 510
                                text1_y = 120
                            else:
                                text1 = 'code not found'
                                text1_x = 515
                                text1_y = 120
                    text1_surf = f1.render(text1, True, BLACK)
                    text1_print = True
                    sleep(0.3)
                elif key_choose:
                    try:
                        if upkey_choose:
                            up_key = event.key
                            control_upkey = chr(up_key)
                            control_upkey_surf = f2.render(control_upkey, True, BLACK)
                        elif downkey_choose:
                            down_key = event.key
                            control_downkey = chr(down_key)
                            control_downkey_surf = f2.render(control_downkey, True, BLACK)
                        elif blueballkey_choose:
                            blue_ball_key = event.key
                            control_blueballkey = chr(blue_ball_key)
                            control_blueballkey_surf = f2.render(control_blueballkey, True, BLACK)
                        elif redballkey_choose:
                            red_ball_key = event.key
                            control_redballkey = chr(red_ball_key)
                            control_redballkey_surf = f2.render(control_redballkey, True, BLACK)
                        warning = False
                    except Exception:
                        warning = True

                    choose_box = False
                    key_choose = False
                    upkey_choose = False
                    downkey_choose = False
                    blueballkey_choose = False
                    redballkey_choose = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos) and not control_settings:
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active and not control_settings and event.key != pygame.K_RETURN and event.key != pygame.K_ESCAPE:
                    # if event.key == pygame.K_RETURN:
                    #    return text
                    if event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        time += 1

        screen.blit(surf, (200, 25))

        if not control_settings:
            x, y = pygame.mouse.get_pos()
            if 875 <= x <= 975 and 75 <= y <= 107:
                button_color = (133, 133, 200)
            else:
                button_color = (133, 133, 133)

            pressed = pygame.mouse.get_pressed()
            if pressed[0]:  # обработка нажатий левой кнопки мыши
                x1, y1 = pygame.mouse.get_pos()
                if music_load_button.mouse_check((x1, y1)):
                    filename = easygui.fileopenbox(filetypes=['*.mp3', '*.wav', '*.ogg'])
                    try:
                        pygame.mixer.music.load(filename)
                        pygame.mixer.music.play(-1)
                    except Exception:
                        pygame.mixer.music.stop()
                        error_sound.play()
                elif 875 <= x1 <= 975 and 75 <= y1 <= 107:  # проверка на коды
                    if is_from_game_cycle:
                        if language == 'rus':
                            text1 = 'код не найден'
                            text1_x = 510
                            text1_y = 120
                        else:
                            text1 = 'code not found'
                            text1_x = 515
                            text1_y = 120
                    else:
                        if text.lower() == 'dino birthday':  # код для внешнего вида дино
                            text = ''
                            if language == 'rus':
                                text1 = 'код успесшно активирован'
                                text1_x = 450
                                text1_y = 120
                            else:
                                text1 = 'code has been activated'
                                text1_x = 465
                                text1_y = 120
                            birth_day_code = True
                        elif ' '.join(text.lower().split()[:2:]) == 'set score' and len(text.lower().split()) == 3:
                            # комманда, устанавливающая введенное значение для score
                            try:
                                if int(text.lower().split()[2]) < 0:
                                    raise Exception
                                score = int(text.lower().split()[2])
                                text = ''
                                if language == 'rus':
                                    text1 = 'код успесшно активирован'
                                    text1_x = 450
                                    text1_y = 120
                                else:
                                    text1 = 'code has been activated'
                                    text1_x = 465
                                    text1_y = 120
                            except Exception:
                                if language == 'rus':
                                    text1 = 'код не найден'
                                    text1_x = 510
                                    text1_y = 120
                                else:
                                    text1 = 'code not found'
                                    text1_x = 515
                                    text1_y = 120
                        else:
                            if language == 'rus':
                                text1 = 'код не найден'
                                text1_x = 510
                                text1_y = 120
                            else:
                                text1 = 'code not found'
                                text1_x = 515
                                text1_y = 120
                    text1_surf = f1.render(text1, True, BLACK)
                    text1_print = True
                    sleep(0.3)
                elif 265 <= x1 <= 385 and 235 <= y1 <= 270:
                    language = 'rus'
                    text_lang1 = 'Язык'
                    text_lang1_surf = f2.render(text_lang1, True, BLACK)
                    text1_print = False

                    control_text1 = 'Управление'
                    control_text1_surf = f3.render(control_text1, True, BLACK)
                    control_text1_x = 490
                    control_text1_y = 170
                    control_text1_w = 200
                    control_text1_h = 35
                    music_load_button = Button(450, 250, f3.render('Загрузить музыку', True, BLACK), BLACK)
                elif 265 <= x1 <= 380 and 275 <= y1 <= 310:
                    language = 'eng'
                    text_lang1 = 'Language'
                    text_lang1_surf = f2.render(text_lang1, True, BLACK)
                    text1_print = False

                    control_text1 = 'Control'
                    control_text1_surf = f3.render(control_text1, True, BLACK)
                    control_text1_x = 530
                    control_text1_y = 170
                    control_text1_w = 125
                    control_text1_h = 35
                    music_load_button = Button(500, 250, f3.render('Load music', True, BLACK), BLACK)
                elif control_text1_x <= x1 <= control_text1_x + control_text1_w and \
                        control_text1_y <= y1 <= control_text1_y + control_text1_h:
                    control_settings = True

                    if language == 'rus':
                        control_text1_x = 480
                        control_text1_y = 50

                        control_text_upkey = 'Прыжок'
                        control_text_downkey = 'Присядка'
                        control_text_blueballkey = 'Стрельба водяным шаром'
                        control_text_redballkey = 'Стрельба огненным шаром'

                        warning_text = 'Произошла ошибка'
                        warning_text_x = 470
                        warning_text_y = 550
                    elif language == 'eng':
                        control_text1_x = 520
                        control_text1_y = 50

                        control_text_upkey = 'Jump'
                        control_text_downkey = 'Sit'
                        control_text_blueballkey = 'Water ball shooting'
                        control_text_redballkey = 'Fire ball shooting'

                        warning_text = 'Error'
                        warning_text_x = 560
                        warning_text_y = 550

                    warning = False

                    control_text_upkey_surf = f2.render(control_text_upkey, True, BLACK)
                    control_text_downkey_surf = f2.render(control_text_downkey, True, BLACK)
                    control_text_blueballkey_surf = f2.render(control_text_blueballkey, True, BLACK)
                    control_text_redballkey_surf = f2.render(control_text_redballkey, True, BLACK)
                    control_text2_surf = f4.render(control_text1, True, BLACK)
                    warning_text_surf = f2.render(warning_text, True, BLACK)

            pygame.draw.rect(screen, button_color, (875, 75, 100, 32))
            if text1_print:
                screen.blit(text1_surf, (text1_x, text1_y))

            screen.blit(control_text1_surf, (control_text1_x, control_text1_y))

            music_load_button.draw(screen)
            if music_load_button.mouse_check(pygame.mouse.get_pos()):
                music_load_button.color = 'red'
            else:
                music_load_button.color = BLACK

            if language == 'rus':
                text_lang_rus_surf = f2.render(text_lang_rus, True, 'blue')
                text_lang_eng_surf = f2.render(text_lang_eng, True, BLACK)
            elif language == 'eng':
                text_lang_rus_surf = f2.render(text_lang_rus, True, BLACK)
                text_lang_eng_surf = f2.render(text_lang_eng, True, 'blue')
            screen.blit(text_lang1_surf, (270, 200))
            screen.blit(text_lang_rus_surf, (270, 240))
            screen.blit(text_lang_eng_surf, (270, 280))

            # Render the current text.
            txt_surface = font.render(text, True, color)
            # Resize the box if the text is too long.
            width = max(standart_width, txt_surface.get_width() + 10)
            input_box.w = width
            # Blit the text.
            screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
            # Blit the input_box rect.
            pygame.draw.rect(screen, color, input_box, 2)

            if active and cursor_active:
                pygame.draw.rect(screen, 'black', (cursor_x + txt_surface.get_width(), cursor_y, cursor_w, cursor_h))

            if time % 20 == 0:
                cursor_active = not cursor_active

        else:
            # pygame.draw.rect(screen, 'grey', (900, 450, 25, 25))
            if choose_box:
                pygame.draw.rect(screen, 'grey', (choose_box_x, choose_box_y, 25, 25))

            screen.blit(control_text2_surf, (control_text1_x, control_text1_y))

            screen.blit(control_text_upkey_surf, (control_text_upkey_x, control_text_upkey_y))
            screen.blit(control_text_downkey_surf, (control_text_downkey_x, control_text_downkey_y))
            screen.blit(control_text_blueballkey_surf, (control_text_blueballkey_x, control_text_blueballkey_y))
            screen.blit(control_text_redballkey_surf, (control_text_redballkey_x, control_text_redballkey_y))

            screen.blit(control_upkey_surf, (control_upkey_x, control_upkey_y))
            screen.blit(control_downkey_surf, (control_downkey_x, control_downkey_y))
            screen.blit(control_blueballkey_surf, (control_blueballkey_x, control_blueballkey_y))
            screen.blit(control_redballkey_surf, (control_redballkey_x, control_redballkey_y))

            if warning:
                screen.blit(warning_text_surf, (warning_text_x, warning_text_y))

            pressed = pygame.mouse.get_pressed()
            if pressed[0]:  # обработка нажатий левой кнопки мыши
                x1, y1 = pygame.mouse.get_pos()
                if control_upkey_x <= x1 <= control_upkey_x + 25 \
                        and control_upkey_y <= y1 <= control_upkey_y + 25:
                    upkey_choose = True
                    downkey_choose = False
                    blueballkey_choose = False
                    redballkey_choose = False
                    key_choose = True
                    choose_box = True
                    choose_box_x = control_upkey_x
                    choose_box_y = control_upkey_y
                elif control_downkey_x <= x1 <= control_downkey_x + 25 \
                        and control_downkey_y <= y1 <= control_downkey_y + 25:
                    upkey_choose = False
                    downkey_choose = True
                    blueballkey_choose = False
                    redballkey_choose = False
                    key_choose = True
                    choose_box = True
                    choose_box_x = control_downkey_x
                    choose_box_y = control_downkey_y
                elif control_blueballkey_x <= x1 <= control_blueballkey_x + 25 \
                        and control_blueballkey_y <= y1 <= control_blueballkey_y + 25:
                    upkey_choose = False
                    downkey_choose = False
                    blueballkey_choose = True
                    redballkey_choose = False
                    key_choose = True
                    choose_box = True
                    choose_box_x = control_blueballkey_x
                    choose_box_y = control_blueballkey_y
                elif control_redballkey_x <= x1 <= control_redballkey_x + 25 \
                        and control_redballkey_y <= y1 <= control_redballkey_y + 25:
                    upkey_choose = False
                    downkey_choose = False
                    blueballkey_choose = False
                    redballkey_choose = True
                    key_choose = True
                    choose_box = True
                    choose_box_x = control_redballkey_x
                    choose_box_y = control_redballkey_y

        # обновление экрана
        pygame.display.update()

    keys = [up_key, down_key, blue_ball_key, red_ball_key]
    return birth_day_code, score, language, keys
