import pygame
import os

class victory(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        image_location = (os.path.join(os.path.dirname(__file__), "pixel_ignite.png"))
        self.image = pygame.image.load(image_location).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.total_scroll = 0

    def Scroll(self, scroll):
        self.rect.y += scroll
        self.total_scroll += scroll