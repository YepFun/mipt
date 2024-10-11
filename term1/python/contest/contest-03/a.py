n = int(input())
a = [0] * n
for i in range(n):
    a[i] = int(input())
even = [i for i in a if i % 2 == 0]
for i in range(len(even)):
    for j in range(i + 1, len(even)):
        if even[i] > even[j]:
            even[i], even[j] = even[j], even[i]
k = 0
for i in range(len(a)):
    if a[i] % 2 == 0:
        a[i] = even[k]
        k += 1 
print(*a)