def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = round((left + right)/2)
        print("the mid value is",mid)

        if arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        elif arr[mid] == target:
            return mid
    return -1


arr = [1,7,9,10,14,36,67]
print(binary_search(arr, 1))