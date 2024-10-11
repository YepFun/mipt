n = int(input())

v = []
for i in range(n):
    row = []
    for j in range(n):
        x = int(input())
        row.append(x)
    v.append(row)

if n < 1:
    print(-1)
else:
    for k in range((n-1)//2 + 1):
        for i in range(k, n-k):
            #print("for1 ", k, i)
            print(v[k][i])
        for i in range(k+1, n-k):
            #print("for2 ", k, i)
            print(v[i][n-k-1])
        for i in range(n-k-2, k-1, -1):
            #print("for3 ", k, i)
            print(v[n-k-1][i])
        for i in range(n-k-2, k, -1):
            #print("for4 ", k, i)
            print(v[i][k])







