n, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

max_diag_value = matrix[0][0]
max_diag_index = 0
for i in range(1, n):
    if matrix[i][i] > max_diag_value:
        max_diag_value = matrix[i][i]
        max_diag_index = i

matrix[k], matrix[max_diag_index] = matrix[max_diag_index], matrix[k]

for row in matrix:
    print(" ".join(map(str, row)))
