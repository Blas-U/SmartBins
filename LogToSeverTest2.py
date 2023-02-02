import time
import board
import digitalio
from hx711_gpio import *
from GETLogger import *

# set up data structure
data = {}
data["picoID"] = "Scale1"
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
scale = 25000.0



logger = GETLogger("TFS Students", "Fultoneagles", "http://popu.local/logger/logger.php")


while True:
    try:
        #scale equation
        mass = hx.read()/scale
        x = 3.58636 + mass
        real_mass = (x-.26854061)/0.01628224
#EACH SCALE HAST TO BE CALIBRATED I.E A 20Kg SCALE WILL HAVE A DIFFERENT EQUATION TO A 5Kg SCALE.
        data["reading"] = real_mass
        logger.log(data)
        time.sleep(5)
    except Exception as e:
        print("Error:\n", str(e))
