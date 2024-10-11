a = set(input().split())
b = set(input().split())
conjunction = a & b
result = sorted(conjunction, reverse=True)
print(" ".join(result))
