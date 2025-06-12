import os
from adafruit_servokit import ServoKit
import time

# Here are the physical limits of the servos for this this project #

kit = ServoKit(channels=16)
kit.servo[0].actuation_range = 270 # This is the pan axis #

sv0_current_pos = 180

def startup():
    kit.servo[0].angle = 180 

# moving to start posission #

startup()


## Here is the funtion for servo 0 (The Pan axis) ##
def mv_sv0_right():
    global sv0_current_pos
    while sv0_current_pos < 275:
        sv0_current_pos += 1
        kit.servo[0].angle = (sv0_current_pos)
        if sv0_current_pos == 270:
            break

## Here is the funtion for servo 0 (The Pan axis) ##
def mv_sv0_left():
    global sv0_current_pos
    while sv0_current_pos >0:
        kit.servo[0].angle = (sv0_current_pos)
        sv0_current_pos += (- 1)
        if sv0_current_pos == 1:
            break


## Here is a loop for controling the robot with a keyboard. ##

def keys():
    while True:
        usr = input(" ")
        if usr == h:
            def mv_sv0_right()

        elif usr == l:
            def mv_sv0_left()

        elif usr == q:
            break

        else:
            pass

