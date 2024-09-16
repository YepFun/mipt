n = int(input())
m = int(input())

v = []
for i in range(n*m):
    v.append(int(input()))
v.sort()

result = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(v[i * m + j])
    result.append(row)

for i in range(n):
    print(*result[i])
