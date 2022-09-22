import pygame
import random
from explosions import Explosion
from pygame.sprite import Sprite
from time import sleep
from bullet import Bullet

class Ship(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load('images/ship.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom # midbottom, topleft etc
        self.settings = game.settings
        
        self.x = float(self.rect.x)
        # movement flag
        self.moving_right = False
        self.moving_left = False
        self.game = game

    def blitme(self):
        # draws ship  at its current position (toinen param)
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
    
    def ship_hit(self):
        if self.game.stats.ships_left > 1:
            explosion = Explosion(self.game)
            explosion.set_explosion_center_and_obj(self.rect.center, 'ship')  
            self.game.explosions.add(explosion)

            self.game.stats.ships_left -= 1
            self.game.sb.prepare_ships()
            self.game.aliens.empty()
            self.game.bullets.empty()
            self.game.create_fleet()
            self.center_ship()
            #sleep(0.5)
        else:
            self.game.stats.game_active = False
            pygame.mouse.set_visible(True)

    def fire_bullet(self):
        """Creates new bullet instances and adds it to the bullets sprite group"""
        if len(self.game.bullets) < self.game.settings.bullets_allowed:
            new_bullet = Bullet(self.game)
            random.choice(self.game.shooting_sounds).play()
            self.game.bullets.add(new_bullet)

    def update(self):
        "updates the ship's position based on the movement flag"
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x
    