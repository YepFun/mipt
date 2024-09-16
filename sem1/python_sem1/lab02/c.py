x, p, y = map(int, input().split())
x *= 100
y *= 100
p = 1 + p / 100
year = 0
while x < y:
    x = int(x * p)
    year += 1
print(year)