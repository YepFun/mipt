n = int(input())
v = [0] * n
for i in range(n):
    v[i] = int(input())
max_cnt = 0
max_num = v[0]
for i in range(n):
    cnt = v.count(v[i])
    if max_cnt < cnt:
        max_cnt = cnt
        max_num = v[i]
print(max_num)
