def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for i in range(n):
            submatrix = []
            for j in range(1, n):
                row = []
                for k in range(n):
                    if k != i:
                        row.append(matrix[j][k])
                submatrix.append(row)
            det += ((-1)**i) * matrix[0][i] * determinant(submatrix)
        return det

n = int(input())
matrix = []

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

print(str(determinant(matrix)))