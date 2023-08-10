# given a 2d array of intervals merge the intervals

def merge_intervals(intervals):
    merged = []
    for interval in intervals:
        # print("merged: ", merged, "interval: ", interval)
        if merged == []:
            merged.append(interval)
        else:
            intervals.sort()
            last = len(merged)-1
            # now we check for an overlap
            # check to see if either value falls inside the interval
            print(merged[last][1], " ", interval[1], " ", merged[last][0])
            if merged[last][1] >= interval[0] >= merged[last][0] or merged[last][1] >= interval[1] >= merged[last][1]:
                maxx = max(merged[last][1], interval[1])
                minn = min(merged[last][0], interval[0])
                merged[last] = [minn, maxx]
            elif merged[last][1] >= interval[1] >= merged[last][0] or interval[0] <= merged[last][1] <= interval[1]:
                maxx = max(merged[last][1], interval[1])
                minn = min(merged[last][0], interval[0])
                merged[last] = [minn, maxx]
            else:
                merged.append(interval)
    print(merged)
    return merged
intervals = [  [100, 105],
  [1, 104]]
merge_intervals(intervals)