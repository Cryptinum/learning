import pygame
import random
import math
from pygame.sprite import Sprite

class Rain(Sprite):

	def __init__(self, ai_game):
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings

		self.image = pygame.image.load('images/rain.png')
		self.rect = self.image.get_rect()
		new_height = self.rect.height * random.uniform(1,3)
		new_width = self.rect.width * random.uniform(0.8,1.2)
		self.image = pygame.transform.scale(self.image, (new_height, new_width))
		self.rect = self.image.get_rect()
		self.rect.x = random.uniform(0, self.settings.screen_width)
		self.rect.y = 0

		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def update(self):
		self.y += self.settings.drop_speed
		self.rect.y = self.y