import time
from adafruit_servokit import ServoKit

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)
#kit.servo[0].set_pulse_width_range(1000, 2000)
kit.servo[0].actuation_range = 270
x = 100

while True:
    #y = float(input(" "))
    #time.sleep(1)
    #if y >= 270 or x >= 270:
        #print("TOO FAR MOTHER FUCKER!")
    kit.servo[0].angle = (x)
    


