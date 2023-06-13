# 209. Minimum Size Subarray Sum
# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray
# whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
# input target: number that we need the subarray to be >= to
# input nums:   input array of numbers

# set up test case
target = 11
nums = [1,1,1,1,1,1,1,1]

def minSubArray(target, nums):
    min_arr = float('inf')
    left = 0
    right = 0
    while left <= len(nums):
        # print("left", left, "  len ", len(nums))
        window = []
        total = 0
        for i in range(left, right+1, 1):
            if left==right and left != 0:
                # print("min arr: ", min_arr)
                return min_arr
            if i >= len(nums):
                if min_arr == float('inf'):
                    return 0
                return min_arr
            window.append(nums[i])
            print(left, right, nums[i])
            total += nums[i]
        if total >= target:
            # print("greater than the target",window, " total: ", total)
            # this is where we want to update our left pointer
            while total >= target:
                if min_arr >= len(window):
                    min_arr = len(window)
                    print(min_arr, window, 'here')
                left+=1
                val = window.pop(0)
                total -= val
                # print("removed value",window, " total: ", total,"--", left, right)
        else:
            # print("less than the target", window," total: ", total)
            right+=1
    print(min_arr)

def getSum(arr):
    sum = 0
    for num in arr:
        sum += num
    return sum

minSubArray(target, nums)