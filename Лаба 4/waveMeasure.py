import numpy as np
import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

#def k_finder(v,v0 , h):  # эта функция определяет коэф k, определяющий зависимость напряжения от глубины v = v0 + k*h
#    #ожидаемо, к < 0
#    return (v - v0)  / h

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
GPIO.setup(21, GPIO.IN)
listADC = []  # напряжение
list_time = []  # моменты времени снятия напряжения

h = int(input(" Введите уровень жидкости")) # начальная высота жидкости. снимаем вручную
v0 = int(input(" Введите начальное напряжение")) #начальное напряжение, ожидаемо 3.3 или 5 В. снимаем вручную
L = int(input(" Введите длину от слива до проводника" ))# длина от проводника до слива из кюветы. снимаем вручную

while 1:  # отслеживает открытие крышки слива
    print(GPIO.input(21), "- состояние закрывашки")
    if GPIO.input(21) == 1:
        timeStart = time.time()
        break

listADC.append(adc() / 256 * 3.3)
#k = k_finder((listADC[0], v0, h)) #определили k. НУЖНО КАЛИБРОВАТЬ
list_time.append(time.time() - timeStart)

while 1:  # отслеживает момент, когда волна проходит через проводник, те момент понижения напряжения
    listADC.append(adc() / 256 * 3.3)
    list_time.append(time.time() - timeStart)
    print(adc() / 256 * 3.3, "- напряжение на проводнике")
    if listADC[-1] - listADC[-2] >= 0.5:
        delta = time.time() - timeStart
        break

print("")
print(delta, "- время до изменения напряжения с момента открытия")
print("")

while 1:  # снимает напряжение с ацп и время
    time.sleep(0.005)
    listADC.append(adc() / 256 * 3.3)
    list_time.append(time.time() - timeStart)

    print(adc() / 256 * 3.3, "<- напряжение на проводнике ----", list_time[-1], "<- время в момент данного измерения")

    if abs(listADC[-1] - listADC[-2]) <= 0.01:  # если изменение напряжения мало, то перестаем снимать показания с ацп
        print("конец измерения")
        break

Time = np.array(list_time) #создаем массивы numpy с напряжением, времнем и глубиной для построения графиков
Voltage = np.array(listADC) #создаем массивы numpy с напряжением, времнем и глубиной для построения графиков
Deep = (Voltage - v0)/k#создаем массивы numpy с напряжением, времнем и глубиной для построения графиков

print("Cкорость распространения волны:", L / delta)

#Далее надо доделать
plt.plot(Time, Deep, label = "V(t)", color = "red")
plt.minorticks_on()
plt.xlabel(r'$x$', fontsize=16)
