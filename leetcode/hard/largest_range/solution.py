arr = [-7, -7, -7, -7, 8, -8, 0, 9, 19, -1, -3, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, -6, 8, 7, 6, 15, 12, 12, -5, 2, 1, 6, 13, 14, -4, -2]

def largestRange(array):
    # Write your code here.
    if len(array) > 1:
        ranges = create_ranges(array)
        max_range = get_largest_range(ranges)
        boundaries = get_boundaries(max_range)
        return boundaries
    else:
        boundaries = get_boundaries(array)
        return boundaries
        
def get_boundaries(range):
    last = len(range)-1
    return [range[0], range[last]]

def get_largest_range(ranges):
    max_index =  0
    max_range = float('-inf')
    for i in range(len(ranges)):
        if get_difference(ranges[i]) >= max_range:
            max_index = i
            max_range = get_difference(ranges[i])
    return ranges[max_index]      

def get_difference(array):  
    last = len(array)-1
    difference = array[last] - array[0]
    print(difference)
    return difference

def create_ranges(array):
    array.sort()
    print(array)
    ranges = []
    current_range = []
    for num in array:
        if current_range == []:
            current_range.append(num)
        else:
            if current_range[len(current_range)-1]+1 == num or current_range[len(current_range)-1] == num:
                current_range.append(num)
            else:
                ranges.append(current_range)
                current_range = [num]
    if current_range != []:
        ranges.append(current_range)
    return ranges


largest_range(arr)