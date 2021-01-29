import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """Represent a single star."""
    def __init__(self, game_settings, screen):
        """Initialize the star and set position of the first one"""
        super().__init__()
        self.screen = screen
        self.game_settings = game_settings
    
        #Load the star image and difine its rect attribute
        self.image = pygame.image.load('images/star.png')
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.rect = self.image.get_rect()
        
        #Initialize first star near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #Store the exact position of the star
        self.x = float(self.rect.x)
        
    def blitme(self):
        """Display the star"""
        self.screen.blit(self.image, self.rect)
