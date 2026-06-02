A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]


B = [[9, 12, 7],
     [6, 9, 4],
     [13, 8, 1]]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]


i = 0
while (i < len(A)):
    j = 0
    while (j < len(A[0])):
        result[i][j] = A[i][j] + B[i][j]
        j += 1
    i += 1

print("Sum of matrices:")
for row in result:
    print(row)