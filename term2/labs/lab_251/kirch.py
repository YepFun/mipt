import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Данные
T = np.array([25.0, 28.0, 31.0, 34.0, 37.1, 40.0, 43.1, 46.0, 49.0, 52.0, 54.9, 58.0, 61.0])
h = np.array([197.0, 195.8, 194.6, 194.2, 193.6, 193.0, 192.2, 191.0, 189.6, 188.4, 187.4, 186.0, 185.2])
dT = 0.3
dh = 4

# Метод наименьших квадратов (МНК)
slope, intercept, r_value, p_value, std_err = linregress(T, h)

# Построение графика
plt.figure(figsize=(8, 6))

# График экспериментальных данных с погрешностями
plt.errorbar(T, h, xerr=dT, yerr=dh, fmt='o', label='Экспериментальные данные', capsize=3)

# График прямой МНК
T_fit = np.linspace(min(T), max(T), 100)
h_fit = slope * T_fit + intercept
plt.plot(T_fit, h_fit, 'r-', label=f'МНК: h = {slope:.4f}T + {intercept:.2f}')

# Настройки графика
plt.xlabel('T, °C')
plt.ylabel('h, мм')
plt.title('График h(T)')
plt.legend()
plt.grid()
plt.tight_layout()

# Вывод погрешности углового коэффициента
print(f'Угловой коэффициент: {slope:.4f} ± {std_err:.4f}')

# Показать график
plt.savefig("images/kirch.png")
