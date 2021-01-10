import pygame


class Bird:
    def __init__(self):
        self.run_img1 = pygame.image.load('imgs/bird1.png')
        self.run_img2 = pygame.image.load('imgs/bird2.png')
        self.run_img1.set_colorkey('white')
        self.run_img2.set_colorkey('white')
        self.out_now_fly = 'img1'
        self.out = self.run_img1
        self.x = 450
        self.y = 200

    def fly_anim(self, screen):
        if self.out_now_fly == 'img1':
            self.out = self.run_img1
            self.out_now_fly = 'img2'
        elif self.out_now_fly == 'img2':
            self.out = self.run_img2
            self.out_now_fly = 'img1'
        screen.blit(self.out, (self.x, self.y))
