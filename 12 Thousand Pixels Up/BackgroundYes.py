# Game made by Jed Krause
import pygame
import os

class background(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()

        image_location = (os.path.join(os.path.dirname(__file__), "stage.png"))
        self.image = pygame.image.load(image_location).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()