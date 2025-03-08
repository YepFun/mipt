import numpy as np
import matplotlib.pyplot as plt
import os
from scipy import stats

# Функция для чтения данных из файла
def read_data(file_name):
    data = np.loadtxt(file_name, skiprows=1)  # Пропускаем заголовок
    return data[:, 1], data[:, 0]  # Возвращаем значения по оси абсцисс и ординат

# Функция для аппроксимации данных методом МНК с использованием scipy.stats.linregress
def fit_line(x, y):
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    
    # Вычисление погрешности (среднеквадратическая ошибка)
    y_fit = slope * x + intercept
    error = np.sqrt(np.mean((y - y_fit) ** 2))
    
    return slope, intercept, error, y_fit

# Загрузка данных
x_worse_1, y_worse_1 = read_data('data/worse_1.txt')
x_worse_2, y_worse_2 = read_data('data/worse_2.txt')
x_better_1, y_better_1 = read_data('data/better_1.txt')
x_better_2, y_better_2 = read_data('data/better_2.txt')

# Фитинг прямой для worse_1 и worse_2
m_worse_1, c_worse_1, error_worse_1, y_fit_worse_1 = fit_line(y_worse_1, x_worse_1)  # Поменяли местами
m_worse_2, c_worse_2, error_worse_2, y_fit_worse_2 = fit_line(y_worse_2, x_worse_2)  # Поменяли местами

# Фитинг прямой для better_1 и better_2 без последних трех точек
m_better_1, c_better_1, error_better_1, y_fit_better_1 = fit_line(y_better_1[:-3], x_better_1[:-3])
m_better_2, c_better_2, error_better_2, y_fit_better_2 = fit_line(y_better_2[:-3], x_better_2[:-3])

# Генерация значений аппроксимирующей прямой для полного диапазона x
y_fit_better_1_full = m_better_1 * y_better_1 + c_better_1
y_fit_better_2_full = m_better_2 * y_better_2 + c_better_2  

# Создание директории images, если она не существует
if not os.path.exists('images'):
    os.makedirs('images')

# График для данных worse_1 и worse_2 на одной координатной плоскости
plt.figure(figsize=(8, 6))
plt.scatter(y_worse_1, x_worse_1, label='worse_1', color='red', alpha=0.35)
plt.scatter(y_worse_2, x_worse_2, label='worse_2', color='blue', alpha=0.35)
plt.plot(y_worse_1, y_fit_worse_1, 'r--', label=f'Ухудшение, 1: y = {m_worse_1:.4f}x + {c_worse_1:.4f}')
plt.plot(y_worse_2, y_fit_worse_2, 'b--', label=f'Ухудшение, 2: y = {m_worse_2:.4f}x + {c_worse_2:.4f}')
plt.title('График P(t) для ухудшения вакуума')
plt.ylabel('P, $10^{-4}$ торр')
plt.xlabel('t, с')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('images/graph_worse.png')

# График для данных better_1 и better_2 на одной координатной плоскости
plt.figure(figsize=(8, 6))
plt.scatter(y_better_1, x_better_1, label='better_1', color='red', alpha=0.35)
plt.scatter(y_better_2, x_better_2, label='better_2', color='blue', alpha=0.35)
plt.plot(y_better_1, y_fit_better_1_full, 'r--', label=f'Улучшение, 1: y = {m_better_1:.4f}x + {c_better_1:.4f}')
plt.plot(y_better_2, y_fit_better_2_full, 'b--', label=f'Улучшение, 2: y = {m_better_2:.4f}x + {c_better_2:.4f}')
plt.title('График для улучшения вакуума')
plt.ylabel('ln(p-$p_{пр}$)/($p_0$-$p_{пр}$), 1')
plt.xlabel('t, с')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('images/graph_better.png')

# Печать результатов
print(f"worse_1: m = {m_worse_1:.4f}, c = {c_worse_1:.4f}, error = {error_worse_1:.4f}")
print(f"worse_2: m = {m_worse_2:.4f}, c = {c_worse_2:.4f}, error = {error_worse_2:.4f}")
print(f"better_1: m = {m_better_1:.4f}, c = {c_better_1:.4f}, error = {error_better_1:.4f}")
print(f"better_2: m = {m_better_2:.4f}, c = {c_better_2:.4f}, error = {error_better_2:.4f}")
