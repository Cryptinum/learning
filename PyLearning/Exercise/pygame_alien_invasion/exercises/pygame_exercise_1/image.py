import pygame

class Image(object):

    def __init__(self, whole_screen, path='images/rio.jpg'):

        self.screen = whole_screen.screen
        self.settings = whole_screen.settings
        self.screen_rect = whole_screen.screen.get_rect()

        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()

        self.rect.x = -600
        self.rect.y = -120
        
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right > self.screen_rect.right:
            self.x -= self.settings.moving_speed
        if self.moving_left and self.rect.left < 0:
            self.x += self.settings.moving_speed
        if self.moving_up and self.rect.top < 0:
            self.y += self.settings.moving_speed
        if self.moving_down and self.rect.bottom > self.screen_rect.bottom:
            self.y -= self.settings.moving_speed
            
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)