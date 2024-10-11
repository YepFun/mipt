def merge_lists(a, b):
    to = [0] * (len(a) + len(b))
    i = 0
    j = 0
    while i < len(a) or j < len(b): 
        if j == len(b) or (i < len(a) and a[i] < b[j]):
            to[i + j] = a[i]
            i += 1
        else:
            to[i + j] = b[j]
            j += 1
    return to

a = list(map(int, input().split()))
b = list(map(int, input().split()))
to = merge_lists(a, b)
print(*to)