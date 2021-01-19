import pygame
import sqlite3


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

        self.out = self.run_img1
        self.x = x
        self.y = y

        self.rect = self.out.get_rect()
        self.rect.x = self.x - 15
        self.rect.y = self.y

        self.con = sqlite3.connect('HI.db')
        self.cur = self.con.cursor()
        self.HI_s = self.cur.execute(
            """Select HI From HI""").fetchall()
        self.HI = int(self.HI_s[0][0])

    def run_anim(self, screen):
        if self.out_now_run == 'img1':
            self.out = self.run_img1
            self.out_now_run = 'img2'
        elif self.out_now_run == 'img2':
            self.out = self.run_img2
            self.out_now_run = 'img1'
        screen.blit(self.out, (self.x, self.y))
        self.rect = self.out.get_rect()
        self.rect.x = self.x  # - 15
        self.rect.y = self.y

    def sit_anim(self, screen):
        if self.out_now_sit == 'img1':
            self.out = self.sit_img1
            self.out_now_sit = 'img2'
        elif self.out_now_sit == 'img2':
            self.out = self.sit_img2
            self.out_now_sit = 'img1'
        screen.blit(self.out, (self.x, self.y))
        self.rect = self.out.get_rect()
        self.rect.x = self.x  # - 5
        self.rect.y = self.y

    def jump_anim(self, screen):
        k = 20
        while k > 0:
            k -= 1
            self.y -= 5
            screen.fill('black')
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

    def collide_check(self, group, spr_class, score):
        collide_sprite = pygame.sprite.spritecollideany(self, group)
        if isinstance(collide_sprite, spr_class):
            self.die(score)

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

    def die(self, score):  # TODO сделать нормальную смерть а не вот это
        if score > self.HI:
            self.HI_s = self.cur.execute(
                """Update Hi Set HI = {} Where id = 0""".format(score)).fetchall()
            print(score)
        self.con.close()
        quit()
        # pass

    def update(self, screen):
        self.rect = self.out.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        screen.blit(self.out, (self.x, self.y))
