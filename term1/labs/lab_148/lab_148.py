import matplotlib.pyplot as plt
import numpy as np

def graph():
    x_data1 = []
    y_data1 = []

    with open('data_copper.txt', 'r') as f:
        for line in f:
            x, y = line.strip().split()
            x_data1.append(float(x))
            y_data1.append(float(y))

    # Преобразуем списки в массивы numpy для удобства расчетов
    x_data1 = np.array(x_data1)
    y_data1 = np.array(y_data1)

    x_data2 = []
    y_data2 = []

    with open('data_aluminium.txt', 'r') as f:
        for line in f:
            x, y = line.strip().split()
            x_data2.append(float(x))
            y_data2.append(float(y))

    # Преобразуем списки в массивы numpy для удобства расчетов
    x_data2 = np.array(x_data2)
    y_data2 = np.array(y_data2)

    x_data3 = []
    y_data3 = []

    with open('data_steel.txt', 'r') as f:
        for line in f:
            x, y = line.strip().split()
            x_data3.append(float(x))
            y_data3.append(float(y))

    # Преобразуем списки в массивы numpy для удобства расчетов
    x_data3 = np.array(x_data3)
    y_data3 = np.array(y_data3)

    # Метод наименьших квадратов для линейной регрессии
    k1, b1 = np.polyfit(x_data1, y_data1, 1)  # 1 означает, что мы подбираем прямую (1-й степени)
    k2, b2 = np.polyfit(x_data2, y_data2, 1)
    k3, b3 = np.polyfit(x_data3, y_data3, 1)

    # Вычисляем значения y по уравнению прямой y = kx + b для всех x
    y_fit1 = k1 * x_data1 + b1
    y_fit2 = k2 * x_data2 + b2
    y_fit3 = k3 * x_data3 + b3

    # Построение графика исходных данных
    plt.plot(x_data1, y_data1, marker='o', linestyle='', color='brown', label='copper')
    plt.plot(x_data2, y_data2, marker='o', linestyle='', color='gray', label='aluminium')
    plt.plot(x_data3, y_data3, marker='o', linestyle='', color='black', label='steel')

    # Построение прямой регрессии
    plt.plot(x_data1, y_fit1, linestyle='--', color='black', label=f'Fit: y = {k1:.4f}x + {b1:.4f}')
    plt.plot(x_data2, y_fit2, linestyle='--', color='black', label=f'Fit: y = {k2:.4f}x + {b2:.4f}')
    plt.plot(x_data3, y_fit3, linestyle='--', color='black', label=f'Fit: y = {k3:.4f}x + {b3:.4f}')

    # Настройка графика
    plt.title('f_n(n)')
    plt.xlabel('n, 1')
    plt.ylabel('f_n, kHz')
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

graph()
