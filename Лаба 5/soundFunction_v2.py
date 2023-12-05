import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

def speedOfSound(temperature, h2oX, co2Max):
    # Функция определения скорости звука
    R = 8.31314462618
    Mi = [0.028, 0.032, 0.04, 0.044]  # молярные массы N2, O2, Ar, CO2 соотв
    Ci = [0.7899, 0.2095, 0.0093, 0.0003]  # концентрации
    # Значение СN2 было взято со страницы 15
    Cpi = [5, 5, 3, 6]  # Степень свободы
    M = 0
    Pw = h2oX * 2982.4
    C_H2O = Pw / 101300
    Ci[2] = Ci[2] * (1 - C_H2O)
    Ci[0] = Ci[0] * (1 - C_H2O)
    Ci[1] = Ci[1] - co2Max + Ci[3]
    Ci[3] = co2Max
    adiobata_up = 0  # числитель
    adiobata_down = 0  # знаменатель
    for i in range(4):
        M += Mi[i] * Ci[i]
        adiobata_up += Mi[i] * Ci[i] * (Cpi[i] + 2)
        adiobata_down += Mi[i] * Ci[i] * Cpi[i]
        # Деление на 2 и у умножение на R убираем из формулы Cpi(m), т.к оно сократится
    adiobata = adiobata_up / adiobata_down
    #    print(adiobata)
    #    print(M)
    soundSpeed = (adiobata * R * (temperature + 273.15) / M) ** 0.5
    co2X = Ci[3]
    return co2X, soundSpeed
def analytics():  # построение аналитического графика
    # построим график
    fig, ax = plt.subplots()
    ax.grid(which="major", linewidth=1)
    ax.grid(which="minor", linewidth=0.3)
    ax.minorticks_on()
    ax.set_xlim(0, 0.05)

    t = 24  # в цельсиях
    Vp = 0.324
    x = []
    arr = []
    y = []
    for i in range(1001):
        x.append(0.05 / 1000 * i)
    for i in range(1001):
        arr.append(speedOfSound(t, Vp, x[i]))
        y.append(arr[i][1])

    x = np.array(x)
    y = np.array(y)

    def foo(x, a, b, c):
        return a * x ** 2 + b * x + c

    popt, pcov = curve_fit(foo, x, y)
    print(popt)
    plt.plot(x, foo(x, *popt), color='orange', label="Аналитическая функция", linestyle='-')

    plt.xlabel('Концентрация углекислого газа')
    plt.ylabel('Скорость звука, м/с')
    plt.legend()
    ax.set_title("График аналитической функции", wrap=True)
    fig1 = plt.gcf()
    plt.show()
    fig.savefig('analitic.png', dpi=600)

distanse = 1.158
max_speed_hz = 500000
data0 = np.loadtxt('data_0.txt', dtype=int)  # время 2-ой фиксации хлопка
data1 = np.loadtxt('data_1.txt', dtype=int)  # время 1-ой фиксации хлопка

sr_signal_data1 = sum(data1[:28])/28
sr_signal_data0 = sum(data0[:1716])/1716

num = np.arange(0, 4998, 1)
fig1, ax = plt.subplots()
ax.grid(which="major", linewidth=1)
ax.grid(which="minor", linewidth=0.3)
ax.minorticks_on()

plt.plot(num, data1, color='orange', label="первый микрофон", linestyle='-')
plt.plot(num, data0, color='#1E90FF', label="второй микрофон", linestyle='-')

plt.xlabel('Номер отсчета измерения')
plt.ylabel('Показание АЦП')
plt.legend()
fig1.savefig('air_begin.png', dpi=600)

max_value_data1 = max(data1) - sr_signal_data1
max_value_data0 = max(data0) - sr_signal_data0
index_max_value_data1 = np.where(data1 - sr_signal_data1 == max_value_data1)[0][0]
index_max_value_data0 = np.where(data0 - sr_signal_data0 == max_value_data0)[0][0]
print(index_max_value_data0, index_max_value_data1)
print(max_value_data0, max_value_data1)

fig2, ax = plt.subplots()
ax.grid(which="major", linewidth=1)
ax.grid(which="minor", linewidth=0.3)
ax.minorticks_on()

plt.plot(num, data1-sr_signal_data1, color='orange', label="первый микрофон", linestyle='-')
plt.plot(num, data0-sr_signal_data0, color='#1E90FF', label="второй микрофон", linestyle='-')
plt.scatter([index_max_value_data0], [max_value_data0], c = "green")
plt.scatter([index_max_value_data1], [max_value_data1], c = "green")

plt.xlabel('Номер отсчета измерения')
plt.ylabel('Показание АЦП')
plt.legend()
fig2.savefig('air_maximums.png', dpi=600)

fig3, ax = plt.subplots()
ax.grid(which="major", linewidth=1)
ax.grid(which="minor", linewidth=0.3)
ax.minorticks_on()

plt.plot(num, (data1-sr_signal_data1)/max_value_data1, color='orange', label="первый микрофон", linestyle='-')
plt.plot(num, (data0-sr_signal_data0)/max_value_data0, color='#1E90FF', label="второй микрофон", linestyle='-')

plt.xlabel('Номер отсчета измерения')
plt.ylabel('Показание АЦП')
plt.legend()
fig3.savefig('air_sgatie.png', dpi=600)

difference_max = index_max_value_data0 - index_max_value_data1
num_1 = num + difference_max
print(difference_max)
print(num_1)
print(num)

fig4, ax = plt.subplots()
ax.grid(which="major", linewidth=1)
ax.grid(which="minor", linewidth=0.3)
ax.minorticks_on()

plt.plot(num_1[:1117], ((data1-sr_signal_data1)/max_value_data1)[:1117], color='orange', label="первый микрофон", linestyle='-')
plt.plot(num[1683:2800], ((data0-sr_signal_data0)/max_value_data0)[1683:2800], color='#1E90FF', label="второй микрофон", linestyle='-')

plt.xlabel('Номер отсчета измерения')
plt.ylabel('Показание АЦП')
plt.legend()
fig4.savefig('air_smechenie.png', dpi=600)

t = difference_max/max_speed_hz
v = distanse/t
print("Скорость звука в воздухе:", v)
########################################################################################################################
data0_c = np.loadtxt('data_2_2.txt', dtype=int)  # время 2-ой фиксации хлопка
data1_c = np.loadtxt('data_3_2.txt', dtype=int)  # время 1-ой фиксации хлопка

sr_signal_data1_c = sum(data1[:42])/42
sr_signal_data0_c = sum(data0[:1496])/1496

num_c = np.arange(0, 4995, 1)
fig1_c, ax = plt.subplots()
ax.grid(which="major", linewidth=1)
ax.grid(which="minor", linewidth=0.3)
ax.minorticks_on()

plt.plot(num_c, data1_c, color='orange', label="первый микрофон", linestyle='-')
plt.plot(num_c, data0_c, color='#1E90FF', label="второй микрофон", linestyle='-')

plt.xlabel('Номер отсчета измерения')
plt.ylabel('Показание АЦП')
plt.legend()
fig1_c.savefig('c_begin.png', dpi=600)

max_value_data1_c = max(data1_c) - sr_signal_data1_c
max_value_data0_c = max(data0_c) - sr_signal_data0_c
index_max_value_data1_c = np.where(data1_c - sr_signal_data1_c == max_value_data1_c)[0][0]
index_max_value_data0_c = np.where(data0_c - sr_signal_data0_c == max_value_data0_c)[0][0]
print(index_max_value_data0_c, index_max_value_data1_c)
print(max_value_data0_c, max_value_data1_c)

fig2_c, ax = plt.subplots()
ax.grid(which="major", linewidth=1)
ax.grid(which="minor", linewidth=0.3)
ax.minorticks_on()

plt.plot(num_c, data1_c-sr_signal_data1_c, color='orange', label="первый микрофон", linestyle='-')
plt.plot(num_c, data0_c-sr_signal_data0_c, color='#1E90FF', label="второй микрофон", linestyle='-')
plt.scatter([index_max_value_data0_c], [max_value_data0_c], c = "green")
plt.scatter([index_max_value_data1_c], [max_value_data1_c], c = "green")

plt.xlabel('Номер отсчета измерения')
plt.ylabel('Показание АЦП')
plt.legend()
fig2_c.savefig('c_maximums.png', dpi=600)

fig3_c, ax = plt.subplots()
ax.grid(which="major", linewidth=1)
ax.grid(which="minor", linewidth=0.3)
ax.minorticks_on()

plt.plot(num_c, (data1_c-sr_signal_data1_c)/max_value_data1_c, color='orange', label="первый микрофон", linestyle='-')
plt.plot(num_c, (data0_c-sr_signal_data0_c)/max_value_data0_c, color='#1E90FF', label="второй микрофон", linestyle='-')

plt.xlabel('Номер отсчета измерения')
plt.ylabel('Показание АЦП')
plt.legend()
fig3_c.savefig('c_sgatie.png', dpi=600)

difference_max_c = index_max_value_data0_c - index_max_value_data1_c
num_1_c = num_c + difference_max_c
print(difference_max_c)
print(num_1_c)
print(num_c)

fig4_c, ax = plt.subplots()
ax.grid(which="major", linewidth=1)
ax.grid(which="minor", linewidth=0.3)
ax.minorticks_on()

plt.plot(num_1_c[:704], ((data1_c-sr_signal_data1_c)/max_value_data1_c)[:704], color='orange', label="первый микрофон", linestyle='-')
plt.plot(num_c[1696:2400], ((data0_c-sr_signal_data0_c)/max_value_data0_c)[1696:2400], color='#1E90FF', label="второй микрофон", linestyle='-')

plt.xlabel('Номер отсчета измерения')
plt.ylabel('Показание АЦП')
plt.legend()
fig4_c.savefig('c_smechenie.png', dpi=600)

t_c = difference_max_c/max_speed_hz
v_c = distanse/t_c
print("Скорость звука в углекислом газе:", v_c)

analytics()

t = 24  # в цельсиях
Vp = 0.324
x = []
for i in range(5001):
    x.append(0.2 / 5000 * i)
y1 = []
arr1 = []
y2 = []
arr2 = []
for i in range(5001):
    arr1.append(speedOfSound(t, Vp, x[i]))
    y1.append(arr1[i][1])
for i in range(5001):
    arr2.append(speedOfSound(t, 1, x[i]))
    y2.append(arr2[i][1])

x = np.array(x)
y1 = np.array(y1)
y2 = np.array(y2)

# построим график
fig5, ax = plt.subplots()
ax.grid(which="major", linewidth=1)
ax.grid(which="minor", linewidth=0.3)
ax.minorticks_on()
ax.set_xlim(0, 0.1)
ax.set_ylim(338, 352)


# для атмосферы:
def foo(x, a, b):    return a * x + b

popt, pcov = curve_fit(foo, x, y1)
k1 = popt[0]  # коэфцициент наклона
b1 = popt[1]  # f(0)
ugl1 = (v - b1) / k1
print('концентрация угл газа в атмосфере: ', ugl1 * 100, '%')
plt.plot(x, foo(x, *popt), color='orange', label="Влажность, измеренная в учебной аудитории", linestyle='-')


# для воздуха из легких
def foo(x, a, b):
    return a * x + b


popt, pcov = curve_fit(foo, x, y2)
k2 = popt[0]  # коэф наклона
b2 = popt[1]  # f(0)
ugl2 = (v_c - b2) / k2
print('концентрация угл газа в воздухе из легких: ', ugl2 * 100, '%')

plt.plot(x, foo(x, *popt), color='red', label="100% влажность", linestyle='-')
plt.scatter([ugl1, ugl2], [v, v_c], color='Black')  # наносим точки на график

plt.xlabel('Концентрация углекислого газа')
plt.ylabel('Скорость звука, м/с')
plt.legend()
fig5 = plt.gcf()
plt.show()
fig5.savefig('uglic.png', dpi=600)

plt.show()