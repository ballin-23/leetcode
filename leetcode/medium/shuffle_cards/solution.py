# implement a shuffle algorithm
import random
arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]


def shuffle(arr):
    for i in range(len(arr)-1, 0, -1):
        # here we want to swap arr[i] with a random index
        swap_index = random.randint(0,i)
        temp = arr[i]
        arr[i] = arr[swap_index]
        arr[swap_index] = temp
    print(arr)
shuffle(arr)