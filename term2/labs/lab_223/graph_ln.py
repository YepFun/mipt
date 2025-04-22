import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Данные из таблицы
ln_T = np.array([5.6904, 5.7137, 5.7472, 5.7777, 5.8081, 5.8380, 5.8665])  # x
ln_dQdT = np.array([-4.369, -4.340, -4.332, -4.2859, -4.261, -4.2303, -4.198])  # y
sigma_x = np.array([0.0003] * 7)  # погрешности x
sigma_y = np.array([0.006, 0.005, 0.004, 0.0027, 0.003, 0.0024, 0.003])  # погрешности y

# Функция для аппроксимации (линейная)
def linear_func(x, a, b):
    return a * x + b

# Веса для МНК (1/σ²)
weights = 1 / (sigma_y**2)

# Подгонка методом χ² (curve_fit с весами)
popt, pcov = curve_fit(linear_func, ln_T, ln_dQdT, sigma=sigma_y, absolute_sigma=True)
a, b = popt  # a - угловой коэффициент, b - свободный член
sigma_a, sigma_b = np.sqrt(np.diag(pcov))  # погрешности коэффициентов

# Вывод результатов
print(f"Угловой коэффициент (a) = {a:.4f} ± {sigma_a:.4f}")
print(f"Свободный коэффициент (b) = {b:.4f} ± {sigma_b:.4f}")

# Построение графика
plt.figure(figsize=(8, 6))

# Данные с крестами погрешностей
plt.errorbar(ln_T, ln_dQdT, xerr=sigma_x, yerr=sigma_y, fmt='o', capsize=3, label='Данные')

# Аппроксимирующая прямая
x_fit = np.linspace(min(ln_T), max(ln_T), 100)
y_fit = linear_func(x_fit, a, b)
plt.plot(x_fit, y_fit, 'r-', label=f'y = ({a:.3f}±{sigma_a:.3f})x + ({b:.3f}±{sigma_b:.3f})')

# Настройки графика
plt.xlabel('ln(T), 1')
plt.ylabel('ln(dQ/d(ΔT)), 1')
plt.title('Зависимость ln(dQ/d(ΔT)) от ln(T)')
plt.legend(fontsize=12)
plt.grid(True)
plt.tight_layout()

plt.savefig("images/graph_ln.png")