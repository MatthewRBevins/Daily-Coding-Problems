def intersections(arr1, arr2):
    segments = list(zip(arr1, arr2))
    count = 0
    for i in range(len(segments)):
        p1start, p1end = segments[i]
        for p2start, p2end in segments[:i]:
            if (p1start < p2start and p1end > p2end) or (p1start > p2start and p1end < p2end):
                count += 1
    return count
print(intersections([1,4,5], [4,2,3]))