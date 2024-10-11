def operation_to_access(operation):
    if operation == "read":
        return "R"
    if operation == "write":
        return "W"
    if operation == "execute":
        return "X"
n = int(input())
file_access = {}
for _ in range(n):
    line = input().split()
    file_name = line[0]
    access = set(line[1:])
    file_access[file_name] = access
m = int(input())
result = []
for _ in range(m):
    operation, file_name = input().split()
    operation = operation_to_access(operation)
    if (file_name in file_access) and (operation in file_access[file_name]):
        result.append("OK")
    else:
        result.append("Access denied")
print('\n'.join(result))
