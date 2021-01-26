import pygame
from time import sleep

FPS = 60
WIDTH = 1200
HEIGHT = 800


def sets(screen, score):
    clock = pygame.time.Clock()

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
    text1_surf = f1.render(text1, True, 'black')

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
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    # if event.key == pygame.K_RETURN:
                    #    return text
                    if event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        x, y = pygame.mouse.get_pos()
        if 875 <= x <= 975 and 75 <= y <= 107:
            button_color = (133, 133, 200)
        else:
            button_color = (133, 133, 133)

        pressed = pygame.mouse.get_pressed()
        if pressed[0]:  # обработка нажатий левой кнопки мыши
            x1, y1 = pygame.mouse.get_pos()
            if 875 <= x1 <= 975 and 75 <= y1 <= 107:  # проверка на коды
                if text.lower() == 'dino birthday':  # код для внешнего вида дино
                    text = ''
                    text1 = 'код успесшно активирован'
                    text1_x = 450
                    text1_y = 120
                    birth_day_code = True
                elif ' '.join(text.lower().split()[:2:]) == 'set score' and len(text.lower().split()) == 3:
                    # комманда, устанавливающая введенное значение для score
                    try:
                        score = int(text.lower().split()[2])
                        text = ''
                        text1 = 'код успесшно активирован'
                        text1_x = 450
                        text1_y = 120
                    except Exception:
                        text1 = 'код не найден'
                        text1_x = 510
                        text1_y = 120
                else:
                    text1 = 'код не найден'
                    text1_x = 510
                    text1_y = 120
                text1_surf = f1.render(text1, True, 'black')
                text1_print = True
                sleep(0.3)

        screen.blit(surf, (200, 25))
        pygame.draw.rect(screen, button_color, (875, 75, 100, 32))
        if text1_print:
            screen.blit(text1_surf, (text1_x, text1_y))

        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(standart_width, txt_surface.get_width() + 10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)

        # обновление экрана
        pygame.display.update()

    return birth_day_code, score
