matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
  ]

# iterate over row in the matrix
# iterate over each value in the row'
# if it is a 1 => we explore that one (let's start with bfs)
# keep track of found rivers in a visited_rivers array 
def riverSizes(matrix):
    river_sizes = []
    rivers = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                print("found a potential river")
                if [i,j] not in rivers:
                    discovered_rivers = bfs_rivers(matrix, i, j)
                    river_sizes.append(len(discovered_rivers))
                    rivers.extend(discovered_rivers)
            else:
                continue
    print("river sizes: ",river_sizes)
# search above, below, right and left
def bfs_rivers(matrix, i, j):
    rivers_explored = []
    rivers_to_explore = [[i, j]]
    while len(rivers_to_explore) > 0:
        new_rivers = []
        for river in rivers_to_explore:
            if river not in rivers_explored:
                rivers_explored.append(river)
                row = river[0]
                position = river[1]
                if row - 1 >= 0:
                    if matrix[row-1][position] == 1:
                        new_rivers.append([row-1, position])
                if row + 1 < len(matrix):
                    if matrix[row+1][position] == 1:
                        new_rivers.append([row+1, position])
                if position -1 >= 0:
                    if matrix[row][position-1] == 1:
                        new_rivers.append([row, position-1])
                if position + 1 < len(matrix[row]):
                    if matrix[row][position+1] == 1:
                        new_rivers.append([row, position+1])
        arr = []
        for river in new_rivers:
            if river not in rivers_explored:
                arr.append(river)
        rivers_to_explore = arr
    print("river positions: ", rivers_explored)
    return rivers_explored



riverSizes(matrix)