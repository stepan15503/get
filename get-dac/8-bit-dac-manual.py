import RPi.GPIO as gp


gp.setmode(gp.BCM)

pins=[16,20,21,25,26,17,27,22]
gp.setup(pins, gp.OUT)

dynamic_range=3.19

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} В)")
        print("Устанавлниваем 0.0 В")
        return 0

    return int(voltage / dynamic_range * 255)

def DecToBin(value):
    return [int(i) for i in bin(value)[2:].zfill(8)]

def number_to_dac(num):
    for i in range(8):
        gp.output(pins[i], DecToBin(num)[i])

try:
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах: "))
            number = voltage_to_number(voltage)
            number_to_dac(number)

        except ValueError:
            print("Вы ввели не число. Попробуйте ещё раз\n")

finally:
    gp.output(pins, 0)
    gp.cleanup()