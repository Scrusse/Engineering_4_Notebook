#type ignore
import adafruit_mpu6050
import busio
import digitalio
from digitalio import DigitalInOut, Direction, Pull
import time
import board

led = digitalio.DigitalInOut(board.GP16)
led.direction = digitalio.Direction.OUTPUT
sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c)

while True:
    accelerationVals = mpu.acceleration
    
    print(f"X {accelerationVals[0]}")
    print(f"Y {accelerationVals[1]}")
    print(f"Z {accelerationVals[2]}")
    print("")
    time.sleep(.20)

    if accelerationVals[2] <= 1:
        led.value = True
    else:
        led.value = False