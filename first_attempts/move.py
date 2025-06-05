from pyPS4Controller.controller import Controller
import os
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)


class MyController(Controller):
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

        # This exits the program #
    def on_playstation_button_press(self):
            os.system("Ctrl-C")

            # This block is to controls the base axis #
    def on_right_arrow_press(self):
            kit.continuous_servo[2].throttle = 1
    def on_left_right_arrow_release(self):
            kit.continuous_servo[2].throttle = 0
    def on_left_arrow_press(self):
            kit.continuous_servo[2].throttle = -1

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

