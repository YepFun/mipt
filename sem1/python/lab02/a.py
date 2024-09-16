def log2(a):
    powered = 1
    power = 0
    while powered < a:
        powered *= 2
        power += 1
    return power

a = int(input())
print(log2(a))