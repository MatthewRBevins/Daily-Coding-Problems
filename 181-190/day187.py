rectangles = [
    dict({"top_left": [1, 4], "dimensions": [3,3]}),
    dict({"top_left": [-1, 3], "dimensions": [2,1]}),
    dict({"top_left": [0, 5], "dimensions": [4,3]}),
]
def checkOverlap(r1, r2):
    corners1 = [r1["top_left"][0] + r1["dimensions"][0], r1["top_left"][1] + r1["dimensions"][1]]
    corners2 = [r2["top_left"][0] + r2["dimensions"][0], r2["top_left"][1] + r2["dimensions"][1]]
    if r1["top_left"][0] <= r2["top_left"][0]:
        if r1["top_left"][1] >= r2["top_left"][1]:
            if corners1[0] >= corners2[0]:
                if corners1[1] >= corners2[1]:
                    return True
    return False
y = False
for i in range(len(rectangles)):
    for j in range(len(rectangles)):
        if i != j and checkOverlap(rectangles[i], rectangles[j]):
            print("YES")
            y = True
            break
    if y:
        break
if y == False:
    print("NO")