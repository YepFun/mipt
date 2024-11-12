def visible():
    max_height = 0
    cnt = 0
    while True:
        height = int(input())
        if height == 0:
            break
        if height > max_height:
            cnt += 1
            max_height = height
    return cnt

print(visible())
