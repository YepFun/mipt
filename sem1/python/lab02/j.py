"""
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
"""

v = [-1] * 6

current_number = int(input())
i = 0
max_element = -1

while current_number != 0:
    v[i] = current_number
    max_element = max(max_element, v[(i - 5) % 6])
    i = (i + 1) % 6
    current_number = int(input())
print(max_element)

