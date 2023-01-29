grid = [[0]]

def min_minutes(grid):
    minutes = 0
    rotten_oranges = find_first_orange(grid)
    if len(rotten_oranges) == 0:
        if not check_for_fresh_orange(grid):
            return -1
        return minutes
    more_oranges = []
    for rotten_orange in rotten_oranges:
        more_oranges.extend(find_rotten_oranges(grid,rotten_orange[0],rotten_orange[1]))
    for coord in more_oranges:
        grid = update(grid,coord[0],coord[1],2)
    
    while len(more_oranges) > 0:
        minutes += 1
        found_oranges = []
        for coord in more_oranges:
            found = find_rotten_oranges(grid,coord[0],coord[1])
            found_oranges.extend(found)
        for coord in found_oranges:
            grid = update(grid,coord[0],coord[1],2)
        more_oranges = found_oranges
    
    if check_for_fresh_orange(grid):
        return minutes
    return -1

def check_for_fresh_orange(grid):
    for row in grid:
        if 1 in row:
            return False
    return True

def find_rotten_oranges(grid,i,j):
    # check for rotten oranges
    # len(grid) = y
    # len(grid[0]) = x
    found = []
    y_max = len(grid)
    x_max = len(grid[0])
    if i+1 < y_max:
        if grid[i+1][j] == 1:
            found.append((i+1,j))
    if i - 1 >= 0:
        if grid[i-1][j] == 1:
            found.append((i-1,j))
    if j+1 < x_max:
        if grid[i][j+1] == 1:
            found.append((i,j+1))
    if j-1 >= 0:
        if grid[i][j-1] == 1:
            found.append((i,j-1))
    return found

def find_first_orange(grid):
    rotten_oranges = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 2:
                rotten_oranges.append((i,j))
    return rotten_oranges

def update(grid,i,j,update_value):
    grid[i][j] = update_value
    return grid

print(min_minutes(grid))