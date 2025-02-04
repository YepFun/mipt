import matplotlib.pyplot as plt
import numpy as np
import math

def graph(y, x):
    # print(len(y), len(x))
    if len(y) != len(x):
        print("Error len(x) != len(y).")
        return

    # Преобразуем списки в массивы numpy для удобства расчетов
    x = np.array(x)
    y = np.array(y)

    # Метод наименьших квадратов для линейной регрессии
    k, b = np.polyfit(x, y, 1)  # 1 означает, что мы подбираем прямую (1-й степени)

    # Вычисляем значения y по уравнению прямой y = kx + b для всех x
    y_fit = k * x + b

    # Построение графика исходных данных
    plt.plot(x, y, marker='o', linestyle='', color='b', label='T(h^2)')

    # Построение прямой регрессии
    plt.plot(x, y_fit, linestyle='--', color='r', label=f'Fit: y = {k:.8f}x + {b:.8f}')

    # Настройка графика
    plt.title('Omega(m)')
    plt.xlabel('m, g')
    plt.ylabel('Omega, Hz')
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

def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    m, t, n = [], [], []
    T, Omega, Omega_f = [], [], []
    delta_phi = 5.0 / 180.0 * math.pi

    for line in lines:
        values = list(map(float, line.strip().split()))
        m.append(values[0])
        t.append(values[1])
        n.append(values[2])

    for i in range(len(m)):
        T.append(t[i] / n[i])
        Omega.append(2 * math.pi / T[i])
        Omega_f.append(delta_phi / t[i] * 1e3)

    print(f"{'m, g':>6}{'n, 1':>6}{'t, s':>10}{'T, s':>10}{'Omega, Hz':>12}{'Omega_f, mHz':>14}")
    for i in range(len(m)):
        print(f"{m[i]:6.1f}{n[i]:6.1f}{t[i]:10.2f}{T[i]:10.3f}{Omega[i]:12.5f}{Omega_f[i]:14.5f}")

    i = 0
    average_m, average_T, average_Omega, average_Omega_f = [], [], [], []
    while i < len(m):
        average_m.append(m[i] * 0.001)
        average_T.append(0.2 * (T[i] + T[i + 1] + T[i + 2] + T[i + 3] + T[i + 4]))
        average_Omega.append(0.2 * (Omega[i] + Omega[i + 1] + Omega[i + 2] + Omega[i + 3] + Omega[i + 4]))
        average_Omega_f.append(0.2 * (Omega_f[i] + Omega_f[i + 1] + Omega_f[i + 2] + Omega_f[i + 3] + Omega_f[i + 4]))
        i += 5
    print("average")
    for j in range(len(average_m)):
        print(average_m[j], "\t", average_T[j], "\t", average_Omega[j], "\t", average_Omega_f[j])

    return average_Omega, average_m

Omega, m = read_file("data_hyroscope.txt")
graph(Omega, m)
