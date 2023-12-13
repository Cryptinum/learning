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
        self.image = pygame.transform.rotate(self.image, randint(-360, 360))
        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x)