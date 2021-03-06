import pygame

class Ship():
    
    def __init__(self, game_settings, screen):
        """Initialize the ship and set its starting position"""
        self.screen = screen
        self.game_settings = game_settings
        
        #Load the ship image and get its rectangle
        self.image = pygame.image.load('images/ship.png')
        self.image = pygame.transform.scale(self.image, (30, 60))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #Initialize new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 20
        
        #Store a decimal value for the ship's center
        self.center = float(self.rect.centerx)
        
        #Movement flag
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """Update the ship's position based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.game_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.game_settings.ship_speed_factor
        
        self.rect.centerx = self.center
        
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
