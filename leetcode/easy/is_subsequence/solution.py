input = [5, 1, 22, 25, 6, -1, 8, 10],
seq = [1, 6, -1, -1]

def is_subsequence(arr, seq):
    count = 0
    for num in arr:
        if arr == seq[count]:
            count += 1
        if count == len(seq)-1:
            print("true")
            return True
    print("false")
    return False

is_subsequence(input,seq)