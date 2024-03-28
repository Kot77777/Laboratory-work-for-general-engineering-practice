import numpy as np
import matplotlib.pyplot as plt

with open("values_ADC_for_20mm_kalib.txt", "r") as data:
    values_ADC_for_20mm_kalib = np.array([float(i) for i in data.read().split("\n")])

with open("values_ADC_for_40mm_kalib.txt", "r") as data:
    values_ADC_for_40mm_kalib = np.array([float(i) for i in data.read().split("\n")])

with open("values_ADC_for_60mm_kalib.txt", "r") as data:
    values_ADC_for_60mm_kalib = np.array([float(i) for i in data.read().split("\n")])

with open("values_ADC_for_80mm_kalib.txt", "r") as data:
    values_ADC_for_80mm_kalib = np.array([float(i) for i in data.read().split("\n")])

with open("values_ADC_for_100mm_kalib.txt", "r") as data:
    values_ADC_for_100mm_kalib = np.array([float(i) for i in data.read().split("\n")])

with open("values_ADC_for_120mm_kalib.txt", "r") as data:
    values_ADC_for_120mm_kalib = np.array([float(i) for i in data.read().split("\n")])

average_values_for_ADC = np.array([sum(values_ADC_for_20mm_kalib)/len(values_ADC_for_20mm_kalib),
                                   3.3 - sum(values_ADC_for_40mm_kalib)/len(values_ADC_for_40mm_kalib),
                                   3.3 - sum(values_ADC_for_60mm_kalib)/len(values_ADC_for_60mm_kalib),
                                   3.3 - sum(values_ADC_for_80mm_kalib)/len(values_ADC_for_80mm_kalib),
                                   3.3 - sum(values_ADC_for_100mm_kalib)/len(values_ADC_for_100mm_kalib),
                                   3.3 - sum(values_ADC_for_120mm_kalib)/len(values_ADC_for_120mm_kalib)])

deep = np.array([20, 40, 60, 80, 100, 120])


coefs = np.polyfit(average_values_for_ADC, deep, 1)#создаем коэффициенты
func = np.poly1d(coefs)#создает функцию по этим коэффициентам
print("Коэффициенты:", func)


plt.scatter(average_values_for_ADC, deep, c = '#0d00ff')
plt.plot(average_values_for_ADC, func(average_values_for_ADC), label = "h = 124.3U -112.6", color = "red") #Написать в нахвание коэффициенты
plt.minorticks_on()

plt.grid(which='major')
plt.grid(which='minor', linestyle=':')
plt.tight_layout()
plt.xlabel('Напряжение, В', fontsize=10, fontweight='bold')
plt.ylabel('Глубина, мм', fontsize=10, fontweight='bold')

plt.legend()
plt.show()
