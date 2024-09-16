def grades_summ(grades):
    summ = 0
    for j in range(len(grades)):
        summ += grades[j]
    return summ

n = int(input())

grades = []
for i in range(n):
    grades.append([])

while True:
    line = input().strip()
    if line == "#":
        break
    id, value = map(int, line.split())
    grades[id].append(value)

# print(grades)

# condition sum
grades.sort(key=lambda x: grades_summ(x), reverse=True)

for i in range(len(grades)):
    grades[i].sort()
    grades[i] = grades[i][::-1]
    # print(*grades[i])

flat_list = [str(i) for row in grades for i in row]
result = ' '.join(flat_list)

print(result)
