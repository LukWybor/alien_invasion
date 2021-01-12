import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Manage fired bullets"""
    
    def __init__(self, game_settings, screen, ship):
        """Create a bullet object at the ship's position"""
        super().__init__()
        self.screen = screen

        #Create a bullet rect at (0,0)
        self.rect = pygame.Rect(0,0, ai_settings.bullet_width, 
        ai_settings.bullet_height)
        #Set correct position of the bullet
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        #Bullet's position as a decimal value
        self.y = float(self.rect.y)
        
        self.color = game_settings.bullet_color
        self.speed_factor = game_settings.bullet_speed_factor
