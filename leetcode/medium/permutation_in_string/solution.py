s1 = "ab"
s2 = "ab"
# s2 = "ab"

def is_permutation(s1, s2):
    h1 = {}
    h2 = {}
    for char in s1:
        insert_into_hashmap(h1, char)

    oldest = 0
    for i in range(len(s2)):
        # print("h2",h2)
        # print("h1",h1)
        if i < len(s1):
            insert_into_hashmap(h2, s2[i])
        else:
            if compare_hashmap(h1,h2):
                # print("here")
                return True
            else:
                # print("here")
                h2[s2[oldest]] -= 1
                insert_into_hashmap(h2,s2[i])
                oldest += 1
    return compare_hashmap(h1,h2)



def insert_into_hashmap(h, item):
    if item not in h.keys():
        h.update({item: 1})
    else:
        h[item] += 1

def compare_hashmap(h1,h2):
    for key in h1.keys():
        if key in h2.keys():
            if h1[key] == h2[key]:
                continue
            else:
                return False
        else:
            return False
    return True

print(is_permutation(s1,s2))
