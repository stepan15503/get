import numpy as np
import time
from math import sin,pi

def get_sin_wave_amplitude(freq,time):
    a=(sin(2*pi*freq*time)+1)/2
    return a
def wait_for_sampling_period(sampling_frequency):
    time.sleep(1/sampling_frequency)