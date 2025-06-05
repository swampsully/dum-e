from pyPS4Controller.controller import Controller
import os
from adafruit_servokit import ServoKit
import time


kit = ServoKit(channels=16)
kit.servo[0].actuation_range = 270
kit.servo[1].actuation_range = 180
kit.servo[2].actuation_range = 180
kit.servo[3].actuation_range = 180

 # These are the starting positions for the servos#
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

startup()

def mv_sv0_right():
    global sv0_current_pos
    
    while True:
        value1 = (sv0_current_pos + 45)
        if value1 >= 270:
            value1 = 270
        sv0_current_pos = value1
        kit.servo[0].angle = (sv0_current_pos)

def mv_sv0_left():
    global sv0_current_pos
    
    while True:
        value1 = (sv0_current_pos - 45)
        if value1 <=0:
            value1 = 0
        sv0_current_pos = value1
        kit.servo[0].angle = (sv0_current_pos)

def mv_sv1_up():
    global sv1_current_pos
    
    while True:
        value1 = (sv1_current_pos + 40)
        if value1 >=180:
            value1 = 180
        sv1_current_pos = value1
        kit.servo[1].angle = (sv1_current_pos)

def mv_sv1_down():
    global sv1_current_pos
    
    while True:
       value1 = (sv1_current_pos - 40)
        if value1 <=0:
            value1 = 0
        sv1_current_pos = value1
        kit.servo[1].angle = (sv1_current_pos)

def mv_sv2_down():
    global sv2_current_pos
    
    while True:
        value1 = (sv2_current_pos + 40)
        if value1 >=180:
            value1 = 180
        sv2_current_pos = value1
        kit.servo[2].angle = (sv2_current_pos)

# This is the contoller portion of the code #
class MyController(Controller):
           # This exits the program #
    def on_playstation_button_press(self):
        startup()
        print("You're a Bitch!")
        os.system(quit)


def mv_sv2_up():
    global sv2_current_pos
    
    while True:
        value1 = (sv2_current_pos - 40)
        if value1 <=0:
            value1 = 0
        sv2_current_pos = value1
        kit.servo[2].angle = (sv2_current_pos)

            # This block is to controls the base axis #
    def on_right_arrow_press(self):
        mv_sv0_right()
    def on_left_arrow_press(self):
        mv_sv0_left()

        # This block controls the first tilt axis #
    def on_up_arrow_press(self):
        mv_sv1_up()
    def on_down_arrow_press(self):
        mv_sv1_down()

    def on_L3_up():
        mv_sv1_up()

    def on_L3_down():
        mv_sv1_down()

        # This block controls the second tilt axis #
    def on_L1_press(self):
        mv_sv2_down()
    def on_R1_press(self):
        mv_sv2_up()
controller = MyController(interface="/dev/input/js0")
controller.listen(timeout=160)

