def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    current_difference = float('inf')
    pair = []
    for num1 in arrayOne:
        for num2 in arrayTwo:
            if abs(num1-num2) < current_difference:
                current_difference = abs(num1-num2)
                pair = [num1, num2]
    return pair