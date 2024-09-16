answer = ""
n = input()

a = n
while int(a) > 9:
    summ = 0
    for i in range(len(a)):
        summ += int(a[i])
    a = str(summ)
if int(a) == 0 or int(a) == 3 or int(a) == 6 or int(a) == 9:
    answer += "Fizz"

a = n
if int(a[len(a)-1]) == 0 or int(a[len(a)-1]) == 5:
    answer += "Buzz"

a = n
while int(a) > 9:
    e = a[len(a)-1]
    d = a[:(len(a)-1)]
    a = str(int(e) + 3 * int(d))
if int(a) in [0, 7]:
    answer += "Pozz"

if answer == "":
    print("Nedelizz")
else:
    print(answer)