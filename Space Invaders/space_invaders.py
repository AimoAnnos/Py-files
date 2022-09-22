import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
from game_texts import UIText
import os.path

from game_stats import GameStats
from explosions import Explosion
from button import Button
from scoreboard import Scoreboard

class SpaceInvaders:
    """class to manage assets and behaviour"""
    def __init__(self):
        pygame.init() # must!!!
        pygame.mixer.init()
        pygame.display.set_caption("Space Invaders") # title
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) # = set_reso ((pixe,lit))
        self.bg_image = pygame.image.load('images/starfield.png').convert_alpha() # convert_alpha .png:eille
        # fullscreen
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        self.play_button = Button(self, 'Start')
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group() # group jonne lisätään alien oliot(alempana)
        self.explosions = pygame.sprite.Group()
        self.create_fleet()
        self.stats = GameStats(self)
        self.stats.highscore = int(self.get_highscore())
        self.sb = Scoreboard(self)
        self.bg_color = (self.settings.bg_color) # RBG
        self.ui_text = UIText(self)
        
        self.setup_sounds()
              
        #self.play_button = Button(self.screen, 100,100,300,150, text='Start the shit', fontSize=60, inactiveColour=(200, 50, 0), \
            #hoverColour=(150, 0, 0),pressedColour=(0, 200, 20),onClick=lambda: self.make_active)

    def run_game(self):
        pygame.mixer.music.play(loops= -1)
        """Main loop"""
        while True:
            self.check_events() # keyboard + mouse events
            if self.stats.game_active: # only when game_active == True
                self.ship.update()
                self.update_bullets()
                self.update_aliens()
                self.explosions.update()
            self.update_screen() # screen update anyway
    
    def get_highscore(self):
        try:
            with open('highscore.txt', 'r+') as f:
                highscore = f.readline()
                if highscore == "":
                    highscore = 0
                    print("no highscore found, setting it to 0")
                return highscore
        except:
            raise

    def setup_sounds(self):
        pygame.mixer.music.load("sounds/cyberpunk.wav")
        pygame.mixer.music.set_volume(0.08)

        # effect sounds
        self.shooting_sounds = []
        sound_dir = os.path.join(os.path.dirname(__file__),"sounds")
        for sound in ['laser.wav', 'laser2.wav']:
            self.shooting_sounds.append(pygame.mixer.Sound(os.path.join(sound_dir,sound)))

        for s in self.shooting_sounds:
            s.set_volume(0.1)
        
        self.explosion_sound = pygame.mixer.Sound(os.path.join(sound_dir, 'explosion.wav'))
        self.explosion_sound.set_volume(0.1)

    def check_events(self):
        """Responds to keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()  
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_play_button(mouse_pos)
        
    def check_play_button(self, pos):
        button_clicked = self.play_button.rect.collidepoint(pos)
        if button_clicked and not self.stats.game_active:
            self.settings.setup_dynamic_settings()
            self.sb.prepare_score()
            self.sb.prepare_ships()
            pygame.mouse.set_visible(False)
            self.stats.reset_stats()
            self.stats.game_active = True
            self.aliens.empty()
            self.bullets.empty()
            self.create_fleet()
            self.ship.center_ship()
               
    def check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self.ship.fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()
        
    def check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.moving_left = False

    def create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size # size = tuple(int x, int y)
        ship_height = self.ship.rect.height
        # calculate space; one alien witdh which is removed from left and right edge
        available_space_x = self.settings.screen_width - (2*alien_width) # 1080
        # calculate how many aliens (inclunding empty space (=alien width) fit to row)
        number_of_aliens_x = available_space_x // (2*alien_width)

        # calculate y space; screen.height - 3*alien.height - ship.height
        available_space_y = (self.settings.screen_height - 
                            (3*alien_height) - ship_height) # sulut niin voi laittaa rivinvaihdon

        number_of_aliens_y = available_space_y // (2*alien_height) # number of rows

        #create full fleet
        for row in range(number_of_aliens_y): # 0-3
            for alien_number in range(number_of_aliens_x): # 0-8
                self.create_alien(alien_number,row)
            
    def create_alien(self, alien_number, row):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + (2* alien_width * alien_number)
        alien.rect.x = alien.x
        alien.rect.y = alien_height + (2*alien_height * row)
        self.aliens.add(alien)

    def check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges(): # if True, what happens when colliding with edge:
                self.change_fleet_direction()
                break

    def change_fleet_direction(self): # drop whole fleet and change direction
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed # y + 10px (down)
        self.settings.fleet_direction *= -1 # handy trick to change direction in 1 row (without elif)

    def check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens: # .sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self.ship.ship_hit()
                break

    def check_bullet_alien_collisions(self):
        # bullet collision to alien
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True) # = dictionary
        if collisions:
            for aliens in collisions.values(): # if we hit several aliens at once
                self.stats.score += self.settings.alien_pts *len(aliens)
                for alien in aliens:
                    explosion = Explosion(self)
                    explosion.set_explosion_center_and_obj(alien.rect.center, 'alien')  
                    self.explosions.add(explosion)
                    
            self.sb.prepare_score()
            self.sb.check_highscore()

        # check if no more aliens left -> create new fleet
        if not self.aliens: # is aliens-group (from constructor) empty?
            self.bullets.empty()
            self.create_fleet()
            self.settings.increase_speed()

    def update_aliens(self):
        self.check_fleet_edges()
        self.aliens.update()
        # check for collision
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self.ship.ship_hit()
        self.check_aliens_bottom()
    
    def update_bullets(self):
        self.bullets.update()  # calls every instance's (in bullets) update method
        # Get rid of bullets after they disappear from screen
        for bullet in self.bullets.copy(): # kopioi listan
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        self.check_bullet_alien_collisions()

    def update_screen(self):
        #self.screen.fill(self.bg_color)
        self.screen.blit(self.bg_image,self.screen.get_rect()) # image + srcreen rect
        self.ship.blitme()
        #self.ui_text.update_ship_position_text()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)
        self.explosions.draw(self.screen)
        self.sb.show_score()

        if not self.stats.game_active:
            self.screen.fill(self.bg_color)
            self.play_button.draw_button()

        # make the most recently drawn screen visible = frame juttu
        pygame.display.flip()

if __name__ == '__main__': # only when run directly
    space_invaders = SpaceInvaders()
    space_invaders.run_game() 