import pygame


class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.fly_img1 = pygame.image.load('imgs/bird1.png')
        self.fly_img2 = pygame.image.load('imgs/bird2.png')
        self.fly_img1.set_colorkey('white')
        self.fly_img2.set_colorkey('white')
        self.out_now_fly = 'img1'