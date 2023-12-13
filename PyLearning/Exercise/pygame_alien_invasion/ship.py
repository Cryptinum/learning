# Creating ship.

import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        super().__init__()

        # pygame can treat all elements like rectangles (rects).
        # ai_game is to give a reference to the instance of AlienInvasion.
        # Attention: ai_game is a instance, a parameter
        #            self is an attribute.
        self.screen = ai_game.screen # Assign to an attribute of Ship class.
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        # pygame.image.load returns a surface representing the ship.
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect() # Call get_rect to access the ship's rect.

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's x value rather than rect.
        # Limiting the ship's range by add a comparison.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Then update the rect from x value.
        # rect will store only the integer portion, but it's OK for displaying.
        self.rect.x = self.x

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the ship at its current loaction."""
        self.screen.blit(self.image, self.rect)