class Settings:
    """Class storing all settings for AI"""

    def __init__(self):
        """Initializing the game's static settings"""
        # Screen settings:
        self.screen_width = 600
        self.screen_height = 1000
        self.bg_color = (177, 155, 217)

        # Ship settings:
        self.ship_limit = 2
        self.spawn_ship = True

        # Bullet settings:
        self.bullet_width = 4
        self.bullet_height = 20
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 7
        self.god_bullet_on = False

        # Alien settings:
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def god_bullet(self):
        """Changes bullets to GOD BULLETS"""
        self.bullet_speed = 5
        self.bullet_width = 40
        self.bullet_height = 100
        self.god_bullet_on = True

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = .75
        self.bullet_speed = 1.5
        self.alien_speed = .2

        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

    
    