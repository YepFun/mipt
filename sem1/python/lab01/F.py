a = []
x = int(input())
while x != 0:
    a.append(x)
    x = int(input())

max_el = 0
for i in range(len(a)):
    el = a[i]
    if max_el < el and el % 2 == 0:
        max_el = el
print(max_el)