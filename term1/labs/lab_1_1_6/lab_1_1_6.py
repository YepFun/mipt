import matplotlib.pyplot as plt
import numpy as np

def graph():
    x_data = []
    y_data = []

    with open('data.txt', 'r') as f:
        for line in f:
            y, x = line.strip().split()
            x_data.append(float(x))
            y_data.append(float(y))

    average_x, average_y, average_xy = 0.0, 0.0, 0.0
    for i in range(len(x)):
        average_x += x_data[i]
        average_y += y_data[i]
        average_xy += (x_data[i] * y_data[i])
    average_x /= len(x)
    average_y /= len(x)
    average_xy /= len(x)
    print(average_x, average_y, average_xy)

    # Преобразуем списки в массивы numpy для удобства расчетов
    x_data = np.array(x_data)
    y_data = np.array(y_data)

    # Метод наименьших квадратов для линейной регрессии
    k, b = np.polyfit(x_data, y_data, 1)  # 1 означает, что мы подбираем прямую (1-й степени)

    # Вычисляем значения y по уравнению прямой y = kx + b для всех x
    y_fit = k * x_data + b

    # Построение графика исходных данных
    plt.plot(x_data, y_data, marker='o', linestyle='', color='b', label='')

    # Построение прямой регрессии
    # plt.plot(x_data, y_fit, linestyle='--', color='r', label=f'Fit: y = {k:.2f}x + {b:.2f}')

    # Настройка графика
    plt.title('График зависимости разности ФЧХ каналов осциллографа от частоты')
    plt.xlabel('lg(f), 1')
    plt.ylabel('разность ФЧХ, 1')
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
