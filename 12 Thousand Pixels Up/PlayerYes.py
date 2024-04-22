import pygame
import os
from pygame import mixer

class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        image_location = (os.path.join(os.path.dirname(__file__), "player.png"))
        self.image = pygame.image.load(image_location).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = 40

        self.x_speed = 5
        self.x_velocity = 0
        self.jumpForce = -25
        self.gravity = 1
        self.y_velocity = 0
        self.canJump = True
    
    def Move(self, direction):
        self.x_velocity = direction * self.x_speed

    def Update(self):
        self.rect.x += self.x_velocity
        self.rect.y += self.y_velocity
        self.x_velocity = 0
    
    def ApplyGravity(self):
        self.y_velocity += self.gravity

    def Jump(self):
        if self.canJump == True:
            jump_sound = mixer.Sound(os.path.join(os.path.dirname(__file__), "Jump.ogg"))
            self.y_velocity = self.jumpForce
            jump_sound.play()
            self.canJump = False
    
    def Scroll(self, scroll):
        self.rect.y += scroll