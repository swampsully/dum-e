import time
from adafruit_servokit import ServoKit
import adafruit_motor.servo

#servo = adafruit_motor.servo.Servo(servo_channel)
kit = ServoKit(channels=16)

kit.servo[0].angle = 0
kit.servo[1].angle = 0
kit.servo[2].angle = 90
time.sleep(1)

kit.servo[0].angle = 180
kit.servo[1].angle = 90
kit.servo[2].angle = 0
time.sleep(1)

kit.servo[0].angle = 0
kit.servo[1].angle =180
kit.servo[2].angle =180
time.sleep(1)

kit.servo[0].angle = 0
kit.servo[1].angle = 0
kit.servo[2].angle = 90
time.sleep(1)

kit.servo[0].angle = 180
kit.servo[1].angle = 90
kit.servo[2].angle = 0
time.sleep(1)

kit.servo[1].angle = 180
kit.servo[2].angle = 90
kit.servo[0].angle = 0
time.sleep(1)

kit.servo[0].angle = 180
kit.servo[1].angle = 90
kit.servo[2].angle = 0
time.sleep(1)

