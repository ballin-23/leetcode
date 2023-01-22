# O(N) solution => iterate over array twice
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr1 = []
        arr2 = []
        arr3 = []
        negative_index = self.find_first_negative_index(nums)
        if negative_index < 0:
            negative_index = len(nums)
        # iterate backwards
        for i in range(negative_index-1, -1, -1):
            arr1.append(abs(nums[i]))
        for i in range(negative_index, len(nums)):
            arr2.append(nums[i])
        arr3 = self.merge_arr(arr1, arr2)
        for i in range(len(arr3)):
            arr3[i] = arr3[i]*arr3[i]
        print(arr3)
        return arr3
    
    def find_first_negative_index(self,arr):
        for i in range(len(arr)):
            if arr[i] >= 0:
                return i
        return -1
    
    def merge_arr(self,arr1, arr2):
        arr = []
        i = 0
        j = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] > arr2[j]:
                # print("arr2 smaller",arr2[j], j)
                arr.append(arr2[j])
                j += 1
            else:
                # print(arr1[i], i)
                arr.append(arr1[i])
                i += 1
        while i < len(arr1):
            arr.append(arr1[i])
            i+=1
        while j < len(arr2):
            arr.append(arr2[j])
            j +=1
        return arr

# run this

arr = [-4,-1,0,3,10]
x = Solution()
print(x.sortedSquares(arr))