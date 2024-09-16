n = input()
a = n
res = ""
sum = 0
while (int(a)  >  9):
     for i in range(len(a)):
        sum += int(a[i])
     a = str(sum)
     sum = 0
if (int(a) == 9 or int(a) == 3 or int(a) == 6 or int(n)  == 0):
    res += "Fizz"
a = n
if int(a[len(a) - 1]) == 0 or int(a[len(a) - 1]) == 5:
    res += "Buzz"
a = n
s = int(a)
while s > 7:
    if (len(str(s)) == 1):
        break
    a = str(s)
    a = a[0:len(a) - 1]
    if a == '':
        a = 0
    b = a[len(a) - 1]
    s = 3 * int(a) + int(b)
if s == 7 or int(n)  == 0:
    res += "Pozz"
if res == "":
    res = "Nedelizz"
print(res)