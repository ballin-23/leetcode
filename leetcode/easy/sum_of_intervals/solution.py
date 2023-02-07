arr = [
    [97, 98], [97, 99],[-98, 96]
]

def intervals(intervals):
    arr = []
    intervals.sort()
    for interval in intervals:
        arr = add_to_intervals(interval, arr)
        # print(arr)
    sum = 0
    merge = []
    for i in range(len(arr)):
        if i+1 < len(arr):
            if arr[i][1] >= arr[i+1][0]:
                merge.append(i)
    
    i = 0
    while i <= len(arr)-1:
        if i in merge:
            sum += arr[i+1][1] - arr[i][0]
            i += 2
        else:
            sum += arr[i][1] - arr[i][0]
            i+=1
    print(sum)
    return sum
def add_to_intervals(interval, list_of_intervals):
    # if the highest or lowest part of range fits in another range update the range accordingly else add to the intervals
    low = interval[0]
    high = interval[1]

    if len(list_of_intervals) == 0:
        list_of_intervals.append(interval)
        return list_of_intervals

    for entry in list_of_intervals:
        # this is the case where the entry is contained in the interval
        if low <= entry[0] and entry[1] <= high:
            entry[0] = low
            entry[1] = high
            return list_of_intervals
        elif entry[0] <= low <= entry[1]:
            if entry[1] <= high:
                entry[1] = high
            return list_of_intervals
        elif entry[0] <= high <= entry[1]:
            if low <= entry[0]:
                entry[0] = low
            return list_of_intervals
    list_of_intervals.append(interval)


    return list_of_intervals


intervals(arr)