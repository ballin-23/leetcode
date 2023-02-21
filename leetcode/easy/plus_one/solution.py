class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        last_digit = digits[len(digits)-1]
        if last_digit == 9:
            # handle that case here
            print("here")
            if len(digits) == 1:
                return [1,0]
            i = len(digits)-1
            while digits[i] == 9:
                digits[i] = 0
                i -= 1
            print(i, digits[i])
            if i == -1 and digits[0] == 0:
                arr = [1]
                new_arr = [0]*len(digits)
                arr.extend(new_arr)
                print(arr)
                return arr
            digits[i] = digits[i]+1
        else:
            digits[len(digits)-1] = digits[len(digits)-1] + 1 
        return digits