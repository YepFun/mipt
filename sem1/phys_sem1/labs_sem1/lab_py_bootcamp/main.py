import numpy as np # Умные массивы и арифметические операции (многие функции из math модуля типа pow, sqrt доступны и в нём)
import pandas as pd # Большая библиотека для работы с данными, мы используем для быстрого импорта данных из файла excel или csv
import matplotlib.pyplot as plt # Графики
import matplotlib as mpl

"""
    Eng:
        Returns coefficients b, k and their standard errors s_k, s_b
    from linear approximation (using least squares) y = k * x + b to
    given points (x, y).
    Rus:
        Возвращает коэффициенты b, k и их погрешности s_b, s_k при
    линейной аппроксимации y = k * x + b методом МНК по введённым точкам (х, у).

    Parameters
    ----------
    x : numpy.ndarray
        Numpy array with x coordinates of points.

    y : numpy.ndarray
        Numpy array with y coordinates of points. Vectors x and y must be the same length.

    Returns
    -------
    out : tuple
        (k, s_k, b, s_b)
"""

def linear_least_squares(x, y):
    xy = np.mean(x * y)
    x1y = np.mean(x) * np.mean(y)
    x2 = np.mean(x * x)
    x12 = np.mean(x) ** 2
    y2 = np.mean(y * y)
    y12 = np.mean(y) ** 2
    k = (xy - x1y) / (x2 - x12)
    b = np.mean(y) - k * np.mean(x)
    s_k = np.sqrt(1 / x.size) * np.sqrt((y2 - y12) / (x2 - x12) - k ** 2)
    s_b = s_k * np.sqrt(x2 - x12)
    return k, s_k, b, s_b

PLOT_FOLDER = './tex/images/'

# Считываем данные в массив data

data = pd.read_excel("./lab_data/data_lab_1_1_1.xlsx", index_col=0).to_numpy() # Считываем файл в специфический формат и сразу же конвертируем его в numpy.array для дальнейшей работы

t = data[:, 0]
y = data[:, 1]

sr_y = 0.04

y1 = np.log(y)
s_y1 = np.abs(sr_y * y1)

# Вычисляем коэффициенты прямой методом МНК

k, s_k, b, s_b = linear_least_squares(t, y1)

x_app = np.linspace(t[4], t[0], 20) # Чтобы провести прямую задаём х, для которых будем вычислять y = k * x
y_app = k*x_app + b # Вычисляем y

# Строим график с крестами ошибок: так как у номеров колец погрешности нет, то параметр x_err для указания погрешности точек по оси х не прописываем
# Описание параметров: m, y - координаты точек на графике, y_err - погрешность по оси y, lw - толщина линии, так как обычно соседние точки не соединяют прямыми, то равна 0
# capsize - длина перпендикулярной палки креста ошибок (попробуйте поменять и сравнить графики до и после, возможно так нагляднее)
# capthick - её толщина, elinewidth - толщина вертикальной линии креста, figure - создаём фигуру с параметрами размера figsize в пикселях ((6, 6) - значит 600х600 пкс)
# и плотности точек на дюйм dpi - чтобы изображение не было размытым, в качестве маркера указываем кружок с пустым центром с диаметром ms=6 и толщиной линии кружка 1.5
er_plt = plt.errorbar(t, y1, yerr=s_y1, lw=0, capsize=3, capthick=1, elinewidth=1.5, figure=plt.figure(figsize=(9,7), dpi=400),
                              marker=mpl.markers.MarkerStyle("o", fillstyle="none"), ms=4, mew = 1.5)

# Строим прямую по вычисленным точкам, строка формата "-" указывает, что проводится сплошная линия 
# без маркеров (подробнее про строки форматов в разделе Notes тут https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html)
# с - сокращённо от color - цвет линии в формате RGB, linewidth - ширина линии
app = plt.plot(x_app, y_app, "-", c = [1, 0.5, 0], linewidth=2)

# Adjusting график

plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0), useMathText=True) # Масштаб в научном стиле без массы нулей с помощью отбражения степеней 10
# (попробуйте закомментировать строку чтобы увидеть разницу)
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0), useMathText=True)

plt.minorticks_on() # включаем мелкие деления (попробуйте отключить)
plt.grid(visible=True, which='major', linestyle='-', linewidth=1.5, color='0.7') # Формат основных линиий сетки
plt.grid(visible=True, which='minor', linestyle='--', linewidth=1, color='0.8') # Формат побочных линий, цвет указывается как оттенок серого - 0.0 - чёрный, 1.0 - белый
plt.rc('text', usetex=False) # Выключаем использование latex, чтобы использовался mathtext взамен 

axis_lw = 2 # Константа для толщины осей

axis_lw = 2 # Константа для толщины осей
plt.xlim([t[4]-15, t[0]+15]) # Пределы по оси х
# plt.ylim([y[4]-0.15, y[0]+0.15])
# plt.ylim([0, 5.9*10**-3]) # Пределы по оси y

plt.xlabel(r"$ I, мА$") # Название оси х
plt.ylabel(r"$ V, В$") # Название оси y

# Задаём некоторые параметры таким образом (попробуйте поменять)
plt.rc('axes', linewidth=axis_lw) # Толщина линий осей
plt.rc('xtick.major', width=axis_lw) # Тощина насечек по Ох
plt.rc('xtick.minor', width=0) # Отключаем побочные насечки по Ох
plt.rc('xtick', direction='in') # Направляем насечки по Ох внутрь графика
plt.rc('axes', labelsize=20) # Высота шрифта на названии осей
plt.rc('ytick.major', width=axis_lw) # Аналогично
plt.rc('ytick.minor', width=0)
plt.rc('ytick', direction='in')
plt.rc('xtick', labelsize=18) # Высота шрифта цифр масштаба
plt.rc('ytick', labelsize=18)
plt.rc('xtick.major', pad=10) # Отступ между осью и цифрами
plt.rc('ytick.major', pad=10)

# Легенда с автоматической подстановкой вычисленного значения коэффициента наклона прямой
# k_fmt = ("%1.2e" % (k)).split("e-") # Представляем коэффициент k в виде массива, где первый элемент - число с одной значащей цифрой слева от запятой, второй - степень десяти
# s_str = 'Аппроксимация: \n' + r"$V/I$ " + '= \n$(' + k_fmt[0] + r"\pm" + ("%1.2f" % (s_k/k*float(k_fmt[0]))) + r")\cdot 10^{-" + f"{int(k_fmt[1])}" + r"}$" + r"$\cdot t$ " 

k_fmt = ("%1.1e" % (k)).split("e-")
b_fmt = "%.1f" % (abs(b)*(10**int(k_fmt[1]))) + r" \pm " + "%.1f" % (abs(s_b)*(10**int(k_fmt[1])))
s_str = 'Аппроксимация: \n' + r"$V(I)$ " + '= $\{(' + k_fmt[0] + r"\pm" + ("%1.1f" % (s_k/k*float(k_fmt[0]))) + r")\cdot t ~ +$"+ "\n" + "$ + ~ (" + b_fmt + r")\}\cdot 10^{-" + f"{int(k_fmt[1])}" + r"}$"


# Создаём легенду - сначала массив с линиями графиков (попробуйте поменять их местами), и подписями, соответствующими каждому,
# параметр loc определяет положение легенды на графике
plt.legend([er_plt, app[0]], ["Экспериментальные \n значения", s_str], loc=0)
plt.rc('legend', fontsize=16) # Размер шрифта легенды

plt.savefig(PLOT_FOLDER + "plot_1.png", bbox_inches='tight') # Сохраняем в файл

B = np.exp(b)
s_B = B * (s_b / b)
sr_B = s_B / B

tau = -1/k
s_tau = tau * (s_k / k)
sr_tau = (s_k / k)