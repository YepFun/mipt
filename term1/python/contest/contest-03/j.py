def argsort(arr, n):
    a = arr
    index = [i for i in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
                index[i], index[j] = index[j], index[i]
    return index
            
arr = list(map(int, input().split()))
index = argsort(arr, len(arr))
print(*index)