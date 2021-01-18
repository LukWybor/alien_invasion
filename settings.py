class Settings():
    """Store all settings"""
    
    def __init__(self):
        """Initialize the game's settings"""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (100,160,180)
        self.ship_speed_factor = 1.5
        #bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (200,60,60)
        self.bullets_allowed = 3
