times = 0
def throw_dice(N, faces, total, curTotal, curN):
    global times
    curN += 1
    if curN == N+1:
        if curTotal == total:
            times += 1
            return True
        return False
    for i in range(1,faces+1):
        c = curTotal + i
        throw_dice(N, faces, total, c, curN)

throw_dice(3, 6, 7, 0, 0)
print(times)