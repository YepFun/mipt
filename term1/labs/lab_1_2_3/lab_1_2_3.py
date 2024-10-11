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
            x_data.append(float(x) * float(x) * 0.001)  # Трансформация для h^2
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
    plt.title('T(h^2)')
    plt.xlabel('h^2, 10^{-3} * m^2')
    plt.ylabel('T, s')
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
