#type ignore
import time
import board
import digitalio

led_red = digitalio.DigitalInOut(board.GP16) #
led_red.direction = digitalio.Direction.OUTPUT
led_green = digitalio.DigitalInOut(board.GP15)
led_green.direction = digitalio.Direction.OUTPUT

for x in range(10, 0, -1): #if I wanted it to end on 0 then I would put a -1 in place of the 0
    print(x) #prints the number x is equal to
    led_red.value = True
    time.sleep(0.5)
    led_red.value = False
    time.sleep(0.5)

print("LIFTOFF")
led_green.value = True
time.sleep(10)