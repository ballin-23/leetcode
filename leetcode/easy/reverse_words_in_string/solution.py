class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        answer = ""
        words = s.split()
        for word in words:
            for i in range(len(word)-1,-1,-1):
                answer+=word[i]
            answer += " "
        return answer.strip()