import pygame


class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.fly_img1 = pygame.image.load('imgs/bird1.png')
        self.fly_img2 = pygame.image.load('imgs/bird2.png')
        self.fly_img1.set_colorkey('white')
        self.fly_img2.set_colorkey('white')
        self.out_now_fly = 'img1'
        self.x = x
        self.y = y

        self.image = self.fly_img1
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, speed, t):  # обновляет(меняет картинки) и двигает птицу
        if self.out_now_fly == 'img1' and t % 10 == 0:
            self.image = self.fly_img1
            # self.rect = self.image.get_rect()
            # self.rect.x = self.x - speed
            # self.rect.y = self.y
            self.out_now_fly = 'img2'
            # self.rect = self.rect.move(-speed, 12)
        elif self.out_now_fly == 'img2' and t % 10 == 0:
            self.image = self.fly_img2
            # self.rect = self.image.get_rect()
            # self.rect.x = self.x - speed
            # self.rect.y = self.y
            self.out_now_fly = 'img1'
            # self.rect = self.rect.move(-speed, -12)
        else:
            self.rect = self.rect.move(-speed, 0)
