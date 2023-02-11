
# x1=1
# x2=2
# y1=3
# y2=4
class massSensor:
    def __init__(self,x1,y1,x2,y2):
        #reading (x) and the mass (y) of the scale for two different masses.
        self.x1 = x1 
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


    def getMB(self):# finding the m and the b of the line
        m = (self.y2-self.y1)/(self.x2-self.x1)
        b = (self.y1 - (m*self.x1))
        return m, b 

    def ymass(self,x): # using the m and the b in the equation of the line to get the y which is the mass 
        m,b = self.getMB()
        y = m*x + b
        return y

# sensor1 = massSensor(2,2,3,3)

# print(sensor1.ymass(7))


