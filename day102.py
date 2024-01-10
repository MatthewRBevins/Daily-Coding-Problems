l = [1,2,3,4,5]
n = 9
for i in range(len(l)):
    s = l[i]
    for j in range(i+1,len(l)):
        if s == n:
            print("YESSSS " + str(i) + " TO " + str(j))
        if s > n:
            break
        s += l[j]
        