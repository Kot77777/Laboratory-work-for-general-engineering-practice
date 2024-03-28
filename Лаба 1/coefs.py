import numpy as np
import matplotlib.pyplot as plt

with open("40.txt", "r") as data:
    values_ADC_for_20mm_kalib = np.array([float(i) for i in data.read().split("\n")])

with open("80.txt", "r") as data:
    values_ADC_for_40mm_kalib = np.array([float(i) for i in data.read().split("\n")])

with open("100.txt", "r") as data:
    values_ADC_for_60mm_kalib = np.array([float(i) for i in data.read().split("\n")])

with open("120.txt", "r") as data:
    values_ADC_for_80mm_kalib = np.array([float(i) for i in data.read().split("\n")])

with open("140.txt", "r") as data:
    values_ADC_for_100mm_kalib = np.array([float(i) for i in data.read().split("\n")])

average_values_for_ADC = np.array([sum(values_ADC_for_20mm_kalib)/len(values_ADC_for_20mm_kalib),
                                   sum(values_ADC_for_40mm_kalib)/len(values_ADC_for_40mm_kalib),
                                   sum(values_ADC_for_60mm_kalib)/len(values_ADC_for_60mm_kalib),
                                   sum(values_ADC_for_80mm_kalib)/len(values_ADC_for_80mm_kalib),
                                   sum(values_ADC_for_100mm_kalib)/len(values_ADC_for_100mm_kalib)])

deep = np.array([40, 80, 100, 120, 140])


coefs = np.polyfit(deep, average_values_for_ADC, 1)#создаем коэффициенты
func = np.poly1d(coefs)#создает функцию по этим коэффициентам
print("Коэффициенты:", func)


plt.scatter(deep, average_values_for_ADC, c = '#0d00ff', label='Калибровочные значения')
plt.plot(deep, func(deep), label = "y = 9.694x + 113.7 -- аппроксимирующая прямая", color = "red") #Написать в нахвание коэффициенты
plt.minorticks_on()

plt.grid(which='major')
plt.grid(which='minor', linestyle=':')
plt.tight_layout()
plt.xlabel('Давления, Па', fontsize=10, fontweight='bold')
plt.ylabel('Отсчёты АЦП', fontsize=10, fontweight='bold')
title_text = 'Калибровочный график давления от отсчётов АЦП'
plt.title(title_text, wrap=True)
plt.legend()
plt.show()
