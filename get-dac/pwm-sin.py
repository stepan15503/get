import pwm_dac as pwm
import signal_generator as sg
import time
amplitude = 3.18
signal_frequency = 0.1
sampling_frequency = 1000




if __name__ == "__main__":
    try:
        dac = pwm.PWM_DAC(12, 500, 3.290, True)
        
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