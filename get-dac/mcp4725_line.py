import mcp4725_driver as mcp
import signal_generator as sg

amplitude = 5.11
signal_frequency = 0.1
sampling_frequency = 1000
t=0


if __name__ == "__main__":
    try:
        dac = mcp.MCP4725(amplitude, 0x61 ,True)
        
        while True:
            try:
                t+=1/sampling_frequency
                voltage = amplitude*sg.get_line_wave_amplitude
                (signal_frequency,t)
                dac.set_voltage(voltage)
                sg.wait_for_sampling_period(sampling_frequency)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()