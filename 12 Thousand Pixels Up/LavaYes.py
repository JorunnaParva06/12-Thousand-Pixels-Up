from typing import Any
import os
import pygame

class lava(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        image_location = (os.path.join(os.path.dirname(__file__), "lava_tile.png"))
        self.image = pygame.image.load(image_location).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.width = width
        self.rect.height = height
        self.speed = 3
    
    def update(self):
        self.rect.y -= self.speed # The speed at which the lava will rise
    
    def Scroll(self, scroll):
        self.rect.y += scroll