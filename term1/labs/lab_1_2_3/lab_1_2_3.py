import matplotlib.pyplot as plt
import numpy as np
import math

def general():
    """
    R =
    sigma_R =
    r =
    sigma_r =

    L =
    sigma_L = 1  # cm
    R0 =
    sigma_R0 =
    z0 = math.sqrt(L * L - R0 * R0)
    sigma_z0 = z0 * (sigma_L + sigma_R0)
    print("z0 = ", z0, "+-", sigma_z0)

    k = 9.81 * r * R / (4 * math.pi * math.pi * z0)
    sigma_k = k * math.sqrt(sigma_r / r * sigma_r / r + sigma_R / R * sigma_R / R + sigma_z0 / z0 * sigma_z0 / z0)
    print("k =", k, "+-", sigma_k)

    m_disc =
    m_block =
    m_ring =
    sigma_mass = 0.3  # g
    """

def graph():
    x_data = []
    y_data = []

    with open('data.txt', 'r') as f:
        for line in f:
            x, y = line.strip().split()
            x_data.append(float(x))  
            y_data.append(float(y))

    # Преобразуем списки в массивы numpy для удобства расчетов
    x_data = np.array(x_data)
    y_data = np.array(y_data)

    # Метод наименьших квадратов для линейной регрессии
    k, b = np.polyfit(x_data, y_data, 1)  # 1 означает, что мы подбираем прямую (1-й степени)

    # Вычисляем значения y по уравнению прямой y = kx + b для всех x
    y_fit = k * x_data + b

    # Построение графика исходных данных
    plt.plot(x_data, y_data, marker='o', linestyle='', color='b', label='T(h^2)')

    # Построение прямой регрессии
    plt.plot(x_data, y_fit, linestyle='--', color='r', label=f'Fit: y = {k:.2f}x + {b:.2f}')

    # Настройка графика
    plt.title('I(h^2)')
    plt.xlabel('h^2, 10^3 * m^2')
    plt.ylabel('I, 10^3 kg * m^2')
    plt.legend()

    # Включаем основную сетку
    plt.grid(True, which='major', axis='both', color='gray', linestyle='-', linewidth=0.7)

    # Включаем минорные тики на обеих осях
    plt.minorticks_on()

    # Добавляем мелкую сетку для минорных тиков
    plt.grid(True, which='minor', axis='both', color='gray', linestyle=':', linewidth=0.5)

    # Показ графика
    # plt.show()
    plt.savefig('graph.png', dpi=300, bbox_inches='tight')  # dpi - разрешение, bbox_inches - убирает лишние поля

general()
graph()

def I(k, m, t):
    i = k * m * t * t
    eps_i = math.sqrt((0.05/4.02) * (0.05/4.02) + 2 * (0.002/t) * (0.002/t) + (0.0003/m) * (0.3/m))
    sigma_i = i * eps_i
    return i, sigma_i, eps_i

def print_I(k, m, t):
    i, sigma_i, eps_i = I(k, m, t)
    print(i, "+-", sigma_i, "| eps =", eps_i * 100, "%")

k = 4.02e-4
eps_k = 0.012
m_platform = 1066.8e-3
m_cylinder = 737.4e-3
m_block = 1199.4e-3
t_platform = 4.368
t_cylinder = 4.227
t_block = 3.745
t_block_and_cylinder = 3.821

print_I(k, m_platform, t_platform)
print_I(k, m_platform + m_cylinder, t_cylinder)
print_I(k, m_platform + m_block, t_block)
print_I(k, m_platform + m_block + m_cylinder, t_block_and_cylinder)
