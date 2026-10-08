#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
motor1 = Motor(port = Port.B, positive_direction = Direction.COUNTERCLOCKWISE)
touch_sensor = TouchSensor(port = Port.S1)
us_sensor = UltrasonicSensor(port = Port.S4)
gyro_sensor = GyroSensor(port = Port.S2)


# Write your program here.
ev3.speaker.beep()
motor1.run_target(speed = 180, target_angle = 360, then = Stop.HOLD, wait = True)
while(True):
    ev3.screen.clear()
    ev3.screen.print("Pressed:", touch_sensor.pressed())
    ev3.screen.print("Distance:", us_sensor.distance(), "mm")
    ev3.screen.print("Gyro:", gyro_sensor.angle(), "deg")
    ev3.screen.print("Gyro Speed:", gyro_sensor.speed(), "deg/s")
    wait(100)