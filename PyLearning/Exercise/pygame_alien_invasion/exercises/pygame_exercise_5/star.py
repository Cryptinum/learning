# Creating ship.

import pygame
from pygame.sprite import Sprite
from random import randint

class Star(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        self.image = pygame.image.load('images/starsmall.png')
        angle = randint(-360, 360)
        zoom = 0.25
        self.image = pygame.transform.rotozoom(self.image, angle, zoom)
        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x)