matrix = [
[1, 0, 0, 0, 0, 0], 
[0, 1, 0, 1, 1, 1], 
[0, 0, 1, 0, 1, 0], 
[1, 1, 0, 0, 1, 0], 
[1, 0, 1, 1, 0, 0], 
[1, 0, 0, 0, 0, 1]
]


# how to solve? find all islands not on a border and then analyze them / modify in place if successful island found
potential_islands = []
def remove_islands(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == 0 or i == len(matrix)-1 or j == 0 or j == len(matrix[0])-1:
                continue
            if matrix[i][j] == 1:
                potential_islands.append((i,j))

    for coord in potential_islands:
        print(coord)
        x = update_matrix(coord, potential_islands, matrix)
    for row in matrix:
        print(row)

def update_matrix(coord, potential_islands, matrix):
    island_group = explore_island(coord, potential_islands, matrix)
    if validate(island_group, matrix):
        for island in island_group:
            matrix[island[0]][island[1]] = 0
    for row in matrix:
        print(row)
    print("xxx")

def validate(islands, matrix):
    print(islands)
    for island in islands:
        if island[0] == len(matrix)-1 or island[0] == 0:
            print("false")
            return False
        if island[1] == len(matrix[0])-1 or island[1] == 0:
            print("false")
            return False
    print("true")
    return True

def explore_island(coord, potential_islands,matrix):
    explored = []
    unexplored = [coord]
    while len(unexplored) > 0:
        found_islands = []
        for island in unexplored:
            if island in explored:
                continue
            else:
                explored.append(island)
                i = island[0]
                j = island[1]
                if i+1 < len(matrix):
                    if matrix[i+1][j] == 1:
                        found_islands.append((i+1,j))
                if i-1 >= 0:
                    if matrix[i-1][j] == 1:
                        found_islands.append((i-1,j))
                if j+1 < len(matrix[0]):
                    if matrix[i][j+1] == 1:
                        found_islands.append((i,j+1))
                if j-1 >= 0:
                    if matrix[i][j-1] == 1:
                        found_islands.append((i,j-1))
        unexplored = set(found_islands)
    return explored



remove_islands(matrix)