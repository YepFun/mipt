measure = ["monkey", "parrot", "elephant"]
m = [90, 10, 300]

n = int(input())
k = input()

l = -1
for i in range(3):
    if k == measure[i]:
        l = m[i]

result = n // l
if result == 0:
    print(1)
else:
    print(result)