arr = [23,-30,1,2]

def max_arr(array):
    # calculate the max including that index
    maxx = array[0]
    max_so_far = array[0]
    print("max so far : ",max_so_far)
    for i in range(1,len(array),1):
        max_so_far = max(array[i], max_so_far+array[i])
        print("max so far : ",max_so_far)
        maxx = max(maxx, max_so_far)
    print(maxx)
    return maxx

max_arr(arr)