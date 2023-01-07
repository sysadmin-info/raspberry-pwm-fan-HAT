# raspberry-pwm-fan-HAT

Program written in Python and C from https://www.waveshare.com/wiki/Fan_HAT I made a corrections in C and Python code, because of variables that by default are wrongly written. Also declared the same value (60) for the below. By default they are set this way:

C:
PCA9685_Init (1000);

Python:
pwm.setPWMFreq (50)
