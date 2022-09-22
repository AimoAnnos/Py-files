import pygame
from pygame.sprite import Sprite
import random

class Alien(Sprite):
    def __init__(self,game):
        super().__init__()
        self.screen = game.screen
        self.image = pygame.image.load('images/alien.png').convert_alpha()
        #self.image.set_colorkey((230,230,230)) # make transparent
        self.image.set_alpha(random.randint(100,255)) # random transparency
        
        self.settings = game.settings
            
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width # 60px from left edge (at x pos 60)
        self.rect.y = self.rect.height # 58

        self.x = float(self.rect.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True


    def update(self):
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
