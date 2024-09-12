n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
b = []
for i in range(n):
    b.append(a.count(a[i]))
m = max(b)
for i in range(n):
    if b[i] == m:
        print(a[i])
        break
