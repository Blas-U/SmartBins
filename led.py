print("Hello World! x")
import board
import neopixel

pixels = neopixel.NeoPixel(board.GP0, 29)

for i in range(14):
  pixels[i] = (50,0,0)
for i in range(14, 29):
  pixels[i] = (0,0,50)