# HiWonder Tank Chassis Python Code (un-official)


![image](https://github.com/robswc/hi-wonder-tank-chassis/assets/38849824/505294d0-94c6-44b9-843f-532ce4a5e897)

Hey all!  I recently ordered a tank chassis from HiWonder.
The a lot of the python documentation was in Chinese and required rospy.
I believe there were also files missing in the offical documentation.

I created this very simple script, based off the more complete and working Arduino tutorial.

I'm using the following motor driver:

https://www.hiwonder.com/products/4-channel-encoder-motor-driver

With this chassis:

https://www.hiwonder.com/products/suspended-shock-absorbing-tracked-chassis?variant=40378709835863

The python scripts contained in this repo are _very_ simple but I find them to fit my use case perfectly.

The main concepts are as follows:

```python
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
```

I derived the constants/addresses from HiWonder's arduino tutorial.  The scripts use [smbus2](https://pypi.org/project/smbus2/) to handle the writing operations.  That would be the only 3rd party library needed.
