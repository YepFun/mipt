n = int(input())
m = int(input())
k = int(input())
x = int(input())

if m < n:
    print("NO")
else:
    if k < m:
        if k + x >= m:
            print("NO")
        else:
            print("YES")
    else:
        print("YES")