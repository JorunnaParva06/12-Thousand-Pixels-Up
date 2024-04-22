import pygame
import os

class enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, native_index):
        super().__init__()

        image_location = (os.path.join(os.path.dirname(__file__), "enemy.png"))
        self.image = pygame.image.load(image_location).convert_alpha()
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.native_index = native_index
        self.speed = 3
        self.total_scroll = 0
    
    def Update(self, right, left):
        self.rect.x += self.speed
        if self.rect.x >= right or self.rect.x <= left:
            self.speed *= -1
            self.Flip()
    
    def Flip(self):
        if self.speed > 0:
            self.image = pygame.transform.flip(self.image, True, False)
        elif self.speed < 0:
            self.image = pygame.transform.flip(self.image, True, False)
    
    def Scroll(self, scroll):
        self.rect.y += scroll
        self.total_scroll += scroll