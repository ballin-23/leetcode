s = ["h","e","l","l","o"]

def reverse(s):
    start = 0
    end = len(s)-1
    while start <= end and end > 0:
        temp = s[start]
        s[start] = s[end]
        s[end] = temp
        end -= 1
        start += 1

reverse(s)