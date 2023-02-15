import board
import neopixel
import time

class gridAwe:
    def __init__(self):
        self.npix=16*16
        # even: y=16r-c, odd: y=16r-17+c
        # even: y=16x-2, odd: y=16x-15
        self.pixels = neopixel.NeoPixel(board.GP0, self.npix)
        self.r= (100,0,0) #red 
        self.b= (0,0,50) #blue
        self.g= (0,100,0) #green
        self.p= (50,0,50) #purple
        self.y= (50,50,0) #yellow
        self.o= (70,30,0) #orange
        self.w= (33,33,33) #white
        self.pi= (80,20,20) #pink
        self.t= (0,70,30) #teal

    def pix(self,r,c,col= (10,0,0)):
        if (r %2)==0:
            y=16*r-c
        else:
            y=16*r-17+c
        self.pixels[y] = col
    
#pix(1,1)    #bottom corner pixel
    
    



    def smileyFace(self):
        g= (0,100,0) #green
        grid= [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,g,0,0,0,0,g,0,0,0,0,0],
            [0,0,0,0,0,g,0,0,0,0,g,0,0,0,0,0],
            [0,0,0,0,0,g,0,0,0,0,g,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,g,0,0,0,0,0,0,0,0,0,0,0,0,g,0],
            [0,g,0,0,0,0,0,0,0,0,0,0,0,0,g,0],
            [0,0,g,0,0,0,0,0,0,0,0,0,0,g,0,0],
            [0,0,0,g,0,0,0,0,0,0,0,0,g,0,0,0],
            [0,0,0,0,g,g,g,g,g,g,g,g,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        self.drawGrid(grid)

    def defaultColor(self):
        for i in range (1,17):
            for j in range (16,0,-1):
                self.pix(i,j,self.b)

    def drawGrid(self,grid):
        for i in range (1,17):
            for j in range (16,0,-1):
                if (grid[15-i][j-1])!=0:
                    self.pix(i,j,grid[15-i][j-1])
