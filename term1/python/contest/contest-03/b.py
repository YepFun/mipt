v_positive = []
v_negative = []

v = [i for i in map(int, input().split())]

for i in range(len(v)):
    if v[i] >= 0:
        v_positive.append(v[i])
    else:
        v_negative.append(v[i])

v_positive.sort()
v_negative.sort()
v_negative = v_negative[::-1]

print(*v_negative, *v_positive)