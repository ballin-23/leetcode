class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        number_chars = len(word)
        upper_case = 0
        for char in word:
            if char.isupper():
                upper_case += 1
        if number_chars == upper_case:
            return True
        elif upper_case == 1:
            if word[0].isupper():
                return True
        elif upper_case == 0:
            return True
        return False