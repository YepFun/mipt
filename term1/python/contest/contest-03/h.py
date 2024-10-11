element = int(input())
v = []
total_max = element
while element != 0:
    v.append(element)
    total_max = max(element, total_max)
    element = int(input())
print(v.count(total_max))
