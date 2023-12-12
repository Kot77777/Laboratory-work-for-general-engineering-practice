import numpy as np
import matplotlib.pyplot as plt
with open("после веселья.txt", "r") as data:
    values_presure = np.array([int(i) for i in data.read().split("\n")])

presure = (values_presure - 113.7)/9.694
chastota = (60/12557)
time = chastota * np.array(np.arange(1, 12558))

coefs = np.polyfit(time, presure, 25)#создаем коэффициенты
func = np.poly1d(coefs)#создает функцию по этим коэффициентам

plt.plot(time, presure - func(time), label = "Пульс - 78[уд/мин]", color = "red") #Написать в нахвание коэффициенты
plt.minorticks_on()
plt.xlim([35, 45])
plt.grid(which='major')
plt.grid(which='minor', linestyle=':')
plt.tight_layout()
plt.xlabel('Время, с', fontsize=10, fontweight='bold')
plt.ylabel('Изменение давления в артерии, мм.рт.ст', fontsize=10, fontweight='bold')
title_text = 'Пульс после физической нагрузки'
plt.title(title_text, wrap=True)
plt.legend()
plt.show()

