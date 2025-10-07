import RPi.GPIO as gp

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.pwm_frequency=pwm_frequency
        
        gp.setmode(gp.BCM)
        gp.setup(self.gpio_pin, gp.OUT, initial = 0)

        self.pwm=gp.PWM(gpio_pin,pwm_frequency)

        self.pwm.start(0)

    def deinit(self):
        gp.output(self.gpio_pin,0)
        gp.cleanup()

    def set_number(self, number):
        self.pwm.ChangeDutyCycle(number)

    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range:.2f} В)")
            print("Устанавлниваем 0.0 В")
            self.set_number(0)
        self.set_number(int(voltage / self.dynamic_range * 100))

if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, 3.290, True)
        
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()