def is_palindrome(a):
    return a == a[::-1]

n = int(input())
a = [int(i) for i in input().split()]

if is_palindrome(a):
    print(0)
else:
    for i in range(n):
        ending = a[i:]
        if is_palindrome(ending):
            print(i)
            print(*a[:i][::-1])
            break


