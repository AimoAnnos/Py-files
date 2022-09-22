import pygame
import pygame.font

class Button:
    def __init__(self,game,txt):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 300, 100
        self.button_color = (255,204,153) # rgb
        self.txt_color = (0,0,0)
        self.font = pygame.font.SysFont('helvetica',40)

        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        self.set_button_text(txt)

    def set_button_text(self,txt):
        self.txt = self.font.render(txt,True,self.txt_color,self.button_color)
        self.txt_rect = self.txt.get_rect()
        self.txt_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.txt,self.txt_rect)