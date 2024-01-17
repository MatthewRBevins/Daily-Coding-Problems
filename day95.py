l = [1,3,2]
def nextDesc(l, i):
    c = l[i]
    if i == len(l)-1:
        return True
    for i in range(i+1,len(l)):
        if c < l[i]:
            return False
        c = l[i]
    return True
def findNextUp(l, v):
    smallDiff = sum(l)
    s = None
    for i in range(len(l)):
        if l[i] - v > 0 and l[i] < smallDiff:
            smallDiff = l[i]
            s = i
    return s
# go through array
# check whether next elements are descending
# if so, replace previous element with next element up
# all other elements should be sorted
# condition for if 3,2,1
for i in range(1,len(l)):
    if nextDesc(l, i):
        nu = findNextUp(l,l[i-1])
        temp = l[i-1]
        l[i-1] = l[nu]
        print(l[:nu-1])
        print(temp)
        print(l[nu:])
        break