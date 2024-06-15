# This is a simple Python script that uses the smbus2 library to control the motor controller
# It was adapted from the documentation created by Hi-Wonder, the manufacturer of the motor controller and chassis
import time
from smbus2 import SMBus  # requires smbus2, a Python 3.x library
import curses

# Constants
I2C_ADDR = 0x34  # I2C address of the motor controller
MOTOR_TYPE_ADDR = 20  # Motor type address
MOTOR_ENCODER_POLARITY_ADDR = 21  # Motor encoder polarity address
MOTOR_FIXED_SPEED_ADDR = 51  # Motor fixed speed address

class MotorInstructions:
    FORWARD = [23, 23, 0, 0]
    RETREAT = [-23, -23, 0, 0]
    TURN_LEFT = [20, -20, 0, 0]
    TURN_RIGHT = [-20, 20, 0, 0]
    STOP = [0, 0, 0, 0]

# Initialize I2C bus
bus = SMBus(1)  # usually 1 for Raspberry Pi/Jetson Nano

def write_motor_data(data):
    """Writes motor data to the motor controller."""
    for i, value in enumerate(data):
        bus.write_byte_data(I2C_ADDR, MOTOR_FIXED_SPEED_ADDR + i, value & 0xFF)

def move_forward():
    write_motor_data(MotorInstructions.FORWARD)

def move_retreat():
    write_motor_data(MotorInstructions.RETREAT)

def turn_left():
    write_motor_data(MotorInstructions.TURN_LEFT)

def turn_right():
    write_motor_data(MotorInstructions.TURN_RIGHT)

def stop():
    write_motor_data(MotorInstructions.STOP)

def control_car(window):
    """Curses-based function to control the car with the arrow keys."""
    window.nodelay(True)
    key=""
    window.clear()
    window.addstr("Control the car with the arrow keys. Press 'q' to quit.\n")
    while True:  # Main loop
        try:
            key = window.getch()
            if key == ord('q'):
                break
            elif key == curses.KEY_UP:
                move_forward()
            elif key == curses.KEY_DOWN:
                move_retreat()
            elif key == curses.KEY_LEFT:
                turn_left()
            elif key == curses.KEY_RIGHT:
                turn_right()
            else:
                stop()
            time.sleep(0.025)
        except Exception as e:
            window.addstr(str(e))
            break

# Setup curses for keyboard input
curses.wrapper(control_car)