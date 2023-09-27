# dynamic programming solution
# iterate over all positions in the matrix
# each position is the sum of the number of paths to the left and above
# fill out the matrix this way
# the top row and left most column are all equal to one since there is only one path to get there

def numberOfWaysToTraverseGraph(width, height):
    # Write your code here.
    row = [0]*width
    arr = []
    for i in range(height):
        arr.append(row[:])
    # let's go across the top here
    for i in range(len(arr[0])):
        arr[0][i] = 1
    for i in range(len(arr)):
        arr[i][0] = 1
    print(arr)
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print("coordinate: ", i,j, "  ", arr[i][j])
            if arr[i][j] == 0:
                arr[i][j] = add_values(arr, i, j)
    print(arr)
    print(arr[height-1][width-1])
    return arr[height-1][width-1]

def add_values(arr, i, j):
    left = arr[i][j-1]
    top = arr[i-1][j]
    return left + top
numberOfWaysToTraverseGraph(4,3)
