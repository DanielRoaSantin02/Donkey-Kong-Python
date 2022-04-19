from Tablero import Tablero
import pyxel
class Mario:
    def __init__(self):
        '''variables de Mario:
            su posición en el eje x
            su posición en el eje y
            si está vivo o no
            si está mirando a la derecha o no
            si está corriendo o no
        '''
        self.tablero=Tablero()
        self.x=1
        self.y=232
        self.hayviga=None
        self.hayescalera=None
        self.piesenelsuelo=False
        self.subiendoescalera=False
        self.derecha=True
        self.correr=False
        self.contador=0
        self.saltando=False
        
    def draw(self):
        if self.derecha==True:
            if self.correr==False:
                pyxel.blt(self.x, self.y, 0, 0, 0, 16, 16)              
            else:
                pyxel.blt(self.x, self.y, 0, 0, 16, 16, 16) 
        else:
            if self.correr==False:
                pyxel.blt(self.x, self.y, 0, 16, 0, 16, 16)              
            else:
                pyxel.blt(self.x, self.y, 0, 16, 16, 16, 16)

    def Hay_Viga(self,y,x):
        '''print("hayViga ",y, " ", x , ' ' , self.tablero.Matriz[y+16][x])'''
        if self.tablero.Matriz[self.y+15][self.x+8]==1:
            self.y=self.y-1 
        elif self.tablero.Matriz[self.y+16][self.x+8]==1:
            self.hayviga=True
        else:
            self.hayviga=False            
        return self.hayviga
    
    def Hay_Escalera(self,y,x):
        print("hayViga ",y, " ", x , ' ' , self.tablero.Matriz[y+14][x+8])
        if self.tablero.Matriz[y+15][x+8]==2 or self.tablero.Matriz[y+16][x+8]==2:
            self.hayescalera=True
        else:
            self.hayescalera=False
        return self.hayescalera
    
    def Hay_EscaleraDebajo(self,y,x):
        print("hayViga ",y, " ", x , ' ' , self.tablero.Matriz[y+14][x+8])
        if self.tablero.Matriz[y+19][x+8]==2:
            self.hayescaleradebajo=True
        else:
            self.hayescaleradebajo=False
        return self.hayescaleradebajo
        
    def movimiento(self,izquierda,derecha,arriba,abajo,espacio):
        if izquierda:
            self.x = max(self.x - 2, 0)
            self.derecha=False
            if self.correr==True:
                self.correr=False
            else:
                self.correr=True
        if derecha:
            self.x = min(self.x + 2, 210)
            self.derecha=True
            if self.correr==True:
                self.correr=False
            else:
                self.correr=True
         
        
        self.subiendoescalera=self.Hay_Escalera(self.y,self.x) 
        self.piesenelsuelo = self.Hay_Viga(self.y,self.x) 
       
     
        if self.subiendoescalera==True:
            if arriba:
                self.y=self.y-1
            if abajo:
                self.y=self.y+1
                
        if self.piesenelsuelo==True:
            if espacio:
                self.contador=0
                self.saltando=True  
                
        if self.piesenelsuelo and self.Hay_EscaleraDebajo(self.y,self.x):
            if abajo:
                self.y=self.y+1
                
        if self.subiendoescalera==False and self.piesenelsuelo==False:
            self.y=self.y+1
        
        
            
        if self.saltando==True and self.contador<10:
            self.y = self.y-3
            self.contador+=1
        else:
            self.piesenelsuelo=False
            self.saltando=False
            

            
            
    def contactoPauline(self):
        if self.x<=100 and self.y==32:
            return True


    