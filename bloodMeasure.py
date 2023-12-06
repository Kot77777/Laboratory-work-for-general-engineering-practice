import bloodFunctions as b
import RPi.GPIO as Rpi
import matplotlib.pyplot as plt
import time
b.initSpiAdc()
data_file = 'после веселья.txt'

a = input()
try:
    st_time = time.time()
    data = []
    data_x = []
    while time.time() - st_time <= 60:
        data.append(b.getAdc())
        data_x.append(time.time() - st_time)
        data_str = [str(i) for i in data]
        print(time.time() - st_time, b.getAdc())
    with open(data_file,"w") as file:
        file.write("\n".join(data_str))
    plt.plot(data_x, data)
    plt.show()
finally:
    b.deinitSpiAdc()
    Rpi.cleanup()