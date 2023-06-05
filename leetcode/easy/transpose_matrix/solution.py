matrix = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

def init_empty_matrix(matrix):
    new_matrix = []
    for i in range(len(matrix[0])):
        arr = []
        for j in range(len(matrix)):
            arr.append(0)
        new_matrix.append(arr)
    return new_matrix

def transpose(matrix):
    # create matrix
    new_matrix = init_empty_matrix(matrix)
    # transpose given matrix into new matrix
    # we want to flip the row
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix


    

print(transpose(matrix=matrix))
