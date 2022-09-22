
class UIText:
    def __init__(self, game):
        self.settings = game.settings
        self.screen = game.screen

        self.text_color = (0,0,0) # black
        self.font = self.settings.font
        self.ship = game.ship

    def update_ship_position_text(self):
        coords = str(self.ship.rect.x) # + ',' + str(self.ship.rect.y)
        ship_postion_text = self.font.render(coords,True,self.text_color)
        ship_postion_rect = ship_postion_text.get_rect()
        ship_postion_rect.topleft = (20,20)
        self.screen.blit(ship_postion_text, ship_postion_rect) # blittaa coordit