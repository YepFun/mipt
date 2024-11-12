def is_shifted_lines(a, b):
    if len(a) != len(b):
        return -1
    s = a + a
    position = s.find(b)
    if position != -1:
        return position
    return -1

a = input()
b = input()

print(is_shifted_lines(a, b))