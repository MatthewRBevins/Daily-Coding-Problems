mapping = dict({"2": ["a","b","c"], "3": ["d","e","f"]})

def findMap(cur, num, digit):
    arr = []
    for i in mapping[str(num)[digit]]:
        #print(cur + str(i))
        if digit < len(str(num))-1:
            a = findMap(cur + str(i), num, digit+1)
            for j in a:
                arr.append(j)
        else:
            arr.append(cur+str(i))
    return arr

num = 23
print(findMap("", 23, 0))