import sys
import pygame

def run_game():
    #Initialize the game and create a screen object
    pygame.init()
    screen = pygame.display.set_mode((1200,600))
    pygame.display.set_caption("Alien invasion")
    
    #Starting the main game loop
    while True:
        
        #Waiting to press a key or mouse button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        #Display the last modified screen
        pygame.display.flip()
        
run_game()
