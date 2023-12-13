import sys
import pygame
import math

from settings import Settings
from star import Star
from rain import Rain
from random import randint

##### Exercise: Make a grid of stars in different rotating angles. #####

class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        self.stars = pygame.sprite.Group()
        self.rains = pygame.sprite.Group()
        self._create_stars()
        self._create_rain()

    def run_game(self):
        while True:
            self._check_events()
            self._update_rain()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _create_stars(self):
        star = Star(self)
        screen_edge = self.settings.star_screen_edge
        star_border = self.settings.star_border
        star_size_width, star_size_height = star.rect.size
        star_width = star_size_width + star_border * 2
        star_height = star_size_height + star_border * 2
        
        avaliable_space_x = self.settings.screen_width - (2 * screen_edge)
        avaliable_space_y = self.settings.screen_height - (2 * screen_edge)
        number_stars_x = avaliable_space_x // (2 * star_width)
        number_stars_y = avaliable_space_y // (2 * star_height)

        actual_border_width = (self.settings.screen_width -
                               star_width * (2 * number_stars_x - 1))
        actual_border_height = (self.settings.screen_height -
                               star_height * (2 * number_stars_y - 1))

        for y_number in range(number_stars_y):
            for x_number in range(number_stars_x):
                star = Star(self)
                star.x = (actual_border_width / 2 + 2 * star_width * x_number + 5
                          + randint(math.floor(-star_width/1.2),
                                    math.floor(star_width/1.2)))
                star.y = (actual_border_height / 2 + 2 * star_width * y_number + 5
                          + randint(math.floor(-star_height/1.2),
                                    math.floor(star_height/1.2)))
                star.rect.x = star.x
                star.rect.y = star.y
                self.stars.add(star)

    def _create_rain(self):
        for number in range(self.settings.rains_allowed):
            rain = Rain(self)
            self.rains.add(rain)

    def _update_rain(self):
        self.rains.update()
        for rain in self.rains.copy():
            if rain.rect.top >= self.settings.screen_height:
                self.rains.remove(rain)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)
        self.rains.draw(self.screen)
        
        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()