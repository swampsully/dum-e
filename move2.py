from pyPS4Controller.controller import Controller
import os
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

current_pos = 0
new_pos = 0
value2 = 0

def move_servo():
    global current_pos
    global value2
    global new_pos
    if new_pos >= 180:
        new_pos = 180
        print("TOO FAR BITCH BOI")
    if new_pos<= 0:
        new_pos = 0
    new_pos = value2 - current_pos 
    kit.servo[2].angle = (new_pos)

def turn_right():
   value2 = current_pos + 10
   if value2 >=180:
       value2 = 180
   print(value2)

def turn_left():
   value1 = current_pos
   value2 = value1 - 10
   if value1 <=0:
       value2 = 0
   print(value2)


class MyController(Controller):
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

       # This exits the program #
    def on_playstation_button_press(self):
            os.system("quit")

            # This block is to controls the base axis #
    def on_right_arrow_press(self):
           turn_right() 
    def on_left_right_arrow_release(self):
           move_servo() 
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
controller.debug = True

controller.listen(timeout=60)

