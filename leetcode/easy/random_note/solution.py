# 383. Ransom Note
# input         two strings ransomNote and magazine
# problem:      construct ransomNote using magazine
# constraints:  each letter in magazine can only be used once

# algorithm
# read magazine into dictionary with letters as keys and the value being their count
# loop through ransomNote and subtract 1 from each value if it exists
# loop all the way through without hitting a zero or key missing => ransomNote => return true

# testing inputs
ransomNote = "aa"
magazine = "aab"

def create_dictionary(word):
    letter_dictionary = {}
    for letter in word:
        if letter in letter_dictionary:
            letter_dictionary[letter] += 1
        else:
            letter_dictionary[letter] = 1
    return letter_dictionary

def create_ransom_note(ransomNote, magazine):
    magazine_letters = create_dictionary(magazine)
    for letter in ransomNote:
        if letter in magazine_letters:
            if magazine_letters[letter] > 0:
                magazine_letters[letter] -= 1
            else:
                return False
        else:
            return False
    return True

print(create_ransom_note(ransomNote, magazine))
