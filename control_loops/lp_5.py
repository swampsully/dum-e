from pyPS4Controller.controller import Controller
import os
from adafruit_servokit import ServoKit
import time

# Here are the physical limits of the servos for this this project #

kit = ServoKit(channels=16)
kit.servo[0].actuation_range = 270 # This is the pan axis #
kit.servo[1].actuation_range = 180 # This is the first tilt axis #
kit.servo[2].actuation_range = 180 # This is the second tilt axis #
kit.servo[3].actuation_range = 180 # This is pan sxis for the wrist #

 # These are the starting positions for the servos#
 	## These variables store the position value of each axis ##

sv0_current_pos = 180

sv1_current_pos = 0

sv2_current_pos = 0

sv3_current_pos = 0

# These are the start up positions #
def startup():
    kit.servo[0].angle = 0 
    kit.servo[1].angle = 40 
    kit.servo[2].angle = 40 
    kit.servo[3].angle = 40 

# moving to start posission #

startup()


# Here I am defining the diffent funtions that control each axis #

## Here is the funtion for servo 0 (The Pan axis) ##
def mv_sv0_right():
    global sv0_current_pos
    while sv0_current_pos < 270:
        (sv0_current_pos + 1)
        kit.servo[0].angle = (sv0_current_pos)

## Here is the funtion for servo 0 (The Pan axis) ##
def mv_sv0_left():
    global sv0_current_pos
    while sv0_current_pos >0:
        (sv0_current_pos - 1)
        kit.servo[0].angle = (sv0_current_pos)

def mv_sv1_up():
    global sv1_current_pos
    while True:
        value1 = (sv1_current_pos + 5)
        if value1 >= 180:
            value1 = 180
            break
        sv1_current_pos = value1
        kit.servo[1].angle = (sv1_current_pos)

def mv_sv1_down():
    global sv1_current_pos
    while True:
        value1 = (sv1_current_pos - 5)
        if value1 < 0:
            value1 = 0
            break
        sv1_current_pos = value1
        kit.servo[1].angle = (sv1_current_pos)

def mv_sv2_down():
    global sv2_current_pos
    while True:
        value1 = (sv2_current_pos + 5)
        if value1 >= 180:
           value1 = 180
           break
        sv2_current_pos = value1
        kit.servo[2].angle = (sv2_current_pos)

def mv_sv2_up():
    global sv2_current_pos
    while True:
        value1 = (sv2_current_pos - 5)
        if value1 <= 0:
           value1 = 0
           break
        sv2_current_pos = value1
        kit.servo[2].angle = (sv2_current_pos)


class MyController(Controller):
           # This exits the program #
    def on_playstation_button_press(self):
     os.system(quit)

            # This block is to controls the base axis #
    def on_right_arrow_press(self):
        #mv_sv0_right()
    	pass

    def on_left_arrow_press(self):
        #mv_sv0_left()
    	pass

    def on_left_right_arrow_release (self):
    	kit.servo[0].angle = (sv0_current_pos)

        # This block controls the first tilt axis #
    def on_up_arrow_press(self):
        mv_sv1_up()

    def on_down_arrow_press(self):
        mv_sv1_down()


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

