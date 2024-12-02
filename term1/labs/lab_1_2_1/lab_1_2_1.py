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
        m2.append(values[0] * 1e-3)
        delta_x2.append(values[1] * 1e-3)

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

def analyze_part_2(m_bullet, x):
    # Параметры установки
    r = 205 * 1e-3
    sigma_r = 1 * 1e-3
    R = (728 - 55) / 2 * 1e-3
    sigma_R = 1 * 1e-3
    d = 1348 * 1e-3
    m1 = 735.6 * 1e-3
    m2 = 733.3 * 1e-3
    m = (m1 + m2) / 2
    sigma_m = (m1 - m2) / 2

    T1 = (6.667 + 6.713 + 6.712) / 3
    T2 = (4.991 + 4.988 + 4.997) / 3
    sigma_T1 = (abs(T1 - 6.667) + abs(T1 - 6.713) + abs(T1 - 6.712)) / 3
    sigma_T2 = (abs(T2 - 4.991) + abs(T2 - 4.988) + abs(T2 - 4.997)) / 3
    print("T_1 =", T1, "+-", sigma_T1)
    print("T_2 =", T2, "+-", sigma_T2)
    sqrt_kI = 4 * math.pi * m * R * R * T1 / (T1 * T1 - T2 * T2)
    sigma_sqrt_kI = sqrt_kI * (sigma_m/m + 2 * sigma_R / R - (T1 * T1 + T2 * T2) / (T1 * T1 - T2 * T2) * sigma_T1 / T1 - 2 * T2 * sigma_T2 / (T1 * T1 - T2 * T2))
    print("sqrt_kI =", sqrt_kI, "+-", sigma_sqrt_kI)

    u = []
    eps_u = []
    sigma_u = []
    sum_u = 0
    for i in range(len(x)):
        if (2 * d * m_bullet[i] * r) != 0:
            u.append(x[i] * sqrt_kI * 1e9 / (   qd * m_bullet[i] * r * 1e9))
            sum_u += u[i]
            eps_u.append(math.sqrt((1e-3 / x[i]) * (1e-3 / x[i]) + (1/1348) * (1/1348) + (sigma_sqrt_kI/sqrt_kI) * (sigma_sqrt_kI/sqrt_kI) + (1e-6 / m_bullet[i]) * (1e-6 / m_bullet[i]) + (sigma_r / r) * sigma_r / r))
            sigma_u.append(u[i] * eps_u[i])
            print(u[i], sigma_u[i], eps_u[i])
        else:
            print('is zero')
    print("u_average =", sum_u / 5)
    return

def print_table_1(m1, x_left, x_right, delta_x1, u, eps_u, sigma_u):
    header = f"{'m1':>10} {'x_left':>10} {'x_right':>10} {'delta_x':>10} {'u':>15} {'eps_u':>10} {'sigma_u':>10}"
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
analyze_part_2(m2, delta_x2)


