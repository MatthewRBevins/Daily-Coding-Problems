str1 = "SEND"
str2 = "MORE"
answer = "MONEY"
import copy
def textToNum(s, d):
    s = s[::-1]
    p = 1
    n = 0
    for i in s:
        n += (p * d[i])
    return n
uniques = []
for i in (str1 + str2 + answer):
    if not i in uniques:
        uniques.append(i)
def tryAll(letters, numbers):
    d = dict()
    for i in range(len(letters)):
        d[letters[i]] = numbers[i]
    if numbers[len(numbers)-1] != -1:
        if textToNum(str1, d) + textToNum(str2, d) == textToNum(answer, d):
            return d
        else:
            return False
    ii = 0
    for i in range(len(letters)):
        if numbers[i] == -1:
            ii = i
            break
        i += 1
    n = copy.deepcopy(numbers)
    for j in range(10):
        if not j in n:
            n[ii] = j
            t = tryAll(letters, n)
            if t != None and t != False:
                return t
nArr = []
for i in uniques:
    nArr.append(-1)
sol = tryAll(uniques, nArr)
print(sol)
