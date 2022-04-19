import pyxel

class Vigas:
    def __init__(self):
        '''variables para la creación de las vigas:
            su posición en el eje x
            su posición en el eje y
            '''
        self.xinicial=0
        self.yinicial=248
        self.hayviga=False
            
    def draw(self):
        yfila16=self.yinicial
        rango=14
        for i in range(2):
            xfila16=self.xinicial
            for i in range(rango):
                pyxel.blt(xfila16, yfila16, 0, 96, 0, 16, 8)
                xfila16=xfila16+16
            yfila16=yfila16-168
            rango=12
            
        yfila35=self.yinicial-60
        for i in range(2):
            xfila35=self.xinicial+32
            for i in range(12):
                pyxel.blt(xfila35, yfila35, 0, 96, 0, 16, 8)
                xfila35=xfila35+16
                yfila35=yfila35-1
            yfila35=yfila35-60
            
        yfila246=self.yinicial-36
        for i in range(2):
            xfila246=self.xinicial
            for i in range(12):
                pyxel.blt(xfila246, yfila246, 0, 96, 0, 16, 8)
                xfila246=xfila246+16
                yfila246=yfila246+1
            yfila246=yfila246-84
            
        yfila7=47
        xfila7=88
        for i in range(4):
            pyxel.blt(xfila7, yfila7, 0, 96, 0, 16, 8)
            xfila7=xfila7+16

   