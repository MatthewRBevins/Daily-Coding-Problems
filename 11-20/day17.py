def findLargestPath(string):
    formatted = string.replace("\n","").split("\t")
    level = 1
    formatted[0] = [formatted[0], 0]
    for ii,i in enumerate(formatted):
        if ii != 0:
            if i == '':
                level += 1
            else:
                formatted[ii] = [i, level]
                level = 1
    bestC = [0,None]
    for ii,i in enumerate(formatted):
        if len(i) == 2 and '.' in i[0]:
            c = len(i[0])
            path = i[0]
            n = i[1]
            j = ii
            while n > 0:
                j -= 1
                if len(formatted[j]) == 2:
                    if formatted[j][1] == (n-1):
                        c += len(formatted[j][0]) + 1
                        path = formatted[j][0] + "/" + path
                        n -= 1
            if c > bestC[0]:
                bestC = [c, path]
    return bestC[0]
                
string = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
print(findLargestPath(string))
