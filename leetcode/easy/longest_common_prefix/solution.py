# strs = ["flower","flow","flight"]
strs = ["dog","racecar","car"]

def longest_common_prefix(words):
    i = 0
    flag = True
    prefix = ""
    potential_char = ""
    if len(words) == 1:
        return words[0]
    while flag:
        if words[0] != "" and i < len(words[0]):
            potential_char = words[0][i]
        for word in words:
            if i >= len(word):
                print("word too short")
                flag = False
                return prefix
            else:
                if word[i] == potential_char:
                    continue
                else:
                    return prefix
        prefix += word[i]
        i+=1
    return prefix

print(longest_common_prefix(strs))