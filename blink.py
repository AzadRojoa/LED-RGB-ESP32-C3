from machine import Pin
from time import sleep
from neopixel import NeoPixel
pine = Pin(8, Pin.OUT)                          # Pin number for v1 of the above DevKitC, use pin 38 for v1.1
np = NeoPixel(pine, 1)                            # "1" = one RGB led on the "led bus"
np[0] = (0,1,1)
np.write()
sleep(1)
np[0] = (0,0,0)
np.write()
sleep(1)
