import pyxel

class Escaleras:
    def __init__(self):
        ''' variables de las escaleras '''
        self.xinicial=168
        self.yinicial=240
        
    def draw(self):
        xfilae1=self.xinicial
        rango=3
        for i in range(2):    
            yfilae1=self.yinicial
            for i in range(rango):
                pyxel.blt(xfilae1, yfilae1, 0, 96, 24, 8, 8)
                yfilae1=yfilae1-8
            xfilae1=self.xinicial-96
            rango=4
            
        xfilae2=136
        yfilae2=220
        rango=5
        for i in range(2):            
            for i in range(rango):
                pyxel.blt(xfilae2, yfilae2, 0, 96, 24, 8, 8)
                yfilae2=yfilae2-8
            xfilae2=xfilae2-80
            yfilae2=215
            rango=4
            
        xfilae3=self.xinicial
        yfilae3=172
        rango=3
        for i in range(2):            
            for i in range(rango):
                pyxel.blt(xfilae3, yfilae3, 0, 96, 24, 8, 8)
                yfilae3=yfilae3-8
            xfilae3=xfilae3-80
            yfilae3=177
            rango=4
                
        xfilae4=136
        yfilae4=148
        rango=5
        for i in range(2):            
            for i in range(rango):
                pyxel.blt(xfilae4, yfilae4, 0, 96, 24, 8, 8)
                yfilae4=yfilae4-8
            xfilae4=xfilae4-80
            yfilae4=143
            rango=4
            
        xfilae5=self.xinicial
        yfilae5=100
        rango=3
        for i in range(2):            
            for i in range(rango):
                pyxel.blt(xfilae5, yfilae5, 0, 96, 24, 8, 8)
                yfilae5=yfilae5-8
            xfilae5=xfilae5-80
            yfilae5=105
            rango=4
            
        xfilae6=144
        yfilae6=74
        rango=4                   
        for i in range(rango):
            pyxel.blt(xfilae6, yfilae6, 0, 96, 24, 8, 8)
            yfilae6=yfilae6-8

