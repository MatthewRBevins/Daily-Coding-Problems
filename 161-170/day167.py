import math
def checkPalindrome(string):
    for i in range(math.floor(len(string)/2)):
        if string[i] != string[len(string)-i-1]:
            return False
    return True
list = ["code", "edoc", "da", "d"]
matches = []
for i in range(len(list)):
    for j in range(len(list)):
        if i != j and checkPalindrome(list[i] + list[j]):
            matches.append([i,j])
print(matches)