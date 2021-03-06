import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	
    #Initialize the game and create a screen object
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, 
        game_settings.screen_height))
    pygame.display.set_caption("Alien invasion")
    
    #Make a ship
    ship = Ship(game_settings, screen)
    
    #Bullets are stored in group
    bullets = Group()
    #Aliens are stored in group
    aliens = Group()
    
    #Stars are stored in group
    stars = Group()
    
    #Creating the fleet of aliens
    gf.create_fleet(game_settings, screen, ship, aliens)
    #Creating stars
    gf.create_stars(game_settings, screen, stars)
    
    #Starting the main game loop
    while True: 
        gf.check_events(game_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(game_settings, aliens)  
        gf.update_screen(game_settings, screen, stars, ship, aliens, bullets)
        
run_game()
