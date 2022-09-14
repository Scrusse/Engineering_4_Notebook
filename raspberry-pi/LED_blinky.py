# type: ignore
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED) #
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True #this means that the light is on
    time.sleep (1) #this means there is a pause between actions (specifically one second)
    led.value = False #this means that the light is off
    time.sleep (1) #this means there is another pause between actions (one second again)