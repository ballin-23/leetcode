# implement bubble sort

def bubbleSort(array):
    for i in range(len(array)):
        # subtract the 1 since arrays are 0 indexed lol
        for j in range(0,len(array)-i-1, 1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array

arr = [1,6,4,2,6,10,2,4,15]
sorted_arr = bubbleSort(arr)
print(sorted_arr)