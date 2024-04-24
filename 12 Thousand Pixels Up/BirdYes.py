# Game made by Jed Krause
import pygame
import os

class bird(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, speed):
        super().__init__()

        image_location = (os.path.join(os.path.dirname(__file__), "bullet_fireball.png"))
        self.image = pygame.image.load(image_location).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.total_scroll = 0 
        self.Flip()
    
    def Update(self):
        self.rect.x += -self.speed
        if self.rect.x < -100:
            self.rect.x = 1000
        elif self.rect.x > 1000:
            self.rect.x = -100
    
    def Flip(self):
        if self.speed > 0:
            self.image = pygame.transform.flip(self.image, True, False)

    def Scroll(self, scroll):
        self.rect.y += scroll
        self.total_scroll += scroll