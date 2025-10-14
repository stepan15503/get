import time
from math import sin,pi

def get_sin_wave_amplitude(freq,time):
    a=(sin(2*pi*freq*time)+1)/2
    return a
def get_line_wave_amplitude(freq,time):
    time=time%(1/freq)
    if time<=0.5*1/freq:
        return 1-time*freq*2
    return (1-time*freq*2)*-1
def wait_for_sampling_period(sampling_frequency):
    time.sleep(1/sampling_frequency)