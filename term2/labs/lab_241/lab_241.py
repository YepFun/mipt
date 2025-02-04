import numpy as np
import matplotlib.pyplot as plt

# Исходные данные
T = np.array([20.045, 21.005, 22.055, 23.03, 24.00, 25.025, 26.00, 27.00, 28.015, 29.01])  # Температура в °C
P = np.array([4482.7776, 4963.0752, 5224.57056, 5682.63216, 6104.22672, 6533.82624, 
              6868.25568, 7306.7496, 7698.99264, 8196.1896])  # Давление (Па)

dT = np.array([0.045, 0.005, 0.015, 0.01, 0.01, 0.005, 0.01, 0.0, 0.025, 0.0])  # Погрешность температуры
dP = np.array([112.06944, 71.1552, 44.472, 9.48736, 61.66784, 27.27616, 51.58752, 72.34112, 20.7536, 18.38176])  # Погрешность давления

# Перевод температуры в Кельвины
T_K = T + 273.15  # Температура в Кельвинах

# Пересчет величин
inv_T_K = 1 / T_K  # 1/T_K
lnP = np.log(P)  # lnP

# Расчет погрешностей
dT_K = dT  # Погрешность температуры в Кельвинах
d_inv_T_K = dT_K / (T_K**2)  # Погрешность для 1/T_K
d_lnP = dP / P  # Погрешность для lnP (относительная погрешность)

# Подбор линейной регрессии (мнк) для ln(P) от 1/T_K
coeffs = np.polyfit(inv_T_K, lnP, 1)  # Коэффициенты прямой (угловой и свободный)
slope = coeffs[0]  # Угловой коэффициент
intercept = coeffs[1]  # Свободный член

# График 1: P(T) с погрешностями
plt.figure(figsize=(8, 6))
plt.errorbar(T, P, xerr=dT, yerr=dP, fmt='o', ecolor='red', capsize=3, label="Экспериментальные данные")
plt.xlabel("T, °C")
plt.ylabel("P, Па")
plt.title("Зависимость P от T")
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend()
plt.tight_layout()

# Сохранение графика 1
plt.savefig("images/graph1.png", dpi=300)
plt.close()

# График 2: ln(P) от 1/T_K с погрешностями
plt.figure(figsize=(8, 6))
plt.errorbar(inv_T_K, lnP, xerr=d_inv_T_K, yerr=d_lnP, fmt='o', ecolor='blue', capsize=3, label="Экспериментальные данные")

# Линия, полученная методом наименьших квадратов
plt.plot(inv_T_K, np.polyval(coeffs, inv_T_K), 'g--', label=f"Линия МНК: $y = {slope:.3f}x + {intercept:.3f}$")

plt.xlabel("1/T_K, 1/K")
plt.ylabel("ln(P), 1")
plt.title("Зависимость ln(P) от 1/T_K")
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend()
plt.tight_layout()

# Сохранение графика 2
plt.savefig("images/graph2.png", dpi=300)
plt.close()
