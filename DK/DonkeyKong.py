import pyxel

class DonkeyKong:
    def __init__(self):
        '''variables de DK '''
        self.x=20
        self.y=46
        
    def draw(self):
        pyxel.blt(self.x, self.y, 0, 40, 46, 40, 36)
        
    def draw_barriles(self):
        pyxel.blt(0, self.y+2, 0, 115, 48, 20, 36)


   
    