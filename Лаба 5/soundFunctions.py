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
    x = [1, 10]
    y = [1, 2]

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

    plt.plot(x, foo(x, *popt), color='orange', label="Аналитическая функция", linestyle='-')

    plt.xlabel('Концентрация углекислого газа')
    plt.ylabel('Скорость звука, м/с')
    plt.legend()
    ax.set_title("График аналитической функции", wrap=True)
    fig1 = plt.gcf()
    plt.show()
    fig.savefig('analitic.png', dpi=600)

    # найдем коэфициенты наклона
    print('Функция имеет вид: f(x) = a*x^2 + b*x + c, где:')
    print('a =', popt[0])
    print('b =', popt[1])
    print('c =', popt[2])


# экспериментальное нахождение скорости
def for_find_t(len, check, massive, num): # check: если 0 - совпадает с первого пика, 1 - со второго пика
    # опустим прямые
    sum = 0
    if (num == 1):
        for i in range(1000):
            sum += massive[i]
        srednee = sum / 1000
    else:
        for i in range(2000, 3000):
            sum += massive[i]
        srednee = sum / 1000
    for i in range(len):
        massive[i] = massive[i] - srednee

    # найдем пики:
    max = 0
    i_max = 0
    max1 = 0
    if (check == 0):
        for i in range(0, len):
            if (massive[i] > max):
                i_max = i
                max = massive[i]

    else:
        for i in range(len):
            if (massive[i] > max1):
                i_max1 = i
                max1 = massive[i]
        for i in range(len):
            if (massive[i] > max and (i < i_max1 - 20 or i > i_max1 + 20)):
                i_max = i
                max = massive[i]

    # разделим все значения зависимостей на значения пиков
    massive_new = []
    for i in range(len):
        massive_new.append(massive[i] / max)

    return i_max, massive_new


# функция для построения графиков
def grafics(x, y1_low_start, y2_low_start, count):
    fig, ax = plt.subplots()
    ax.grid(which="major", linewidth=1)
    ax.grid(which="minor", linewidth=0.3)
    ax.minorticks_on()
    #    ax.set_xlim(0, 11)
    #    ax.set_ylim(0, 2.7)

    y1 = []
    y2 = []
    x1 = []
    for i in range(len(x)-2):
        y1.append(y1_low_start[i])
        y2.append(y2_low_start[i])
        x1.append(x[i])

    plt.plot(x1, y2, color='orange', label="первый микрофон", linestyle='-')
    plt.plot(x1, y1, color='#1E90FF', label="второй микрофон", linestyle='-')

    plt.xlabel('Номер отсчета измерения')
    plt.ylabel('Показание АЦП')
    plt.legend()
    fig1 = plt.gcf()
    plt.show()
    if (count == 0):
        fig1.savefig('graf1.png', dpi=600)
    if (count == 1):
        fig1.savefig('graf2.png', dpi=600)
    if (count == 2):
        fig1.savefig('graf3.png', dpi=600)
    if (count == 3):
        fig1.savefig('graf1_sluch2.png', dpi=600)
    if (count == 4):
        fig1.savefig('graf2_sluch2.png', dpi=600)
    if (count == 5):
        fig1.savefig('graf3_sluch2.png', dpi=600)
    if (count == 6):
        fig1.savefig('graf1_new.png', dpi=600)
    if (count == 7):
        fig1.savefig('graf2_new.png', dpi=600)
    if (count == 8):
        fig1.savefig('graf3_new.png', dpi=600)
    count += 1
    return count


# считаем данные
data0 = np.loadtxt('data_0.txt', dtype=int)  # время 2-ой фиксации хлопка
data1 = np.loadtxt('data_1.txt', dtype=int)  # время 1-ой фиксации хлопка
# добавим немного своих переменных
x = []
a = 0
for i in range(len(data0)):
    x.append(a)
    a += 1
count = 0
count = grafics(x, data0, data1, count)
data2 = []
for i in range(len(x)):
    data2.append(data1)

# обработаем
mas_1 = for_find_t(len(data0), 1, data0, 1) # совпадает со второго максимума
y1 = mas_1[1]
x_max_1 = mas_1[0]  # 1746
mas_2 = for_find_t(len(data1), 0, data1, 0)
y2 = mas_2[1]
x_max_2 = mas_2[0]  # 250

count = grafics(x, y1, y2, count)

x_true = []
a = 0
for i in range(600):
    x_true.append(a)
    a += 1
y1_new = []
for i in range(600):
    y1_new.append(y1[i + x_max_1 - x_max_2])

count = grafics(x_true, y1_new, y2, count)
T1 = x_max_1 - x_max_2  # атмосфера

# Повторим для воздуха из легких

# считаем данные
data0_1 = np.loadtxt('data_2_2.txt', dtype=int)  # время 2-ой фиксации хлопка
data1_1 = np.loadtxt('data_3_2.txt', dtype=int)  # время 1-ой фиксации хлопка
# добавим немного своих переменных
x = []
a = 0
for i in range(len(data1_1)):
    x.append(a)
    a += 1
count = grafics(x, data0_1, data1_1, count)
data2_1 = []
for i in range(len(x)):
    data2_1.append(data1_1)

# обработаем
mas_1 = for_find_t(len(data0_1), 0, data0_1, 1)
y1 = mas_1[1]
x_max_1 = mas_1[0]  # 1746
mas_2 = for_find_t(len(data1_1), 0 , data1_1, 0)
y2 = mas_2[1]
x_max_2 = mas_2[0]  # 250

count = grafics(x, y1, y2, count)

x_true = []
a = 0
for i in range(1000):
    x_true.append(a)
    a += 1
y1_new = []
for i in range(1000):
    y1_new.append(y1[i + x_max_1 - x_max_2])
count = grafics(x_true, y1_new, y2, count)

T2 = x_max_1 - x_max_2  # Колво считываний в воздухе из легких

# вычисления
L = 1.158
delta_T_atm = T1 / 500000
delta_T_ugl = T2 / 500000

c_atm = L / delta_T_atm
c_ugl = L / delta_T_ugl

print('Скорость звука в атмосфере')
print(c_atm)

print('---')

print('Скорость звука в воздухе из легких')
print(c_ugl)

analytics()  # сделаем аналит график, запустив вышесделенную функцию

t = 26  # в цельсиях
Vp = 0.359
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
fig, ax = plt.subplots()
ax.grid(which="major", linewidth=1)
ax.grid(which="minor", linewidth=0.3)
ax.minorticks_on()
ax.set_xlim(0, 0.075)
ax.set_ylim(338, 352)


# для атмосферы:
def foo(x, a, b):    return a * x + b


popt, pcov = curve_fit(foo, x, y1)
k1 = popt[0]  # коэфцициент наклона
b1 = popt[1]  # f(0)
ugl1 = (c_atm - b1) / k1
print('концентрация угл газа в атмосфере: ', ugl1 * 100, '%')
plt.plot(x, foo(x, *popt), color='orange', label="Влажность, измеренная в учебной аудитории", linestyle='-')


# для воздуха из легких
def foo(x, a, b):
    return a * x + b


popt, pcov = curve_fit(foo, x, y2)
k2 = popt[0]  # коэф наклона
b2 = popt[1]  # f(0)
ugl2 = (c_ugl - b2) / k2
print('концентрация угл газа в воздухе из легких: ', ugl2 * 100, '%')

plt.plot(x, foo(x, *popt), color='red', label="100% влажность", linestyle='-')
plt.scatter([ugl1, ugl2], [c_atm, c_ugl], color='Black')  # наносим точки на график

plt.xlabel('Концентрация углекислого газа')
plt.ylabel('Скорость звука, м/с')
plt.legend()
fig1 = plt.gcf()
plt.show()
fig.savefig('uglic.png', dpi=600)


# обработаем
x = []
a = 0
for i in range(len(data0)):
    x.append(a)
    a += 1
count = grafics(x, data0, data1, count)
data2 = []
for i in range(len(x)):
    data2.append(data1)

mas_1 = for_find_t(len(data0),0, data0, 1) # совпадает со второго максимума
y1 = mas_1[1]
x_max_1 = mas_1[0]  # 1746
mas_2 = for_find_t(len(data1), 1, data1, 0)
y2 = mas_2[1]
x_max_2 = mas_2[0]  # 250

count = grafics(x, y1, y2, count)

x_true = []
a = 0
for i in range(600):
    x_true.append(a)
    a += 1
y1_new = []
for i in range(600):
    y1_new.append(y1[i + x_max_1 - x_max_2])

count = grafics(x_true, y1_new, y2, count)
T1 = x_max_1 - x_max_2  # атмосфера
delta_T_atm = T1 / 500000
c_ugl = L / delta_T_atm
print(c_ugl)


