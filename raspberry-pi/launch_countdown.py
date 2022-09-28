#type ignore
import time
import board
import digitalio
from digitalio import DigitalInOut, Direction, Pull
import pwmio
from adafruit_motor import servo

button = digitalio.DigitalInOut(board.GP0)
button.pull = digitalio.Pull.DOWN
led_red = digitalio.DigitalInOut(board.GP16) #tells  the Raspberry Pi which port the red LED is connected to
led_red.direction = digitalio.Direction.OUTPUT
led_green = digitalio.DigitalInOut(board.GP15) #tells  the Raspberry Pi which port the green LED is connected to
led_green.direction = digitalio.Direction.OUTPUT
pwm = pwmio.PWMOut(board.GP1, duty_cycle=2 ** 15, frequency=50)
my_servo = servo.Servo(pwm)

while True:
    if button.value == True:
        for x in range(10, 0, -1): #if I wanted it to end on 0 then I would put a -1 in place of the 0
            print(x) #prints the number x is equal to
            led_red.value = True #turns the red LED on
            time.sleep(0.5)
            led_red.value = False #turns the red LED off
            time.sleep(0.5)

        print("LIFTOFF")
        led_green.value = True #turns the green LED on
        for angle in range(0, 180, 180):
            my_servo.angle = angle
            time.sleep(2)
        for angle in range(180, 0, -180):
            my_servo.angle = angle
            time.sleep(2)
        time.sleep(6) #this is here so the green LED doesn't turn on and then off instantly because the code ends
        led_green.value = False