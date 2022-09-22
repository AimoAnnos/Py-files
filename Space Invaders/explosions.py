from pygame.sprite import Sprite
import pygame
import os.path

class Explosion(Sprite):
    def __init__(self, game ):
        super().__init__() # kutsutaan spriten konstruktoria
        self.explosion_anim = {} # dict:ssä key + value
        self.explosion_anim['alien'] = []
        self.explosion_anim['ship'] = []
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50 # ms, 8 kuvaa vaihtuu 50 ms välein = yhteensä explosion 400 ms
        self.game = game

        for i in range(9): # 0-8
            filename = 'regularExplosion0{}.png'.format(i) # format lisää numerot 0-8 filun nimen loppuun (vanha tapa)
            #filename = f"regularExplosion{i}.png"
            img = pygame.image.load("images/"+filename).convert_alpha()

            #alien explosion
            img_alien = pygame.transform.scale(img,(60,58)) # scaletaan alien pix kokoon
            self.explosion_anim['alien'].append(img_alien)

            # ship explosion
            img_ship = pygame.transform.scale(img,(120,116)) # scaletaan alien pix kokoon
            self.explosion_anim['ship'].append(img_ship)

    def set_explosion_center_and_obj(self,center,obj):
        self.obj = obj
        self.image = self.explosion_anim[self.obj][0] # sets first alien image
        self.rect = self.image.get_rect()
        self.rect.center = center
   
    def update(self):
        now = pygame.time.get_ticks() # timerin teko
        if now -self.last_update > self.frame_rate: # if 50 ms has passed (timer)
            self.last_update = now # time is reset to 0, running -> 
            self.frame += 1
            if self.frame == len(self.explosion_anim[self.obj]):
                self.kill() # viimeisessä framessa tuhotaan sprite
            else:
                center = self.rect.center
                self.image = self.explosion_anim[self.obj][self.frame] # [alien-listan paikka][indeksi]
                self.rect = self.image.get_rect()
                self.rect.center = center
