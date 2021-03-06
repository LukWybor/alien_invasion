import sys

import pygame
import random

from bullet import Bullet
from alien import Alien
from star import Star


def check_keydown_events(event, game_settings, screen, ship, bullets):
    """Respond to keypresses"""
    
    #Move the ship to the right
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
        
    #Move the ship to the left
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
        
    #Create a new bullet and add it to the bullets group
    elif event.key == pygame.K_SPACE:
        fire_bullet(game_settings, screen, ship, bullets)
    #Close the game
    elif event.key == pygame.K_q:
        sys.exit()
        
def check_keyup_events(event, ship):
    """Respond to key releases"""
    
    #Stops moving the ship to the right
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
        
    #Stops moving the ship to the left
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
        
def fire_bullet(game_settings, screen, ship, bullets):
    """Fire a bullet if the set limit is not reached."""
    if len(bullets) < game_settings.bullets_allowed:
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)   
    
def check_events(game_settings, screen, ship, bullets):
    """Reaction to events generated by pressing a key 
    or a mouse button"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_settings, screen, ship, 
            bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(game_settings, screen, stars, ship, aliens, bullets):
    """Update images on the screen and flip to the new screen"""
    #Refresh the screen during each iteration of the loop
    screen.fill(game_settings.bg_color)
    #Redraw all bullets behind ship and alliens
    stars.draw(screen)
    
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        
    ship.blitme()
    aliens.draw(screen)


    #Display the last modified screen
    pygame.display.flip()
    
def update_bullets(bullets):
    """Update position of the bullets and remove bullets 
    that disappeared from the screen."""
    #Update bullets position
    bullets.update()
    #Delete bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            
def get_number_alien_x(game_settings, alien_width):
    """Get number of aliens in a row"""
    available_space_x = game_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(game_settings, ship_height, alien_height):
    """Get number of rows"""
    available_space_y = (game_settings.screen_height - 
    (alien_height) - ship_height)
    number_rows = int(available_space_y / (alien_height * 2))
    return number_rows

def create_alien(game_settings, screen, aliens, alien_number, 
    row_number):
    """Create an alien and place it in the row"""
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    alien_heght = alien.rect.height
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + alien.rect.height * row_number -50
    aliens.add(alien)
    
def create_fleet(game_settings, screen, ship, aliens):
    """Create the full fleet of aliens"""
    #Create an alien and find the number of aliens in a row
    #Distance between aliens is equal to width of one alien
    alien = Alien(game_settings, screen)
    number_aliens_x = get_number_alien_x(game_settings, 
        alien.rect.width)
    number_rows = get_number_rows(game_settings, ship.rect.height,
        alien.rect.height)
    
    #Create the first row of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(game_settings, screen, aliens, alien_number, 
                row_number)
                
def check_fleet_edges(game_settings, aliens):
    """Respond appropriately if any aliens have reached an edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(game_settings, aliens)
            break
            
def change_fleet_direction(game_settings, aliens):
    """Drop the entire fleet down and change the fleet's direction"""
    for alien in aliens.sprites():
        alien.rect.y += game_settings.fleet_drop_speed
    game_settings.fleet_direction *= -1

def update_aliens(game_settings, aliens):
    """Check if the fleet is at an edge and update the positions of all
     aliens in the fleet"""
    check_fleet_edges(game_settings, aliens)
    aliens.update()

#STARS

def get_number_star_x(game_settings, star_width):
    """Get number of stars in a row"""
    available_space_x = game_settings.screen_width
    number_stars_x = int(available_space_x / (15 * star_width))
    return number_stars_x

def get_number_rows_star(game_settings, star_height):
    """Get number of rows with stars"""
    available_space_y = game_settings.screen_height
    number_rows_star = int(available_space_y / (12 * star_height))
    return number_rows_star

def create_star(game_settings, screen, stars, star_number, 
    row_number):
    """Create a star and place it in the row"""
    star = Star(game_settings, screen)
    star_width = star.rect.width
    star_height = star.rect.height
    star.x = ((random.randint(5, 10) * star_width) + 
        (random.randint(5,40) * star_width) * star_number)
    star.rect.x = star.x
    star.rect.y = ((random.randint(1, 5) * star.rect.height) +
        (random.randint(10, 40) * star.rect.height) * row_number)
    stars.add(star)
    
def create_stars(game_settings, screen, stars):
    """Create stars"""
    #Create a star and find the number of stars in a row
    star = Star(game_settings, screen)
    number_stars_x = get_number_star_x(game_settings, 
        star.rect.width)
    number_rows = get_number_rows_star(game_settings, star.rect.height)
    
    #Create the first row of stars
    for row_number in range(number_rows):
        for star_number in range(number_stars_x):
            create_star(game_settings, screen, stars, star_number, 
                row_number)
