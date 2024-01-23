acceptable = ["1","2","3","4","5","6","7","8","9","0","e","E","-","."]
numbers = ["1","2","3","4","5","6","7","8","9","0"]
def isNumber(string):
    if " " in string:
        return False
    es = 0
    dots = 0
    hasNum = False
    for i in range(len(string)):
        if string[i] in numbers:
            hasNum = True
        if not string[i] in acceptable:
            return False
        if string[i] == "-" and i != 0:
            return False
        if string[i] == "." and dots == 0:
            dots += 1
        elif string[i] == ".":
            return False
        if string[i] == "e" or string[i] == "E" and es == 0:
            es += 1
            if i == 0 or i == len(string)-1:
                return False
        elif string[i] == "e" or string[i] == "E":
            return False
    return hasNum