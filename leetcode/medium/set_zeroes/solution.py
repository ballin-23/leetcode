matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]


# check for a zero
# if it contains zero get the indices
# helper function to update the matrix
def remove_zeroes(matrix):
    coordinates_of_zeroes = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                coordinates_of_zeroes.append([i,j])
    matrix = update_matrix(coordinates_of_zeroes, matrix)
    return matrix

def update_matrix(coordinates_of_zeroes, matrix):
    rows_seen = []
    columns_seen = []
    for coordinate in coordinates_of_zeroes:
        if coordinate[0] not in rows_seen:
            rows_seen.append(coordinate[0])
            for i in range(len(matrix[coordinate[0]])):
                matrix[coordinate[0]][i] = 0
        if coordinate[1] not in columns_seen:
            columns_seen.append(coordinate[1])
            for i in range(len(matrix)):
                matrix[i][coordinate[1]] = 0
    


remove_zeroes(matrix)