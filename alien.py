import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Represent a single alien in the fleet."""
    def __init__(self, game_settings, screen):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = screen
        self.game_settings = game_settings
    
        #Load the alien image and difine its rect attribute
        self.image = pygame.image.load('images/alien.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        
        #Initialize each new alien near the top left of the screen
        self.rect.x = self.rect.width - 20
        self.rect.y = self.rect.height - 50
        
        #Store the exact position of the alien
        self.x = float(self.rect.x)
        
    def blitme(self):
        """Display the alien at his current position"""
        self.screen.blit(self.image, self.rect)
