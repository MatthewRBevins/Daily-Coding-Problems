rectangles = [
    dict({"top_left": [1, 4], "dimensions": [3,3]}),
    dict({"top_left": [0, 5], "dimensions": [4,3]}),
]
r1 = rectangles[0]
r2 = rectangles[1]
corners1 = [r1["top_left"][0] + r1["dimensions"][0], r1["top_left"][1] + r1["dimensions"][1]]
corners2 = [r2["top_left"][0] + r2["dimensions"][0], r2["top_left"][1] + r2["dimensions"][1]]
overlap = 0
for i in range(r2["top_left"][0], corners2[0]):
    for j in range(r2["top_left"][1], corners2[1]):
        if i > r1["top_left"][0] and i < corners1[0] and j >= r1["top_left"][1] and j <= corners1[1]:
            overlap += 1
print(overlap)