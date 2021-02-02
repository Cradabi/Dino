import pygame
from dino import Dino

FPS = 60
WIDTH = 1200
HEIGHT = 800


def cut_scen_3(screen, color, score, HI, road_cord_x1, birthday_code, language, keys, water_number, fire_number, money):
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
                    if t > 200 and t < 999:
                        t_c = t // 100
                        t_c += 1
                        t = t_c * 100
            if event.type == pygame.KEYDOWN:  # обработка событий клавиатуры
                if event.key == pygame.K_ESCAPE:
                    quit()
                if event.key == 32:
                    if t > 200 and t < 999:
                        t_c = t // 100
                        t_c += 1
                        t = t_c * 100
                if event.unicode == 'e':
                    if t >= 600 and t < 750:
                        if money >= 50:
                            money -= 50
                            fire_number += 30
                            print(1)
                    elif t >= 750 and t < 900:
                        if money >= 50:
                            money -= 50
                            fire_number += 30
                            print(1)
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
                # t += 1
            elif language == 'eng':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Hi, Dino.", False, (0, 0, 0))
                screen.blit(text, (930, 370))
        elif t >= 300 and t < 400:
            screen.blit(mag_left, (mag_cord_x, mag_cord_y))
            screen.blit(dialog_left, (10, 300))
            if language == 'rus':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Здравствуйте.", False, (0, 0, 0))
                screen.blit(text, (40, 370))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Кто вы?", False, (0, 0, 0))
            elif language == 'eng':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Hello.", False, (0, 0, 0))
                screen.blit(text, (40, 370))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Who are you?", False, (0, 0, 0))
            # t += 1
        elif t >= 400 and t < 500:
            screen.blit(mag_left, (mag_cord_x, mag_cord_y))
            screen.blit(dialog_right, (900, 300))
            if language == 'rus':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Я торговец.", False, (0, 0, 0))
                screen.blit(text, (930, 370))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("У меня есть", False, (0, 0, 0))
                screen.blit(text, (930, 390))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("зелья, которые смогут", False, (0, 0, 0))
                screen.blit(text, (930, 410))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("увеличить количество", False, (0, 0, 0))
                screen.blit(text, (930, 430))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("огня и воды.", False, (0, 0, 0))
                screen.blit(text, (930, 450))
            elif language == 'eng':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("I am a merchant.", False, (0, 0, 0))
                screen.blit(text, (930, 370))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("I have portions", False, (0, 0, 0))
                screen.blit(text, (930, 390))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("that will increase", False, (0, 0, 0))
                screen.blit(text, (930, 410))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("the amount of", False, (0, 0, 0))
                screen.blit(text, (930, 430))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("fire and water", False, (0, 0, 0))
                screen.blit(text, (930, 450))
        elif t >= 500 and t < 600:
            screen.blit(mag_left, (mag_cord_x, mag_cord_y))
            screen.blit(dialog_left, (10, 300))
            if language == 'rus':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Можешь рассказать", False, (0, 0, 0))
                screen.blit(text, (40, 370))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("подробнеее?", False, (0, 0, 0))
                screen.blit(text, (40, 390))
            elif language == 'eng':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Can you tell more?", False, (0, 0, 0))
                screen.blit(text, (40, 390))
        elif t >= 600 and t < 750:
            screen.blit(mag_left, (mag_cord_x, mag_cord_y))
            screen.blit(dialog_right, (900, 300))
            if language == 'rus':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Ты можешь купить 30", False,
                                 (0, 0, 0))
                screen.blit(text, (930, 370))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("огней за 50 денег,", False,
                                 (0, 0, 0))
                screen.blit(text, (930, 390))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render('нажав на "E".', False,
                                 (0, 0, 0))
                screen.blit(text, (930, 410))
            elif language == 'eng':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("You can buy 30", False,
                                 (0, 0, 0))
                screen.blit(text, (930, 370))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("fires for 50 moneys", False,
                                 (0, 0, 0))
                screen.blit(text, (930, 390))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render('by pressing "E".', False,
                                 (0, 0, 0))
                screen.blit(text, (930, 410))
        elif t >= 750 and t < 900:
            screen.blit(mag_left, (mag_cord_x, mag_cord_y))
            screen.blit(dialog_right, (900, 300))
            if language == 'rus':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Ты можешь купить 30", False,
                                 (0, 0, 0))
                screen.blit(text, (930, 370))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("зарядов воды за 50 денег,", False,
                                 (0, 0, 0))
                screen.blit(text, (930, 390))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render('нажав на "E".', False,
                                 (0, 0, 0))
                screen.blit(text, (930, 410))
            elif language == 'eng':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("You can buy 30", False,
                                 (0, 0, 0))
                screen.blit(text, (930, 370))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("waterballs for 50", False,
                                 (0, 0, 0))
                screen.blit(text, (930, 390))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render('moneys by pressing "E".', False,
                                 (0, 0, 0))
                screen.blit(text, (930, 410))
        elif t >= 900 and t < 1000:
            screen.blit(mag_left, (mag_cord_x, mag_cord_y))
            screen.blit(dialog_left, (10, 300))
            if language == 'rus':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Я помогу вам.", False, (0, 0, 0))
                screen.blit(text, (40, 370))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("До свидания.", False, (0, 0, 0))
                screen.blit(text, (40, 390))
            elif language == 'eng':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Thanks. I will try.", False, (0, 0, 0))
                screen.blit(text, (40, 370))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("to help. Goodbye.", False, (0, 0, 0))
                screen.blit(text, (40, 390))
        elif t >= 1000 and t < 1230:
            # t += 1
            mag_cord_x += 1
            screen.blit(mag_right, (mag_cord_x, mag_cord_y))
        elif t >= 1230:
            running = False
            # origin_dino(screen, color, score, HI, birthday_code, language, keys)

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
