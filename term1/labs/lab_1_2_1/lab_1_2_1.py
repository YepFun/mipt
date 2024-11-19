import math

def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    m1, x_left, x_right = [], [], []
    m2, delta_x2 = [], []

    for line in lines[:5]:
        values = list(map(float, line.split()))
        m1.append(values[0])
        x_left.append(values[1])
        x_right.append(values[2])

    for line in lines[5:]:
        values = list(map(float, line.split()))
        m2.append(values[0])
        delta_x2.append(values[1])

    return m1, x_left, x_right, m2, delta_x2

def analyze_part_1(m1, x_left, x_right):
    # Параметры установки
    M = 2925
    sigma_M = 5
    eps_M = sigma_M / M
    L = 2200
    sigma_L = 5
    eps_L = sigma_L / L
    sigma_delta_x1 = 0.5 #mm

    delta_x1, u, eps_u, sigma_u = [], [], [], []
    for i in range(len(m1)):
        delta_x1.append(x_right[i] - x_left[i])
        u.append(M / m1[i] * math.sqrt(9.81 / (L * 0.001)) * delta_x1[i] * 0.001)
        eps_u.append(math.sqrt(eps_M * eps_M + (0.003 / m1[i]) * (0.003 / m1[i]) + (0.5 * eps_L) * (0.5 * eps_L) + (sigma_delta_x1 / delta_x1[i]) * (sigma_delta_x1 / delta_x1[i])))
        sigma_u.append(eps_u[i] * u[i])

    average_m1, average_delta_x1, average_u, average_sigma_u = 0.0, 0.0, 0.0, 0.0
    for i in range(len(m1)):
        average_m1 += m1[i]
        average_delta_x1 += delta_x1[i]
        average_u += u[i]
        average_sigma_u += sigma_u[i]
    average_m1 /= len(u)
    average_delta_x1 /= len(u)
    average_u /= len(u)
    average_sigma_u /= len(u)

    return delta_x1, u, eps_u, sigma_u, average_m1, average_delta_x1, average_u, average_sigma_u

def analyze_part_2(m2, delta_x2):
    # Параметры установки
    r = 205
    sigma_r = 1
    R = (728 - 55) / 2
    sigma_R = 1
    m1 = 735.6
    m2 = 733.3
    m = (m1 + m2) / 2
    sigma_m = (m1 - m2) / 2

def print_table_1(m1, x_left, x_right, delta_x1, u, eps_u, sigma_u):
    header = f"{'m1':>10} {'x_left':>10} {'x_right':>10} {'delta_x1':>10} {'u':>15} {'eps_u':>10} {'sigma_u':>10}"
    print(header)
    print("-" * len(header))

    # Форматированный вывод строк таблицы
    for i in range(len(m1)):
        print(f"{m1[i]:10.3f} {x_left[i]:10.3f} {x_right[i]:10.3f} {delta_x1[i]:10.3f} {u[i]:15.5f} {eps_u[i]:10.5f} {sigma_u[i]:10.5f}")

    # Итоги
    print("-" * len(header))
    print("average:")
    print(
        f"{average_m1:10.3f} {'':>10} {'':>10} {average_delta_x1:10.3f} {average_u:15.5f} {'':>10} {average_sigma_u:10.5f}")

file_path = 'data.txt'
m1, x_left, x_right, m2, delta_x2 = read_file(file_path)
delta_x1, u, eps_u, sigma_u, average_m1, average_delta_x1, average_u, average_sigma_u = analyze_part_1(m1, x_left, x_right)
print_table_1(m1, x_left, x_right, delta_x1, u, eps_u, sigma_u)
