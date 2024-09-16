v = []
while True:
    v.append(int(input()))
    if v[len(v)-1] == 0:
        break

max_element = 0
for i in range(len(v)-6):
    if v[i] > max_element:
        max_element = v[i]

print(max_element)
