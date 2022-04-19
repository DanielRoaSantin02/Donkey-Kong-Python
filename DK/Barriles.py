from Tablero import Tablero
class Barriles:
    def __init__(self):
        ''''variables básicas de los barriles'''
        self.tablero=Tablero()
        self.x=60
        self.y=50
        self.direccion=False
        
    def Hay_Viga(self,y,x):
        '''print("hayViga ",y, " ", x , ' ' , self.tablero.Matriz[y+16][x])'''
        if self.tablero.Matriz[self.y+11][self.x+5]==1:
            self.y=self.y-1
        elif self.tablero.Matriz[self.y+12][self.x+5]==1:
            self.hayviga=True
        else:
            self.hayviga=False
        return self.hayviga
    
    def movimiento(self):
        self.piesenelsuelo = self.Hay_Viga(self.y,self.x)
        if self.piesenelsuelo==False:
            self.y=self.y+1
            
        if self.x==210:
            self.direccion=True
        elif self.x==0:
            self.direccion=False
            
        if self.direccion==False:     
            self.x=self.x+1
        else:
            self.x=self.x-1