import pygame


class Dino:
    def __init__(self):
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
        self.x = 250
        self.y = 200

    def run_anim(self, screen):
        if self.out_now_run == 'img1':
            self.out = self.run_img1
            self.out_now_run = 'img2'
        elif self.out_now_run == 'img2':
            self.out = self.run_img2
            self.out_now_run = 'img1'
        screen.blit(self.out, (self.x, self.y))

    def sit_anim(self, screen):
        if self.out_now_sit == 'img1':
            self.out = self.sit_img1
            self.out_now_sit = 'img2'
        elif self.out_now_sit == 'img2':
            self.out = self.sit_img2
            self.out_now_sit = 'img1'
        screen.blit(self.out, (self.x, self.y))

    def fire_anim(self, screen):
        t = 0
        for i in range(20):
            t += 1
            if t % 10 == 0:
                screen.fill('black')
                screen.blit(self.fire_img2, (self.x, self.y))
            if t % 19 == 0:
                screen.fill('black')
                screen.blit(self.fire_img1, (self.x, self.y))

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
        u = 1
