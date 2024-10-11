a = []
b = []

n = int(input())

for i in range(n):
    a.append(input())
for i in range(n):
    b.append(int(input()))

c = [None] * (n)
for i in range(n):
    c[i] = a[b[i]]
print(*c)
