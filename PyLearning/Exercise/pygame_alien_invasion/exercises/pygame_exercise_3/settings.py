class Settings(object):

    def __init__(self):

        # Screen settings
        self.screen_width = 800
        self.screen_height = 1200
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 0.4

        # Bullet settings
        self.bullet_speed = 0.4
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 4