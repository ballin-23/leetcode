def circle_of_numbers(n, fst):
    jump = n // 2
    if jump > fst:
        return fst + jump
    return fst-jump