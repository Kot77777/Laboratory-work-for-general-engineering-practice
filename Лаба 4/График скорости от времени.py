import numpy as np
import matplotlib.pyplot as plt

V = np.log(np.array([]))
delta = np.log(np.array([]))

t1 = np.polyfit(delta, V, 1)
f1 = np.poly1d(t1)


plt.plot(V, delta, label = "График log(V) от log(t)")
plt.plot(V, f1(t1), label = "Апроксимирующая прямая графика log(V) от log(t)", color = "red")
plt.minorticks_on()

plt.grid(which='major')
plt.grid(which='minor', linestyle=':')
plt.tight_layout()