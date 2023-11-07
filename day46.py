string = "abc"
def findPalindrome(string):
    bpal = [0,""]
    for index,val in enumerate(string):
        index1 = index
        index2 = index
        pal = 1
        palstr = val
        while index1 > -1 and index2 < len(string) and string[index1] == string[index2]:
            index1 -= 1
            index2 += 1
            if index1 > -1 and index2 < len(string) and string[index1] == string[index2]:
                palstr = string[index1] + palstr + string[index2]
            pal+=2
        pal -= 2
        if pal > bpal[0]:
            bpal = [pal, palstr]
    return bpal
print(findPalindrome(string))
