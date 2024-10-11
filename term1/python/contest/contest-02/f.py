n = int(input())
k = 0
max_k = 0
for i in range(n):
    x = int(input())
    if x == 1:
        k += 1
    elif x == 0:
        max_k = max(k, max_k)
        k = 0
max_k = max(k, max_k)

print(max_k)
