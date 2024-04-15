intervals = [[7, 9], [2, 4], [5, 8]]
def checkOverlaps(intervals):
    for i in range(len(intervals)):
        for j in range(len(intervals)):
            if (intervals[i][0] > intervals[j][0] and intervals[i][0] < intervals[j][1]) or (intervals[j][0] > intervals[i][0] and intervals[j][0] < intervals[i][1]):
                return True
    return False
def delIntervals(ints, dels):
    dels += 1
    for i in range(len(ints)):
        l = ints.copy()
        del l[i]
        if not checkOverlaps(l):
            return dels
        else:
            return delIntervals(l, dels)
    return dels
print(delIntervals(intervals, 0))