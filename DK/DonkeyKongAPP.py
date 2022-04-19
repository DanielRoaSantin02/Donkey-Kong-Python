import pyxel
from Mario import Mario
from Pauline import Pauline
from Vigas import Vigas
from DonkeyKong import DonkeyKong
from Tablero import Tablero
from Barril import Barril
from Escaleras import Escaleras
class Game:
    def __init__(self):
        self.mario=Mario()
        self.pauline=Pauline()
        self.vigas=Vigas()
        self.donkeykong=DonkeyKong()
        self.tablero=Tablero()
        self.escaleras=Escaleras()
        self.barriles=[]
        self.vidas=3
        self.score=0
        pyxel.init(224, 256, caption="Donkey Kong")
        pyxel.load("assets/SpritesDK.pyxres")
        pyxel.playm(0, loop=True)
        pyxel.run(self.update, self.draw)
        
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q) or self.vidas<=0:
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_P):
            print(self.tablero.Matriz)
        self.mario.movimiento(pyxel.btn(pyxel.KEY_LEFT), 
                              pyxel.btn(pyxel.KEY_RIGHT),
                              pyxel.btn(pyxel.KEY_UP),
                              pyxel.btn(pyxel.KEY_DOWN),
                              pyxel.btn(pyxel.KEY_SPACE))
        self.movimientobarriles()
        if self.mario.contactoPauline():
            pyxel.quit()
      
    def draw(self):
        pyxel.cls(0) 
        #dibujar texto del marcador
        pyxel.text(0,0,"VIDAS RESTANTES: ",7)
        pyxel.text(68,0, str(self.vidas), 7)
        pyxel.text(0,8,"SCORE:",7)      
        pyxel.text(32,8, str(self.score), 7)
       
        #dibujar las escaleras
        self.escaleras.draw()                    
        #dibujar a Mario
        self.mario.draw()
        #dibujar los barriles que caigan
        for b in self.barriles:
            b.draw()
        #dibujar a Pauline
        self.pauline.draw()
        #dibujar a DonkeyKong
        self.donkeykong.draw()
        #dibujar los barriles al lado de Donkey Kong
        self.donkeykong.draw_barriles()
        #dibujar las vigas  
        self.vigas.draw()
            
    def movimientobarriles(self):
        if pyxel.frame_count % 75 == 0:
          if  len(self.barriles)<10:
              self.barriles.append(Barril())
        self.muertemario = False
        for b in self.barriles:
            b.movimiento()
            if b.barrilmuerto():
                self.barriles.remove(b)
            if b.contacto(self.mario.x,self.mario.y):
                self.muertemario = True
            if b.encima(self.mario.x,self.mario.y)and self.mario.piesenelsuelo==False:
                self.score+=100
        if self.muertemario:
            self.barriles=[]
            self.mario.x=1
            self.mario.y=232
            self.vidas-=1
        print(self.score)
        
Game()
