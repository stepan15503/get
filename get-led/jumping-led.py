import RPi.GPIO as gp
import time as tm

gp.setmode(gp.BCM)

leds=[24,22,23,27,17,25,12,16]
button=13
photsens=6

gp.setup(photsens, gp.IN)
gp.setup(leds, gp.OUT)

gp.output(leds,0)

state=0

period=0.2
levels=20

while True:
    for i in leds:
        gp.output(i, 1)
        tm.sleep(period)
        gp.output(i,0)
    for i in leds[::-1]:
        gp.output(i, 1)
        tm.sleep(period)
        gp.output(i,0)