import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Данные из таблицы
T = np.array([23.0, 30.0, 40.3, 50.0, 60.0, 70.1, 80.0])  # Температура в °C
kappa = np.array([0.0249, 0.0256, 0.0258, 0.0271, 0.0277, 0.0286, 0.0295])  # Теплопроводность в Вт/(м·К)
sigma_kappa = np.array([0.0014, 0.0014, 0.0014, 0.0015, 0.0015, 0.0016, 0.0016])  # Погрешности kappa

# Функция для аппроксимации (линейная)
def linear_func(x, a, b):
    return a * x + b

# Подгонка методом χ² (с учетом погрешностей sigma_kappa)
popt, pcov = curve_fit(linear_func, T, kappa, sigma=sigma_kappa, absolute_sigma=True)
a, b = popt  # a - угловой коэффициент, b - свободный член
sigma_a, sigma_b = np.sqrt(np.diag(pcov))  # погрешности коэффициентов

# Вывод результатов
print(f"Угловой коэффициент (a) = {a:.6f} ± {sigma_a:.6f} [Вт/(м·К·°C)]")
print(f"Свободный коэффициент (b) = {b:.4f} ± {sigma_b:.4f} [Вт/(м·К)]")

# Построение графика
plt.figure(figsize=(8, 6))

# Данные с крестами погрешностей
plt.errorbar(T, kappa, yerr=sigma_kappa, fmt='o', capsize=3, label='Данные')

# Аппроксимирующая прямая
T_fit = np.linspace(min(T), max(T), 100)
kappa_fit = linear_func(T_fit, a, b)
plt.plot(T_fit, kappa_fit, 'r-', label=f'κ(T) = ({a:.6f} ± {sigma_a:.6f})·T + ({b:.4f} ± {sigma_b:.4f})')

# Настройки графика
plt.xlabel('T, °C')
plt.ylabel('κ, Вт/(м·К)')
plt.title('Зависимость теплопроводности от температуры')
plt.legend()  # Стандартное расположение легенды
plt.grid(True)
plt.tight_layout()

plt.savefig("images/graph_kT.png")