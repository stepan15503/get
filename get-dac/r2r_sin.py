import r2r_dac as r2r
import signal_generator as sg
import time
amplitude = 3.18
signal_frequency = 0.1
sampling_frequency = 1000

if __name__ == "__main__":
    try:
        dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)
        t=0

        while True:
            try:
                t+=1/sampling_frequency
                voltage = amplitude*sg.get_sin_wave_amplitude(signal_frequency,t)
                dac.set_voltage(voltage)
                sg.wait_for_sampling_period(sampling_frequency)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()