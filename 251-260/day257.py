import copy
arr = [3, 7, 5, 6, 9]
for i in range(int(len(arr)/2)):
    t = arr[:i+1] + arr[len(arr)-1-i:]
    tt = copy.deepcopy(t)
    tt.sort()
    if t != tt:
        print("(" + str(i) + ", " + str(len(arr)-1-i) + ")")
