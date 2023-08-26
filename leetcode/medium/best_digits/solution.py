# given a number and numDigits return the largest number after removing numDigits number of digits from the string as a string
number = "462839"
numDigits = 2

def bestDigits(number, numDigits):
    # we need to loop numDigits times
    for i in range(numDigits):
        number = reduceNumber(number)
        print("the reduced greatest number is: ",number)
    return number

def reduceNumber(number):
    greatest = float('-inf')
    for i in range(len(number)):
        current = number[:i] + number[i + 1:]
        if int(current) > greatest:
            greatest = int(current)
    print(greatest)
    return str(greatest)


bestDigits(number, numDigits)