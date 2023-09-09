buildings = [3, 5, 4, 4, 3, 1, 3, 2]
direction = "west"

def sunsetViews(buildings, direction):
    if direction == "EAST":
        return sunsetHelper(buildings, len(buildings)-1, -1, -1)
    return sunsetHelper(buildings, 0, len(buildings), 1)

def sunsetHelper(buildings, start, stop, step):
    indices = []
    current_tallest = float('-inf')
    for i in range(start, stop, step):
        if buildings[i] > current_tallest:
            indices.append(i)
            current_tallest = buildings[i]
    indices.sort()
    return indices

sunsetViews(buildings, direction)