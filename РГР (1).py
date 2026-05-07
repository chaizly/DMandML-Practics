def print_matrix(name, matrix):
    print(f"\n{name}:")
    for row in matrix:
        print(row)

def disjunction(A, B):
    n = len(A)
    m = len(A[0])
    C = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if A[i][j] == 1 or B[i][j] == 1:
                C[i][j] = 1
    return C

def transpose(A):
    n = len(A)
    m = len(A[0])
    B = [[0 for i in range(n)] for j in range(m)]
    for i in range(n):
        for j in range(m):
            B[j][i] = A[i][j]
    return B

def invert(A):
    n = len(A)
    m = len(A[0])
    B = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if A[i][j] == 0:
                B[i][j] = 1
            else:
                B[i][j] = 0
    return B

def subtraction(A, B):
    n = len(A)
    m = len(A[0])
    C = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if A[i][j] == 1 and B[i][j] == 0:
                C[i][j] = 1
    return C

def multiplication(A, B):
    n = len(A)
    m = len(B[0])
    p = len(A[0])
    C = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(p):
                if A[i][k] and B[k][j]:
                    C[i][j] = 1
                    break
    return C

R1 = [[0,1,1,0,0,0,0,0],[0,0,1,1,0,0,0,0]]
R2 = [[1,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0]]

print("R1:", R1)
print("R2:", R2)

print("\n1. Дизъюнкция:")
print_matrix("R1 ∨ R2", disjunction(R1, R2))

print("\n2. Транспонирование:")
print_matrix("R1^T", transpose(R1))

print("\n3. Инвертирование:")
print_matrix("¬R1", invert(R1))

print("\n4. Вычитание:")
print_matrix("R1 - R2", subtraction(R1, R2))

print("\n5. Умножение:")
print_matrix("R1 × R1^T", multiplication(R1, transpose(R1)))