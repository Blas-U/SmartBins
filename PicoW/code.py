import time
import board
import digitalio
from hx711_gpio import *
from GETLogger import *
from massSensor import *
from gridAwe import *
#this is the "LOGTOSEVER" code


# set up data structure
data = {}
data["picoID"] = "HayHay"
data["sensor"] = "Mass"
data["reading"] = ""
data["units"] = "g"

# setup pins
pin_OUT = digitalio.DigitalInOut(board.GP5)
pin_SCK = digitalio.DigitalInOut(board.GP6)
pin_SCK.direction = digitalio.Direction.OUTPUT



hx = HX711(pin_SCK, pin_OUT)
hx.OFFSET = 0 # -150000
hx.set_gain(128)
time.sleep(0.050)
#scale = 25000.0



logger = GETLogger("TFS Students", "Fultoneagles", "http://popu.local/WWT/webpage/logger.php")

#calabrate the sensor using reading (x) and the mass (y) of the scale for two different masses.
sensor = massSensor(652055,1510,911010,2084)
old_mass=0
#set up LEDs
grid=gridAwe()
grid.hourglass()

while True:
    try:
        #scale equation
        x = hx.read()
        real_mass = int(round (sensor.ymass(x),-1))

        # real_mass = sensor.getMB()*x+63.5
#EACH SCALE HAST TO BE CALIBRATED I.E A 20Kg SCALE WILL HAVE A DIFFERENT EQUATION TO A 5Kg SCALE.
        if old_mass != real_mass:
           #code below if for LEDs
            grid.hourglass(True)
            time.sleep(1)
            grid.blankScreen()
            grid.hourglass()
            #sends data
            time.sleep(5)
            x = hx.read()
            real_mass = int(round (sensor.ymass(x),-1))
            data["reading"] = real_mass
            logger.log(data)
            #grid.smileyFace()
            
             
        old_mass = real_mass
        time.sleep(1)
    except Exception as e:
        print("Error:\n", str(e))

