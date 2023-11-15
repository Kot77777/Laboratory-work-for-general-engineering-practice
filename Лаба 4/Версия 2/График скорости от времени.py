import numpy as np
import matplotlib.pyplot as plt

deep = np.log(np.array([60, 80, 100 ]))
speed = np.log(np.array([0.77, 0.93, 1.12]))

sr_znach_kv_deep = sum(deep**2)/5
sr_znach_deep_kv = (sum(deep)/5)**2
sr_znach_kv_speed = sum(speed**2)/5
sr_znach_speed_kv = (sum(speed)/5)**2

coefs = np.polyfit(deep, speed, 1)#создаем коэффициенты
func = np.poly1d(coefs)#создает функцию по этим коэффициентам
print("Коэффициенты:", func)
sigma_b = (1/(5**0.5))*(((sr_znach_kv_speed - sr_znach_speed_kv)/(1) - func[1]**2)**0.5)
sigma_a = sigma_b*((sr_znach_kv_speed - sr_znach_speed_kv)**0.5)
print("Погрешности", sigma_a, sigma_b)

plt.scatter(deep, speed)
plt.plot(deep, func(deep), label = "Апроксимирующая прямая графика log(V) от log(t) \n "
                                   "ln(c) = 0.73*ln(h) - 3.256 \n "
                                   "a = 0.73 \u00B1 \n"
                                   "b = -3.256 \u00B1 ", color = "red")#вбить значения погрешностей
plt.minorticks_on()

plt.grid(which='major')
plt.grid(which='minor', linestyle=':')
plt.tight_layout()
plt.xlabel('ln(h), мм', fontsize=10, fontweight='bold')
plt.ylabel('ln(c), м/c', fontsize=10, fontweight='bold')

plt.legend()
plt.show()
