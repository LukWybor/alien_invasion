class Settings():
    """Store all settings"""
    
    def __init__(self):
        """Initialize the game's settings"""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (0,70,140)
        self.ship_speed_factor = 4
        #bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0,255,255)
        self.bullets_allowed = 3
        #alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

