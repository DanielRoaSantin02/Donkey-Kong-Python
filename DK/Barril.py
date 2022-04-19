import random
import pyxel
from Tablero import Tablero

class Barril:
    def __init__(self):
        ''''variables básicas de los barriles'''
        self.tablero=Tablero()
        self.x=50
        self.y=50
        self.izquierda=False
        self.bajandoescalera=False
        self.primeraescalera=0
        self.marioencima = False
        
    def draw(self):
        pyxel.blt(self.x, self.y+2, 0, 98, 54, 12, 10)   

    def Hay_Viga(self,y,x):
        '''print("hayViga ",y, " ", x , ' ' , self.tablero.Matriz[y+16][x])'''
        if self.tablero.Matriz[self.y+11][self.x+5]==1:
            self.y=self.y-1
        elif self.tablero.Matriz[self.y+12][self.x+5]==1:
            self.hayviga=True
        else:
            self.hayviga=False
        return self.hayviga
    
    def Hay_Escalera(self,y,x):
        if self.tablero.Matriz[self.y+19][self.x+5]==2:
            self.hayescalera=True
        else:
            self.hayescalera=False
        return self.hayescalera
    
    def movimiento(self):
        self.piesenelsuelo = self.Hay_Viga(self.y,self.x)
        
        if self.piesenelsuelo==False:
            self.y=self.y+1
        else:
            self.bajandoescalera=False
            
        if self.Hay_Escalera(self.y,self.x):
            self.primeraescalera+=1
            if self.primeraescalera==1:
                a=random.randint(1,2)
                if a==1:
                    self.bajandoescalera=True
                    self.izquierda=not(self.izquierda)
        else:
            self.primeraescalera=0
            self.bajandoescalera=False
                
        if self.bajandoescalera:
            self.y=self.y+2
           
        else:    
            if self.x==210:
                self.izquierda=True
            elif self.x==0:
                self.izquierda=False
            if self.izquierda==False:     
                self.x=self.x+2
            else:
                self.x=self.x-2
                
    def contacto(self, xmario, ymario):
        mariocentrox=xmario+6
        mariocentroy=ymario-8
        barrilcentrox=self.x+6
        barrilcentroy=self.y-5
        return abs(mariocentrox-barrilcentrox)<8 and abs(mariocentroy-barrilcentroy)<8
            
    def encima(self, xmario, ymario):
        mariocentrox=xmario+6
        mariocentroy=ymario-8
        barrilcentrox=self.x+6
        barrilcentroy=self.y-5
        encima = (abs(barrilcentrox - mariocentrox) <= 1) and (0<= (barrilcentroy - mariocentroy) < 30)
        if encima:
            if self.marioencima:
                encima = False
            else:
                self.marioencima = True
        else:
            self.marioencima = False
        return encima
        
                
    def barrilmuerto(self):
        return self.x<10 and self.y>220
            