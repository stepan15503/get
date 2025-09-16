import RPi.GPIO as gp
import time as tm

gp.setmode(gp.BCM)

led=26
button=13
photsens=6

gp.setup(photsens, gp.IN)
gp.setup(led, gp.OUT)
pwm=gp.PWM(led,200)

duty=0.0
pwm.start(duty)


state=0

period=0.001
levels=20

while True:
    pwm.ChangeDutyCycle(duty)
    tm.sleep(period/levels)

    duty+=100/levels
    if duty> 100.0:
        duty=0.0