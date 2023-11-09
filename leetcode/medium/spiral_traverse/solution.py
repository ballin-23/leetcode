# given an m x n matrix traverse it by going right, down, left, up
matrix = [
    [1, 2, 3, 4],
    [10, 11, 12, 5],
    [9, 8, 7, 6]
  ]

def spiralTraverse(array):
    if not isinstance(array[0], list):
        print(array)
        return array
    # Write your code here.
    right_start = 0
    right_end = len(array[0])-1
    down_start = 1
    down_end = len(array)-1
    left_start = len(array[0])-2
    left_end = 0
    up_start = len(array)-2
    up_end = 1
    left_column = 0
    right_column = len(array[0])-1
    top_row = 0
    bottom_row = len(array)-1
    arr = []
    # while (right_start <= right_end or down_start <= down_end or left_start >= left_end or up_end <= up_start):
    while (top_row <= bottom_row):
            print("right start: ", right_start, " right end: ", right_end)
            if right_start <= right_end:
                arr.extend(go_right(array, top_row, right_start, right_end))
            else:
                return arr
            right_start += 1
            right_end -= 1
            top_row += 1
            print("down start: ", down_start, " down end: ", down_end)
            if down_start <= down_end:
                arr.extend(go_down(array, down_start, down_end, right_column))
            else:
                return arr
            down_start += 1
            down_end -= 1
            right_column -= 1
            print("left start: ", left_start, " left end: ", left_end)
            if left_start >= left_end:
                arr.extend(go_left(array, bottom_row, left_start, left_end))
            else:
                return arr
            left_start -= 1
            left_end += 1
            bottom_row -= 1
            print("up start: ", up_start, " up end: ", up_end)
            if up_end <= up_start:
                arr.extend(go_up(array, up_start, up_end, left_column))
            else:
                return arr
            up_start -= 1
            up_end += 1
            left_column += 1
            print("top row: ", top_row)
            print("bottom row: ", bottom_row)
            if bottom_row < top_row:
                print(arr)
                return arr
    print(arr)
    return arr




def go_right(array, current_row, start, stop):
    row = array[current_row]
    arr = []
    for i in range(start, stop+1):
        arr.append(row[i])
    print("going right: ", arr)
    return arr

def go_left(array, current_row, start, stop):
    row = array[current_row]
    arr = []
    for i in range(start, stop-1, -1):
        arr.append(row[i])
    print("going left: ", arr)
    return arr

def get_column(array, current_column):
    column = []
    for i in range(len(array)):
        column.append(array[i][current_column])
    return column

def go_down(array, start, stop, current_column):
    column = get_column(array, current_column)
    arr = []
    for i in range(start, stop+1):
        arr.append(column[i])
    print("going down: ", arr)  
    return arr

def go_up(array, start, stop, current_column):
    column = get_column(array, current_column)
    arr = []
    for i in range(start, stop-1, -1):
        arr.append(column[i])
    print("going up: ", arr)
    return arr


# go_right(matrix, 0, 0, 3)
# go_left(matrix, 3, 2, 0)
# go_down(matrix, 2,3,3)
# go_up(matrix, 3, 0, 0)
print(spiralTraverse(matrix))