a = list(map(int, input().split()))
not_zero = [x for x in a if x != 0]
not_zero.sort()
i, k = 0, 0
while i < len(a) and k < len(not_zero):
    if a[i] != 0:
        a[i] = not_zero[k]
        k += 1
    i += 1
print(*a)