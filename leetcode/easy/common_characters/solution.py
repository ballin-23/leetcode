# given an array of strings find characters common to every string

def common_words(words):
    common_word_dictionary = {}
    for word in words:
        char_set = set()
        for char in word:
            char_set.add(char)
        for char in char_set:
            if char in common_word_dictionary:
                common_word_dictionary[char] += 1
            else:
                common_word_dictionary[char] = 1
    answer = []
    for key in common_word_dictionary.keys():
        if common_word_dictionary[key] == len(words):
            answer.append(key)
    print(answer)
    return answer



words = ["abc", "cba", "da"]
common_words(words)