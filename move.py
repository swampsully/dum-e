from adafruit_servokit import ServoKit
from pyPS4Controller.controller import Controller
import time
kit = ServoKit(channels=16)

# this is a poorly writen program to see if I can move servos wth a ps4 controller at 1:30AM #

    # This is the pan the bottom pan axis with the most degree of motion #

class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_L3_left(self):
        kit.servo[0].angle = 10
        break
    
    def on_L3_x_at_rest (self):
        time.sleep(1)

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# you can start listening before controller is paired, as long as you pair it within the timeout window
controller.listen(timeout=60)
