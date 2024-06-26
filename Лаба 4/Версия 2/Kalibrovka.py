import numpy as np
import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

def binary(n):  # перевод в двоичную сс
    return [int(i) for i in bin(n)[2:].zfill(8)]


def adc():  # ацп
    value = 0
    for i in range(7, -1, -1):
        value += 2 ** i
        GPIO.output(dac, binary(value))
        time.sleep(0.0005)
        if GPIO.input(comp) == 1:
            value -= 2 ** i
    return value

GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

listADC = []
time_start = time.time()
while (time.time() - time_start) <= 10:  #пока не пройдет хотя бы 10 секунд
    listADC.append(3.3 - adc() / 256 * 3.3)
list_str = [str(item) for item in listADC]
with open('values_ADC_for_20mm_kalib.txt', 'w') as f:
    f.write("\n".join(list_str))
