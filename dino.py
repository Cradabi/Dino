import pygame
from cactus import Cactus


class Dino(pygame.sprite.Sprite):
    def __init__(self):
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

        self.out = self.run_img1
        self.x = 100
        self.y = 200

        self.rect = self.out.get_rect()
        self.rect.x = self.x - 15
        self.rect.y = self.y

    def run_anim(self, screen):
        if self.out_now_run == 'img1':
            self.out = self.run_img1
            self.out_now_run = 'img2'
        elif self.out_now_run == 'img2':
            self.out = self.run_img2
            self.out_now_run = 'img1'
        screen.blit(self.out, (self.x, self.y))
        self.rect = self.out.get_rect()
        self.rect.x = self.x - 15
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
        self.rect.x = self.x - 5
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

    def collide_check(self, all_cacti):
        collide_sprite = pygame.sprite.spritecollideany(self, all_cacti)
        if isinstance(collide_sprite, Cactus):
            self.die()

    def die(self):  # TODO сделать нормальную смерть а не вот это
        quit()
