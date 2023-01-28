nums = [1,1,1,1,3]
target = 2

def search(nums, target):
    high = len(nums) -1
    low = 0
    middle = (high+low)//2 
    while low <= high:
        middle = (high+low)//2   
        if nums[middle] > target:
            high = middle -1
        elif nums[middle] < target:
            low = middle + 1
        else:
            print("index is:",middle)
            return middle
    print(middle)
    if nums[len(nums)-1] < target:
        return len(nums)
    if nums[middle] < target:
        return middle + 1
    return middle
print(search(nums, target))
            