import RPi.GPIO as gp
import time as tm

gp.setmode(gp.BCM)

led=26
button=13
photsens=6

gp.setup(photsens, gp.IN)
gp.setup(led, gp.OUT)

state=0

period=0.2

while True:
    gp.output(led, not gp.input(photsens))