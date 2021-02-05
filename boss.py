import pygame


class Boss(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.scale = 130
        self.standart_x = x
        self.standart_y = y

        self.hp = 200

        self.stand = pygame.image.load('imgs/boss/boss_spit1.png')
        self.stand = pygame.transform.scale(self.stand, (int(self.scale * 1.06), self.scale))
        self.stand.set_colorkey('white')

        self.run_img = pygame.image.load('imgs/boss/boss_run.png')
        self.run_img = pygame.transform.scale(self.run_img, (int(self.scale * 1.06), self.scale))
        self.run_img.set_colorkey('white')

        self.jump_img = pygame.image.load('imgs/boss/boss_jump.png')
        self.jump_img = pygame.transform.scale(self.jump_img, (int(self.scale * 1.06), self.scale))
        self.jump_img.set_colorkey('white')

        self.asteroid = pygame.image.load('imgs/asteroid.png')
        self.asteroid = pygame.transform.scale(self.asteroid, (150, 67))
        self.asteroid.set_colorkey('white')
        self.asteroid_x = 100
        self.asteroid_y = -120

        self.spit_img1 = pygame.image.load('imgs/boss/boss_spit1.png')
        self.spit_img1 = pygame.transform.scale(self.spit_img1, (int(self.scale * 1.06), self.scale))
        self.spit_img1.set_colorkey('white')

        self.spit_img2 = pygame.image.load('imgs/boss/boss_spit2.png')
        self.spit_img2 = pygame.transform.scale(self.spit_img2, (int(self.scale * 1.06), self.scale))
        self.spit_img2.set_colorkey('white')

        self.spit = pygame.image.load('imgs/boss/harch.png')
        self.spit.set_colorkey('white')

        self.image = self.run_img
        self.x = x
        self.y = y

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.jump_status = 0
        self.jump_time = 0
        self.fast_jump = 0

    def set_stand(self):
        self.image = self.stand
        self.rect = self.image.get_rect()

    def jump(self):
        if self.jump_status == 1:  # монстр летит вверх
            self.jump_time += 1
            if self.jump_time % 20 != 0:
                if self.jump_time % 2 == 0:
                    self.fast_jump += 1
                self.y -= 14
                self.y += self.fast_jump
                self.image = self.jump_img
            else:
                self.jump_status = 2
                self.jump_time = 0
        elif self.jump_status == 2:  # монстр весит в воздухе
            self.jump_time += 1
            if self.jump_time % 1 != 0:
                self.image = dino1
            else:
                self.jump_status = 3
                self.jump_time = 0
        elif self.jump_status == 3:  # монстр просто опускается
            self.jump_time += 1
            if self.jump_time % 20 != 0 and self.y < self.standart_y:
                self.y += 14
                self.y -= self.fast_jump
                if self.jump_time % 2 == 0:
                    self.fast_jump -= 1
                self.image = self.jump_img
            else:
                self.jump_status = 0
                self.jump_time = 0
                self.fast_jump = 0
                self.image = self.run_img

    def collide_check(self, group):
        # проверяет столкнулся ли монстр с данной группой
        # возвращает True если есть столкновение
        collide_sprite = pygame.sprite.spritecollideany(self, group)
        if collide_sprite:
            if pygame.sprite.collide_mask(self, collide_sprite):
                return True
        return False

    def die(self, boss_die_t):  # TODO сделать смерть
        if boss_die_t > 300 and boss_die_t <= 330:
            self.asteroid_x += 5
            self.asteroid_y += 25

    def update(self):
        if self.jump_status != 0:
            self.jump()
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
