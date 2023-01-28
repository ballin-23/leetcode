image = [[0,0,0],[0,0,0]]

def flood(image, sr, sc, color):
    found = []
    # m = rows n = columns
    m = len(image)
    n = len(image[0])
    starter = image[sr][sc]
    image[sr][sc] = color
    found = checkFourSides(image, sr, sc, color, m, n, starter)
    for coord in found:
        image = update(coord[0], coord[1], image, color)
    while len(found) > 0:
        more_found = []
        for coord in found:
            recent = checkFourSides(image,coord[0], coord[1], color, m, n, starter)
            for xy in recent:
                image = update(xy[0],xy[1], image, color)
                more_found.append(xy)
        found = more_found
    return image

def checkFourSides(image, sr, sc, color,m,n, starter):
    # assume sr is row (y), sc is column (x)
    # if it's [1,1] we want to check one above which is [0,1] one down which is [2,1] one left which is [1,0] and one right which is [1,2]
    # check one row up
    print("here")
    arr = []
    if sr-1 >= 0:
        if image[sr-1][sc] == starter:
            arr.append((sr-1,sc))
    if sr+1 < m:
        if image[sr+1][sc] == starter:
            arr.append((sr+1,sc))
    
    if sc-1 >= 0:
        if image[sr][sc-1] == starter:
            arr.append((sr,sc-1))

    if sc+1 < n:
        if image[sr][sc+1] == starter:
            arr.append((sr,sc+1))
    return arr

def update(x,y, image, color):
    image[x][y] = color
    return image

flood(image,0,0,0)