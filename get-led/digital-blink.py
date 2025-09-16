import RPi.GPIO as gp
import time as tm

gp.setmode(gp.BCM)

led=26

gp.setup(led, gp.OUT)

state=0

period=1.0

while True:
    gp.output(led, state)
    tm.sleep(period/2)
    state = (state+1)%2