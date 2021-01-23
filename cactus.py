import pygame
from dino import Dino


class Cactus(pygame.sprite.Sprite):
    def __init__(self, x, y, image, *group):
        super().__init__(*group)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, speed):  # двигает кактус
        self.rect = self.rect.move(-speed, 0)
