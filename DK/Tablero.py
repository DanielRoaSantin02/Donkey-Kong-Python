from Escaleras import Escaleras
class Tablero:
    def __init__(self):
        ''' Aquí se creará la matriz para comprobar las colisiones de Mario con las plataformas del escenario'''
        self.Matriz = []
        self.escaleras=Escaleras()
        self.xinicial=0
        self.yinicial=248
        for i in range(256):
            self.Matriz.append([])
            for j in range(224):
                self.Matriz[i].append(0) 
        self.MatrizEnorme()
    
    def MatrizEnorme(self):
        '''Aquí se crearan las vigas y escaleras dentro de la matriz'''
        
        self.xfilae1=self.escaleras.xinicial+8
        self.yfilae1=self.escaleras.yinicial
        rango=3
        for i in range(2):                
            for i in range(rango):
                self.ymatriz=self.yfilae1
                self.xmatriz=self.xfilae1
                for i in range(9):
                    self.ymatriz=self.ymatriz+1
                    self.xmatriz=self.xmatriz-8
                    for j in range(8):
                        self.xmatriz=self.xmatriz+1
                        self.Matriz[self.ymatriz][self.xmatriz]=2
                self.yfilae1=self.yfilae1-9
            self.xfilae1=self.escaleras.xinicial-88
            self.yfilae1=self.escaleras.yinicial+2
            rango=4
            
        self.xfilae2=144
        self.yfilae2=213
        rango=5
        for i in range(2):            
            for i in range(rango):
                self.ymatriz=self.yfilae2
                self.xmatriz=self.xfilae2
                for i in range(9):
                    self.ymatriz=self.ymatriz+1
                    self.xmatriz=self.xmatriz-8
                    for j in range(8):
                        self.xmatriz=self.xmatriz+1
                        self.Matriz[self.ymatriz][self.xmatriz]=2
                self.yfilae2=self.yfilae2-8
            self.xfilae2=self.xfilae2-80
            self.yfilae2=209
            rango=4
            
        self.xfilae3=self.escaleras.xinicial+8
        self.yfilae3=173
        rango=4
        for i in range(2):            
            for i in range(rango):
                self.ymatriz=self.yfilae3
                self.xmatriz=self.xfilae3
                for i in range(9):
                    self.ymatriz=self.ymatriz+1
                    self.xmatriz=self.xmatriz-8
                    for j in range(8):
                        self.xmatriz=self.xmatriz+1
                        self.Matriz[self.ymatriz][self.xmatriz]=2
                self.yfilae3=self.yfilae3-8
            self.xfilae3=self.xfilae3-80
            self.yfilae3=177
            rango=5
            
        self.xfilae4=144
        self.yfilae4=141
        rango=5
        for i in range(2):            
            for i in range(rango):
                self.ymatriz=self.yfilae4
                self.xmatriz=self.xfilae4
                for i in range(9):
                    self.ymatriz=self.ymatriz+1
                    self.xmatriz=self.xmatriz-8
                    for j in range(8):
                        self.xmatriz=self.xmatriz+1
                        self.Matriz[self.ymatriz][self.xmatriz]=2
                self.yfilae4=self.yfilae4-8
            self.xfilae4=self.xfilae4-80
            self.yfilae4=137
            rango=4
            
        self.xfilae5=self.escaleras.xinicial+8
        self.yfilae5=102
        rango=4
        for i in range(2):            
            for i in range(rango):
                self.ymatriz=self.yfilae5
                self.xmatriz=self.xfilae5
                for i in range(9):
                    self.ymatriz=self.ymatriz+1
                    self.xmatriz=self.xmatriz-8
                    for j in range(8):
                        self.xmatriz=self.xmatriz+1
                        self.Matriz[self.ymatriz][self.xmatriz]=2
                self.yfilae5=self.yfilae5-8
            self.xfilae5=self.xfilae5-80
            self.yfilae5=104
            rango=4
            
        self.xfilae6=144+8
        self.yfilae6=72
        rango=4                   
        for i in range(rango):
            self.ymatriz=self.yfilae6
            self.xmatriz=self.xfilae6
            for i in range(9):
                self.ymatriz=self.ymatriz+1
                self.xmatriz=self.xmatriz-8
                for j in range(8):
                    self.xmatriz=self.xmatriz+1
                    self.Matriz[self.ymatriz][self.xmatriz]=2
            self.yfilae6=self.yfilae6-8
        
        
        self.yfila35=self.yinicial-60
        for i in range(2):
            self.xfila35=self.xinicial+32
            for i in range(12):
                self.ymatriz=self.yfila35-1               
                for i in range(1):
                    self.ymatriz=self.ymatriz+1
                    self.xmatriz=self.xfila35-1
                    for j in range(16):
                        self.xmatriz=self.xmatriz+1
                        self.Matriz[self.ymatriz][self.xmatriz]=1 
                self.xfila35=self.xfila35+16
                self.yfila35=self.yfila35-1
            self.yfila35=self.yfila35-60
            
        self.yfila246=self.yinicial-36
        for i in range(2):
            self.xfila246=self.xinicial
            for i in range(12):
                self.ymatriz=self.yfila246-1               
                for i in range(1):
                    self.ymatriz=self.ymatriz+1
                    self.xmatriz=self.xfila246-1
                    for j in range(16):
                        self.xmatriz=self.xmatriz+1
                        self.Matriz[self.ymatriz][self.xmatriz]=1 
                self.xfila246=self.xfila246+16
                self.yfila246=self.yfila246+1
            self.yfila246=self.yfila246-84
            
        self.yfila7=47   
        self.xfila7=88
        for i in range(4):
            self.ymatriz=self.yfila7-1            
            for i in range(1):
                self.ymatriz=self.ymatriz+1
                self.xmatriz=self.xfila7-1
                for j in range(16):
                    self.xmatriz=self.xmatriz+1
                    self.Matriz[self.ymatriz][self.xmatriz]=1  
            self.xfila7=self.xfila7+16
            
        
        
        self.yfila16=self.yinicial
        rango=14
        for i in range(2):
            self.xfila16=self.xinicial
            for i in range(rango):
                self.ymatriz=self.yfila16-1               
                for i in range(1):
                    self.ymatriz=self.ymatriz+1
                    self.xmatriz=self.xfila16-1
                    for j in range(16):
                        self.xmatriz=self.xmatriz+1
                        self.Matriz[self.ymatriz][self.xmatriz]=1                      
                self.xfila16=self.xfila16+16
            self.yfila16=self.yfila16-168
            rango=12
            
