seq = []
def deBruijin(C, k, curStr, curK):
    global seq
    if curK == k:
        seq.append(curStr)
        return
    for i in C:
        cc = "" + curStr
        cc += i
        deBruijin(C, k, cc, curK + 1)
deBruijin(["0", "1"], 3, "", 0)
print(seq)