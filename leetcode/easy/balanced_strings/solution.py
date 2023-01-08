input = "RLRRRLLRLL"

count = 0
char_dictionary = {"R":0, "L":0}

for char in input:
    if char == "R":
        if char_dictionary["L"] == 0:
            char_dictionary["R"] += 1
        else:
            char_dictionary["R"] += 1
            if char_dictionary["R"] == char_dictionary["L"]:
                count += 1
                char_dictionary["R"] = 0
                char_dictionary["L"] = 0
    else:
        if char_dictionary["R"] == 0:
            char_dictionary["L"] += 1
        else:
            char_dictionary["L"] += 1
            if char_dictionary["R"] == char_dictionary["L"]:
                count += 1
                char_dictionary["R"] = 0
                char_dictionary["L"] = 0

print(count)