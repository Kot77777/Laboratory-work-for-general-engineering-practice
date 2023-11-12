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

print(2)
GPIO.setup(21, GPIO.IN)
listADC = []

while 1:
    time.sleep(0.1)
    print(GPIO.input(21))
one = adc()/256*3.3
listADC.append(one)
vrem = int(input())
timeStart = time.time()
print(2)
while 1:
    one = adc()/256*3.3
    listADC.append(one)
    print(adc()/256*3.3)
    if listADC[-1] != listADC[-2]:
        delta = time.time() - timeStart
        break
print(delta)
