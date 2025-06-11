from pyPS4Controller.controller import Controller
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
    while sv0_current_pos < 270:
        sv0_current_pos = (sv0_current_pos + 1)
        kit.servo[0].angle = (sv0_current_pos)

## Here is the funtion for servo 0 (The Pan axis) ##
def mv_sv0_left():
    global sv0_current_pos
    while sv0_current_pos >0:
        sv0_current_pos = (sv0_current_pos - 1)
        kit.servo[0].angle = (sv0_current_pos)

class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

        # This block controls the second tilt axis #
    def on_L1_press(self):
        #mv_sv2_down()
    	mv_sv0_left()

    def on_L1_release (self):
        kit.servo[0].angle = (sv0_current_pos)

    def on_R1_release (self):
        kit.serko[0].angle = (sv0_current_pos)

    def on_R1_press(self):
        #mv_sv2_up()
    	mv_sv0_right()

controller = MyController(interface="/dev/input/js0")
controller.listen(timeout=160)
