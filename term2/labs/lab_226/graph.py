import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Данные для стеклянных шариков
T_glass = np.array([3.356, 3.299, 3.247, 3.196, 3.146, 3.095, 3.046, 2.998])  # 1/T
ln_eta_glass = np.array([-0.484178967, -0.791080108, -1.174595283, -1.464294688, -1.875087844, 
                         -2.070207884, -2.374559394, -2.622992016])
d_ln_eta_glass = np.array([0.065, 0.065, 0.045, 0.045, 0.055, 0.065, 0.055, 0.065])

# Данные для металлических шариков
T_metal = np.array([3.356, 3.299, 3.247, 3.196, 3.146, 3.095, 3.046, 2.998])  # 1/T
ln_eta_metal = np.array([-0.410890316, -0.738847872, -1.273325988, -1.779458402, -1.817383556,
                         -2.153635705, -2.440192005, -2.673436797])
d_ln_eta_metal = np.array([0.115, 0.115, 0.135, 0.125, 0.125, 0.125, 0.125, 0.115])

# Линейная регрессия для стеклянных шариков
k_glass, b_glass, r_value, p_value, std_err_glass = linregress(T_glass, ln_eta_glass)

# Линейная регрессия для металлических шариков
k_metal, b_metal, r_value, p_value, std_err_metal = linregress(T_metal, ln_eta_metal)

# Построение графика
plt.figure(figsize=(8, 6))

# Отображение точек для стеклянных шариков с крестами погрешности
plt.errorbar(T_glass, ln_eta_glass, yerr=d_ln_eta_glass, fmt='o', label="glass", color='blue', capsize=5)

# Отображение точек для металлических шариков с крестами погрешности
plt.errorbar(T_metal, ln_eta_metal, yerr=d_ln_eta_metal, fmt='o', label="metal", color='red', capsize=5)

# Построение прямых аппроксимаций
plt.plot(T_glass, k_glass * T_glass + b_glass, label=f"y = ({k_glass:.3f} ± {std_err_glass:.3f})x + {b_glass:.3f}", color='blue', linestyle='--')
plt.plot(T_metal, k_metal * T_metal + b_metal, label=f"y = ({k_metal:.3f} ± {std_err_metal:.3f})x + {b_metal:.3f}", color='red', linestyle='--')

# Подписи и заголовки
plt.xlabel("1/T, $10^{-3}$ 1/K")
plt.ylabel("ln η")
plt.title("Зависимость ln η от 1/T")

# Легенда
plt.legend()

# Отображение графика
plt.grid(True)
plt.tight_layout()
plt.savefig("images/graph.png")

# Печать угловых коэффициентов и их погрешностей
print(f"glass: k = {k_glass:.3f} ± {std_err_glass:.3f}")
print(f"metal: k = {k_metal:.3f} ± {std_err_metal:.3f}")
