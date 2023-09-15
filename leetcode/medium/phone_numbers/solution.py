# get all possible combinations

phoneNumber = "444"

def phoneNumberMnemonics(phoneNumber):
    # Write your code here.
    mnemonics_so_far = []
    for i in range(0,len(phoneNumber)):
        new_mnemonics = []
        if phoneNumber[i] == "9":
            print("here")
            arr = addCharacters(mnemonics_so_far, "wxyz")
            new_mnemonics.extend(arr)
        elif phoneNumber[i] == "8":
            arr = addCharacters(mnemonics_so_far, "tuv")
            new_mnemonics.extend(arr)
        elif phoneNumber[i] == "7":
            arr = addCharacters(mnemonics_so_far, "pqrs")
            new_mnemonics.extend(arr)
        elif phoneNumber[i] == "6":
            arr = addCharacters(mnemonics_so_far, "mno")
            new_mnemonics.extend(arr)
        elif phoneNumber[i] == "5":
            arr = addCharacters(mnemonics_so_far, "jkl")
            new_mnemonics.extend(arr)
        elif phoneNumber[i] == "4":
            arr = addCharacters(mnemonics_so_far, "ghi")
            new_mnemonics.extend(arr)
        elif phoneNumber[i] == "3":
            arr = addCharacters(mnemonics_so_far, "def")
            new_mnemonics.extend(arr)
        elif phoneNumber[i] == "2":
            arr = addCharacters(mnemonics_so_far, "abc")
            new_mnemonics.extend(arr)
        else:
            arr = addCharacters(mnemonics_so_far, phoneNumber[i])
            new_mnemonics.extend(arr)
        mnemonics_so_far = new_mnemonics
    return mnemonics_so_far
            

def addCharacters(mnemonics_so_far, characterSet):
    arr = []
    if len(mnemonics_so_far) == 0:
        for char in characterSet:
            arr.append(char)
        return arr
    for mnemonic in mnemonics_so_far:
        for char in characterSet:
            arr.append(mnemonic+char)
    print(arr)
    return arr


phoneNumberMnemonics(phoneNumber)