# given a 2d array of intervals merge the intervals
# intervals = [[100, 105],[1, 104]]

def merge_intervals(intervals):
    merged = []
    for interval in intervals:
        if merged == []:
            merged.append(interval)
        else:
            intervals.sort()
            print(intervals)
            last = len(merged)-1
            if merged[last][1] >= interval[0]:
                merged[last] = [min(merged[last][0], interval[0]),max(merged[last][1], interval[1])]
            else:
                merged.append(interval)
    print(merged)
    return merged

intervals = [
    [20, 21],
    [22, 23],
    [0, 1],
    [3, 4],
    [23, 24],
    [25, 27],
    [5, 6],
    [7, 19]
  ]
merge_intervals(intervals)