n = int(input())
v = []
for i in range(n):
    v.append(int(input()))

digit = -1
max_count = 0
for i in range(n):
    if max_count < v.count(v[i]):
        max_count = v.count(v[i])
        digit = v[i]

print(digit)