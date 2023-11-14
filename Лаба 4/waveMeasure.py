import waveFunctions as b
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(21, GPIO.IN)
listADC = []

def binary(n):
    return [int(i) for i in bin(n)[2:].zfill(8)]
def adc():
    value = 0
    for i in range(7, -1, -1):
        value += 2**i
        GPIO.output(dac, binary(value))
        time.sleep(0.0005)
        if GPIO.input(comp) == 1:
            value -= 2**i
    return value

while 1:
    print(GPIO.input(21))
    if GPIO.input(21) == 1:
        timeStart = time.time()
        break

listADC.append(adc()/256*3.3)

while 1:
    listADC.append(adc()/256*3.3)
    print(adc()/256*3.3)
    if listADC[-1]  - listADC[-2] >= 0.5:
        delta = time.time() - timeStart
        break
print(delta)

