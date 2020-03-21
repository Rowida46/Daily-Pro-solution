transpose of a matrix 
def transpose(mat):
    n , m = len(mat) , len(mat[0])
    T = [[0 for i in range(n)]for j in range(m)]
    for i in range(m) :
        for j in range(n):
            T[i][j] = mat[j][i]
    return T
mat = [
    [1, 2, 3],
    [4, 5, 6],
]

print(transpose(mat))
