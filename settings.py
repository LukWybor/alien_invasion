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
