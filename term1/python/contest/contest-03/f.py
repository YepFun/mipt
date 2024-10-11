def string_root(s, k):
    is_solution = True
    if len(s) % k != 0:
        result = -1
        is_solution = False
    else:
        block_length = len(s) // k
        result = s[-block_length:]
        #print(result)
        while len(s) > 0:
            if s[-block_length:] == result:
                #print("if:", s[-block_length:])
                s = s[:len(s)-block_length]
            else:
                is_solution = False
                break
    return(is_solution, result)

s = input()
k = int(input())

if k > 0:
    print(s * k)
else:
    is_solution, result = string_root(s, -k)
    if is_solution:
        print(result)
    else:
        print("NO SOLUTION")