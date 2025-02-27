"""The Enemies of the game"""

import pygame
from pygame.sprite import Sprite

from setup import resource_path

class Alien(Sprite):
    """A Class to represent a single alien in the fleet."""
    
    def __init__(self, sp_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = sp_game.screen
        self.settings = sp_game.settings
        self.stats = sp_game.stats

        # Sets the alien health
        self.health = self.settings.alien_health
        if self.stats.level > 1:
            self._set_health()

        # Load the alien image and set its rect attribute
        asset_url = resource_path('images/ufo.bmp')
        self.image = pygame.image.load(asset_url)
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Moves the alien to the right."""
        self.x += (self.settings.alien_speed * \
            self.settings.fleet_direction)
        self.rect.x = self.x

    def _set_health(self):
        """Sets the health of the alien so that its scaled up"""
        self.health *= self.settings.difficulty_scale
        
    