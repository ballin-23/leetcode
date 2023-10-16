def subarraySort(array):
    # Write your code here.
    print(array)
    first, last = findOutOfPlace(array)
    if first == -1 and last == -1:
        return [-1, -1]
    slicedArray = array[first:last+1]
    print(slicedArray)
    biggest = max(slicedArray)
    smallest = min(slicedArray)
    print("biggest: ", biggest)
    print("smallest: ", smallest)
    # now figure out where the max and min go in the actual array
    start, stop = putBack(biggest, smallest, array)
    return [start, stop]

def putBack(max, min, array):
    print("min : ", min)
    start = -1
    stop = 0
    for i in range(len(array)):
        if array[i] > min and start == -1:
            start = i
            print("start: ", start)
        if max > array[i]:
            stop = i
    if max == min:
        return start, len(array)-1
    print("start is: ", start)
    print("stop is: ", stop)
    return start, stop


def findOutOfPlace(array):
    max = float('-inf')
    first_out_of_place = float('-inf')
    last_out_of_place = float('-inf')
    for i in range(len(array)):
        if array[i] >= max:
            max = array[i]
        else:
            if (first_out_of_place) == float('-inf'):
                first_out_of_place = i-1
            else:
                last_out_of_place = i
    if first_out_of_place == last_out_of_place:
        return -1,-1
    elif last_out_of_place == float('-inf'):
        if first_out_of_place == len(array)-1:
            last_out_of_place = len(array)-1
        else:
            last_out_of_place = first_out_of_place+1
    print("first out of place: ", first_out_of_place)
    print("last out of place: ", last_out_of_place)
    return first_out_of_place, last_out_of_place

arr = [1, 2, 4, 7, 10, 11, 7, 12, 13, 14, 16, 18, 19]
subarraySort(arr)