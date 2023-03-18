def fib(n, nums):
    result = 0
    if nums[n] != None:
        print("hit")
        return nums[n]
    # base case
    if n == 1 or n == 2:
        nums[n] = 1
        result =  1
    else:
        result = fib(n-1, nums) + fib(n-2, nums)
        nums[n] = result
    return result

arr = [None] * 8
x = fib(7, arr)
print(x)