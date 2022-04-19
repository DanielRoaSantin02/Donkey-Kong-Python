import pyxel
class Pauline:
    def __init__(self):
        ''' variables de Pauline:
            su posición en el eje x
            su posición en el eje y 
            '''
        self.x=88
        self.y=25
        
    def draw(self):
        pyxel.blt(self.x, self.y, 0, 48, 0, 16, 24)
