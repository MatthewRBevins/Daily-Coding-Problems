inlist = [[1,3],[5,8],[4,10],[20,25]]
finallist = []
for i in inlist:
    s = False
    for j in finallist:
        if (i[0] < j[0] and i[1] > j[1]):
            j[0] = i[0]
            j[1] = i[1]
            s = True
            break
    print(finallist)
    if not s:
        finallist.append(i)
print(finallist)