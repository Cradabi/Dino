import pygame
import sqlite3

DINO_COLOR = (83, 83, 83)


class Dino(pygame.sprite.Sprite):
    def __init__(self, x=100, y=200):
        super().__init__()
        self.run_img1 = pygame.image.load('imgs/dino2.png')
        self.run_img2 = pygame.image.load('imgs/dino3.png')
        self.run_img1.set_colorkey('white')
        self.run_img2.set_colorkey('white')
        self.out_now_run = 'img1'

        self.sit_img1 = pygame.image.load('imgs/dino_sit1.png')
        self.sit_img2 = pygame.image.load('imgs/dino_sit2.png')
        self.sit_img1.set_colorkey('white')
        self.sit_img2.set_colorkey('white')
        self.out_now_sit = 'img1'

        self.fire_img1 = pygame.image.load('imgs/dino1.png')
        self.fire_img2 = pygame.image.load('imgs/dino_fire1.png')
        self.fire_img1.set_colorkey('white')
        self.fire_img2.set_colorkey('white')
        self.out_now_fire = 'img1'

        self.fare_ball_img = pygame.image.load('imgs/fare_ball1.jpg')
        self.fare_ball_img.set_colorkey('black')
        self.watter_ball_img = pygame.image.load('imgs/watter_ball1.jpg')
        self.watter_ball_img.set_colorkey('black')

        self.dino_dead = pygame.image.load('imgs/dino_dead.png')
        self.dino_dead.set_colorkey('white')

        self.image = self.run_img1
        self.x = x
        self.y = y

        self.rect = self.image.get_rect()
        self.rect.x = self.x - 15
        self.rect.y = self.y

        self.mask = pygame.mask.from_surface(self.image)

        self.con = sqlite3.connect('HI.db')
        self.cur = self.con.cursor()
        self.HI_s = self.cur.execute(
            """Select HI From HI""").fetchall()
        self.HI = int(self.HI_s[0][0])
        self.die_status = False
        self.color = 'white'

    def run_anim(self, screen):  # меняет ноги у бегущего прямо дино и выводит дино
        if self.image == self.sit_img1:
            self.image = self.run_img2
            self.out_now_run = 'img1'
        elif self.image == self.sit_img2:
            self.image = self.run_img1
            self.out_now_run = 'img2'
        elif self.out_now_run == 'img1':
            self.image = self.run_img1
            self.out_now_run = 'img2'
        elif self.out_now_run == 'img2':
            self.image = self.run_img2
            self.out_now_run = 'img1'
        screen.blit(self.image, (self.x, self.y))
        self.rect = self.image.get_rect()
        self.rect.x = self.x  # - 15
        self.rect.y = self.y

    def sit_anim(self, screen):  # меняет ноги у бегущего вприсядку дино и выводит дино
        if self.image == self.run_img1:
            self.image = self.sit_img2
            self.out_now_sit = 'img1'
        elif self.image == self.run_img2:
            self.image = self.sit_img1
            self.out_now_sit = 'img2'
        elif self.out_now_sit == 'img1':
            self.image = self.sit_img1
            self.out_now_sit = 'img2'
        elif self.out_now_sit == 'img2':
            self.image = self.sit_img2
            self.out_now_sit = 'img1'
        screen.blit(self.image, (self.x, self.y))
        self.rect = self.image.get_rect()
        self.rect.x = self.x  # - 5
        self.rect.y = self.y

    def jump_anim(self, screen):  # ненужная функция, надо либо удалить, либо переписать
        k = 20
        while k > 0:
            k -= 1
            self.y -= 5
            screen.fill(self.color)
            screen.blit(self.fire_img1, (self.x, self.y))
        k = 5
        while k > 0:
            k -= 1
        k = 20
        while k > 0:
            k -= 1
            self.y += 5
            screen.fill('black')
            screen.blit(self.fire_img1, (self.x, self.y))

    def fare_ball_anim(self, screen, x, y):
        self.fare_ball_sprites = pygame.sprite.Group()
        self.fare_ball_sprite = pygame.sprite.Sprite()
        self.fare_ball_sprite.image = self.fare_ball_img
        self.fare_ball_sprite.rect = self.fare_ball_sprite.image.get_rect()
        self.fare_ball_sprites.add(self.fare_ball_sprite)
        self.fare_ball_sprite.rect.x = x
        self.fare_ball_sprite.rect.y = y
        self.fare_ball_sprites.draw(screen)

    def watter_ball_anim(self, screen, x, y):
        self.watter_ball_sprites = pygame.sprite.Group()
        self.watter_ball_sprite = pygame.sprite.Sprite()
        self.watter_ball_sprite.image = self.watter_ball_img
        self.watter_ball_sprite.rect = self.watter_ball_sprite.image.get_rect()
        self.watter_ball_sprites.add(self.watter_ball_sprite)
        self.watter_ball_sprite.rect.x = x
        self.watter_ball_sprite.rect.y = y
        self.watter_ball_sprites.draw(screen)

    def collide_check(self, group):
        # проверяет столкнулся ли дино с данной группой
        # возвращает True если есть столкновение
        collide_sprite = pygame.sprite.spritecollideany(self, group)
        if collide_sprite:
            if pygame.sprite.collide_mask(self, collide_sprite):
                return True
        return False

    def die(self, score):  # фиксирует смерть и записывает рекорды в sql таблицу
        self.die_status = True
        self.image = self.dino_dead
        if score > self.HI:
            self.HI_s = self.cur.execute(
                """Update Hi Set HI = {} Where id = 0""".format(score)).fetchall()
        self.con.commit()

    def update(self, screen):  # обновляет и выводит дино
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        screen.blit(self.image, (self.x, self.y))
