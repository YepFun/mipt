import numpy as np
import matplotlib.pyplot as plt

# Данные
T = np.array([23.0, 30.0, 40.3, 50.0, 60.0, 70.1, 80.0])  # Температура, °C
R = np.array([19.4740, 19.9656, 20.6881, 21.3775, 22.0891, 22.8018, 23.5186])  # Сопротивление, Ом
sigma_R = np.array([0.0024, 0.0015, 0.0013, 0.0008, 0.0009, 0.0007, 0.0012])  # Погрешности R

# Взвешенный МНК (веса = 1 / sigma_R²)
weights = 1 / sigma_R**2
coeffs, cov = np.polyfit(T, R, deg=1, w=weights, cov=True)

# Получаем коэффициенты a (наклон) и b (свободный член)
a_opt, b_opt = coeffs
# Ошибки коэффициентов (из ковариационной матрицы)
a_error, b_error = np.sqrt(np.diag(cov))

# Построение графика
T_fit = np.linspace(min(T) - 2, max(T) + 2, 200)
R_fit = a_opt * T_fit + b_opt

plt.figure(figsize=(8, 6))
plt.errorbar(T, R, yerr=sigma_R, fmt='o', color='blue', label='Данные', capsize=5)
plt.plot(T_fit, R_fit, 'r-', label=f'R = {a_opt:.5f}±{a_error:.5f}·T + {b_opt:.4f}±{b_error:.4f}')

plt.xlabel('T, °C')
plt.ylabel('R, Ом')
plt.title('Зависимость сопротивления от температуры')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("images/graph_RT.png")

# Вывод результатов
print(f"Коэффициент наклона (a) = {a_opt:.5f} ± {a_error:.5f} Ом/°C")
print(f"Свободный член (b) = {b_opt:.4f} ± {b_error:.4f} Ом")