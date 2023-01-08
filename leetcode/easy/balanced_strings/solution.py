def balance_string(s):
    count = 0
    char_dictionary = {"R":0, "L":0}

    for char in s:
        if char == "R":
            char_dictionary["R"] += 1
        else:
            char_dictionary["L"] += 1
        if char_dictionary["R"] == char_dictionary["L"]:
            count += 1
    print(count)
    return count
input = "RLRRRLLRLL"
balance_string(input)
