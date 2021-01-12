# Анимация бегущего дино


import pygame
from dino import Dino
from bird import Bird

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
    moon = pygame.image.load('imgs/moon.png')
    moon.set_colorkey('black')
    star = pygame.image.load('imgs/star.png')
    star.set_colorkey('black')
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
    jump_status = 0
    road_cord_x1 = 0
    road_cord_x2 = 2398
    running = True
    while running:

        clock.tick(FPS)

        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                fire_status = True
                if status_dino == 'sit':
                    fire_cor_y = 264
                    fire_cor_x = 380
                elif not fire_status:
                    fire_cor_x = 355
                    fire_cor_y = 230
            if event.type == pygame.KEYDOWN:
                if event.key == 115:  # if event.unicode == 's':
                    status_dino = 'sit'
                    d.y += 34
                    time = -1
                elif event.key == 119:  # elif event.unicode == 'w':
                    jump_status = 1
            if event.type == pygame.KEYUP:
                if event.key == 115:  # if event.unicode == 's':
                    status_dino = 'run'
                    d.y -= 34
                    time = -1

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

        screen.blit(road1, (road_cord_x1, 270))
        screen.blit(road2, (road_cord_x2, 270))
        if road_cord_x2 <= -1400:
            road_cord_x1 = 0
            road_cord_x2 = 2398
        else:
            road_cord_x1 -= 10
            road_cord_x2 -= 10

        if fire_status:
            # d.fire_anim(screen)
            pygame.draw.circle(screen, (245, 109, 12), (fire_cor_x, fire_cor_y), 20)
            fire_cor_x += 10
        if fire_cor_x > 800:
            fire_cor_x = 355
            fire_status = False

        # отрисовка и изменение свойств объектов
        # ...

        # обновление экрана
        pygame.display.flip()

    pygame.quit()
