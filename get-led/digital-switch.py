import RPi.GPIO as gp
import time as tm

gp.setmode(gp.BCM)

led=26
button=13

gp.setup(button, gp.IN)
gp.setup(led, gp.OUT)

state=0

period=0.2

while True:
    if gp.input(button):
        gp.output(led, state)
        tm.sleep(period)
        state = (state+1)%2