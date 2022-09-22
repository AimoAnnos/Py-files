import pygame

# import os.path
# img_dir = os.path.join(os.path.dirname(__file__), "images")

class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 666
        self.bg_color = (0,230,230)
            
        #self.bg_image = pygame.image.load(os.path(img_dir,"starba.png")).convert()

        # Ship settings 
        #self.ship_speed = 1.5
        self.ship_limit = 3
        
        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 500
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 50

        # Alien settings
        #self.alien_speed = 1.0
        self.fleet_drop_speed = 10 # how many px fleet drops after hitting the edge
        #self.fleet_direction = 1 # 1=right, -1=left

        # Difficulty settings

        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.setup_dynamic_settings()

        # UI text settings
        self.font = pygame.font.SysFont(None, 40) # font and size
        # self.font = pygame.font.Font('comicsans.ttf', 48)

    def setup_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 1.0
        self.alien_speed = 1.0
        self.alien_pts = 10
        self.fleet_direction = 1
    
    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_pts = int(self.alien_pts * self.score_scale)