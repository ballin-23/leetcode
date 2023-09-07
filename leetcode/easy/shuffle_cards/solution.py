# split the array at n and
nums = [2,5,1,3,4,7]
n = 3

def shuffle(nums, n):
    arr = []
    for i in range(0, int(len(nums)/2)):
        arr.append(nums[i])
        arr.append(nums[i+n])
    print(arr)
    return arr

def shuffle_v2(nums, n):
    arr = [nums[i // 2] if i % 2 == 0 else nums[n + i // 2] for i in range(len(nums))]
    return arr

shuffle(nums,n)