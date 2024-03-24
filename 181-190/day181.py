import math
def checkPalindrome(s):
    for i in range(0,math.floor(len(s)/2)):
        if s[i] != s[len(s)-i-1]:
            return False
    return True
s = "racecarannakayak"
lastStart = 0
def findListHelper(s):
    if checkPalindrome(s):
        return s
    for i in range(len(s)-1,-1,-1):
        if checkPalindrome(s[0:i]):
            return s[0:i] + "," + findListHelper(s[i:])
def findList(s):
    return findListHelper(s).split(",")
print(findList(s))