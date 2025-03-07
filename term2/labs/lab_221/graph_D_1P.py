import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Данные
P = np.array([41, 71, 116, 160, 201])  # давление в торр
k = np.array([-2.894, -1.619, -0.983, -0.7123, -0.5721])  # коэффициент поглощения
epsilon_k = np.array([0.04, 0.10, 0.08, 0.04, 0.03])  # погрешность коэффициента
D = np.array([9.6, 5.3, 3.2, 2.4, 1.89])  # диффузионный коэффициент в см^2/c
D_error = np.array([0.9, 0.5, 0.3, 0.2, 0.18])  # погрешности для D
inv_P = 1 / P  # обратное давление

plt.figure(figsize=(8, 6))

# Построение графика с погрешностями
plt.errorbar(inv_P, D, xerr=0.003, yerr=D_error, fmt='o', label='Данные', capsize=5)

# Метод наименьших квадратов для нахождения прямой
slope, intercept, r_value, p_value, std_err = stats.linregress(inv_P, D)

# Построение прямой, полученной методом МНК
# Добавим точку для P = 760 торр в диапазон
inv_P_atm = 1 / 760  # Обратное давление для 760 торр

# Расширяем диапазон оси x на точку для P = 760 торр
inv_P_extended = np.concatenate([inv_P, [inv_P_atm]])

# Строим прямую для расширенного диапазона
plt.plot(inv_P_extended, slope * inv_P_extended + intercept, label=f'Прямая: y = {slope:.4f}x + {intercept:.4f}', color='red')

# Отображение информации о наклоне и его погрешности
plt.text(0.1, 2, f'Наклон: {slope:.4f} ± {std_err:.4f}', fontsize=12, color='black')

# Расчет значения D для атмосферного давления
D_atm = slope * inv_P_atm + intercept

# Отображение точки на графике
plt.scatter(inv_P_atm, D_atm, color='black', zorder=5, label=f'P = 760 торр: ({inv_P_atm:.4e}, {D_atm:.2f})')

# Настройка масштабов осей
plt.xlim(inv_P_atm - 0.002, max(inv_P_extended) + 0.004)  # Устанавливаем x-ограничения
plt.ylim(D_atm - 0.7, max(D) + 1.2)  # Устанавливаем y-ограничения

# Настройки графика
plt.xlabel(r'$1/P$, торр$^{-1}$')
plt.ylabel(r'$D$, см$^2$/с')
plt.title('График зависимости $D$ от $1/P$')
plt.legend()

# Отображение графика
plt.grid(True)
plt.tight_layout()  # Для плотного расположения элементов
plt.savefig("images/graph_D_1P.png")

# Вывод коэффициента наклона и его погрешности
print(f'Коэффициент наклона: {slope:.4f} ± {std_err:.4f}')
print(f'Точка для P = 760 торр: ({inv_P_atm:.4e}, {D_atm:.2f})')

# Рассчитываем погрешность для k (коэффициента поглощения)
# Погрешность наклона
k_error = std_err

# Вывод погрешности k
print(f'Погрешность коэффициента поглощения k: {k_error:.4f}')