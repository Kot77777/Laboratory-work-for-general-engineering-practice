import numpy as np
import matplotlib.pyplot as plt
with open("после веселья.txt", "r") as data:
    values_presure = np.array([int(i) for i in data.read().split("\n")])

presure = (values_presure - 113.7)/9.694
chastota = (60/12557)
time = chastota * np.array(np.arange(1, 12558))

# coefs = np.polyfit(time, presure, 25)#создаем коэффициенты
# func = np.poly1d(coefs)#создает функцию по этим коэффициентам
# print("Коэффициенты:", func)

x_ADC = [516.41, 1098.05]
y = [84.4, 141]
x = [58.67, 17.422]
plt.text(x[1] + 0.4, y[1], 'Систола', fontsize=15)
plt.text(x[0] + 0.4, y[0], 'Диастола', fontsize=15)
plt.scatter(x, y, c="orange", zorder = 1)
plt.plot(time, presure, label = "Давление - 141/85 [мм.рт.ст.]", zorder = -1)
#plt.plot(time, func(time), label = "y = 9.694x + 113.7 -- аппроксимирующая прямая", color = "red") #Написать в нахвание коэффициенты
plt.minorticks_on()

plt.grid(which='major')
plt.grid(which='minor', linestyle=':')
plt.tight_layout()
plt.xlabel('Время, с', fontsize=10, fontweight='bold')
plt.ylabel('Давление, мм.рт.ст', fontsize=10, fontweight='bold')
title_text = 'Артериальное давление после физической нагрузки'
plt.title(title_text, wrap=True)
plt.legend()
plt.show()

