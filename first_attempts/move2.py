from pyPS4Controller.controller import Controller
import os
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

current_pos = 0

def move_servo():
    global current_pos
    kit.servo[2].angle = (current_pos)

def turn_right():
   global current_pos
   value1 = (current_pos + 10)
   if value1 >=180:
       value1 = 180
   current_pos = value1

def turn_left():
   global current_pos
   value1 = (current_pos - 10)
   if value1 <=0:
       value1 = 0
   current_pos = value1

class MyController(Controller):
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

       # This exits the program #
    def on_playstation_button_press(self):
            usr = str(input("Are you sure you are done?[yes or no]  "))
            if usr == "yes":
                print("You're a Bitch!")
                os.system(quit)
            else:
                pass

            # This block is to controls the base axis #
    def on_right_arrow_press(self):
        turn_right() move_servo()
    def on_left_right_arrow_release(self):
        #move_servo() 
    def on_left_arrow_press(self):
        turn_left() 

        # This block controls the first tilt axis #
    def on_up_arrow_press(self): 
            kit.continuous_servo[1].throttle = 1
    def on_up_arrow_release(self): 
            kit.continuous_servo[1].throttle = 0
    def on_down_arrow_press(self):
            kit.continuous_servo[1].throttle = -1
    def on_down_arrow_release(self): 
            kit.continuous_servo[1].throttle = 0

        # This block controls the second tilt axis #
    def on_L1_press(self):
            kit.continuous_servo[0].throttle = 1
    def on_L1_release(self):
            kit.continuous_servo[0].throttle = 0
    def on_R1_press(self):
            kit.continuous_servo[0].throttle = 1
    def on_R1_release(self):
            kit.continuous_servo[0].throttle = 0

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen(timeout=60)

