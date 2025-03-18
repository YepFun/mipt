import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Данные
T = np.array([25.0, 28.0, 31.0, 34.0, 37.1, 40.0, 43.1, 46.0, 49.0, 52.0, 54.9, 58.0, 61.0])  # Температура
sigma = np.array([83.4, 82.9, 82.4, 82.2, 81.9, 81.7, 81.4, 80.9, 80.3, 79.8, 79.4, 78.8, 78.4])  # Поверхностное натяжение
sigma_err = np.array([2.0, 1.9, 1.9, 1.9, 1.9, 1.9, 1.9, 1.9, 1.9, 1.9, 1.9, 1.9, 1.8])  # Погрешность

# Аппроксимация методом МНК
slope, intercept, r_value, p_value, std_err = linregress(T, sigma)

# Построение графика
plt.figure(figsize=(8, 6))
plt.errorbar(T, sigma, xerr=0.3, yerr=sigma_err, fmt='o', capsize=4, label='Экспериментальные данные')
plt.plot(T, slope * T + intercept, 'r--', label=f'Линейная аппроксимация\n$\sigma = {slope:.3f}T + {intercept:.1f}$')
plt.xlabel('Температура, °C')
plt.ylabel('Коэф. поверхностного натяжения $\sigma$, мН/м')
plt.title('Зависимость поверхностного натяжения от температуры')
plt.grid(True)
plt.tight_layout()
plt.legend()

# Сохранение графика
plt.savefig('images/graph.png')

# Вывод параметров аппроксимации
print(f'Угловой коэффициент: {slope:.3f} ± {std_err:.3f} мН/(м·°C)')

# Константа производной
d_sigma_dT = -0.135  # мН/(м·°C)
d_sigma_dT_err = 0.008  # мН/(м·°C)

# Расчет q и UF
q = -T * d_sigma_dT
UF = sigma - T * d_sigma_dT

# Расчет погрешностей
# Погрешности для q и UF
q_err = np.sqrt((sigma_err * abs(d_sigma_dT))**2 + (T * d_sigma_dT_err)**2)
UF_err = np.sqrt((sigma_err * abs(d_sigma_dT))**2 + (T * d_sigma_dT_err)**2)

# Вывод результатов
print("q:", q)
print("q_err:", q_err)
print("UF:", UF)
print("UF_err:", UF_err)

# Построение графика
plt.figure(figsize=(8, 6))

slope1, intercept1, r_value1, p_value1, std_err1 = linregress(T, q)
slope2, intercept2, r_value2, p_value2, std_err2 = linregress(T, UF)

plt.errorbar(T, q, yerr=q_err, fmt='o', capsize=4, label='q(T)', color='blue')
plt.errorbar(T, UF, yerr=UF_err, fmt='o', capsize=4, label='U/П(T)', color='red')
plt.plot(T, slope1 * T + intercept1, 'k--', label=f'$q = {slope:.4f}T + {intercept:.2f}$', alpha=0.5)
plt.plot(T, slope2 * T + intercept2, 'k--', label=f'$U/F = {slope:.4f}T + {intercept:.2f}$', alpha=0.5)
plt.xlabel('Температура, °C')
plt.ylabel('q и U/П, мН/м')
plt.title('Зависимость q и U/П от T')
plt.grid(True)
plt.tight_layout()
plt.legend()

# Сохранение графика
plt.savefig('images/graph_new.png')