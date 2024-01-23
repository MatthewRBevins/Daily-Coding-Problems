def checkIsPalindrome(string):
    arr = []
    for i in string:
        arr.append(i)
    rArr = list(reversed(arr))
    return arr == rArr
def checkForPalindromes(string, k):
    if k == 0 and checkIsPalindrome(string):
        return True
    elif k == 0:
        return False
    newString = ""
    newString += string
    for i in range(len(string)+1):
        newString = newString[:i-1] + newString[i:]
        if checkForPalindromes(newString, k-1):
            return True
        newString = ""
        newString += string
    return False
string = "waterrfetawx"
print(checkForPalindromes(string, 2))