def calculate_profit(n):
    m, f = 0.3 * 100 + 10, 0.7 * 100
    for i in range(1, n + 1):
        m = 0.3 * (100.0 + 2 * f) + 10
        f = 0.7 * (100.0 + 2 * f)
    return m, f

n = int(input())
n -= 1
print(int(calculate_profit(n)[0]))
