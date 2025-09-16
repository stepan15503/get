import RPi.GPIO as gp
import time as tm

gp.setmode(gp.BCM)

leds=[24,22,23,27,17,25,12,16][::-1]
num=0

def DecToBin(value):
    return [int(i) for i in bin(value)[2:].zfill(8)]
button=13
up=9
down=10

gp.setup(up, gp.IN)
gp.setup(down, gp.IN)
gp.setup(leds, gp.OUT)

gp.output(leds,0)

state=0

period=0.2
levels=20

while True:
    tm.sleep(period)
    if gp.input(up) and gp.input(down):
        num=255
        tm.sleep(period)
    elif gp.input(up):
        num+=1
        if num >255:
            num=0
        print(num, DecToBin(num))
        tm.sleep(period)

    elif gp.input(down):
        num-=1
        if num<0:
            num=255
        print(num, DecToBin(num))
        tm.sleep(period)
    for i in range(len(leds)):
        gp.output(leds[i], DecToBin(num)[i])