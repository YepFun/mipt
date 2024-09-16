import math

n = int(input())

v = [True for i in range(n+1)]
v[0] = False
v[1] = False

for i in range(2, int(math.sqrt(n))+1):
    if v[i]:
        j = i + i
        while j <= n:
            v[j] = False
            j += i

result = []

for i in range(n+1):
    if v[i]:
        result.append(str(i))
result = " ".join(result)

print(result)
