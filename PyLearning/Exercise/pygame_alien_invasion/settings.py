'''
    Instead of adding settings throughout the code, we can write
a module that contains a class to store all the settings in one place.
    It allows us to work with just one setting object anytime when
we need to access an individual setting.
    We can simply modify the value in setting class, instead of
searching for different settings throughout the project.
'''

class Settings(object):
    """A class to store all setting for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3
        
        # Bullet settings
        self.bullet_width = 3000
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 3.0

        # Alien settings
        self.alien_speed = 1.0
        self.alien_points = 50

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)