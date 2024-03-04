num = "11110000111100001111000011110000"
reversedNum = ""
for i in num:
    if i == "1":
        reversedNum += "0"
    else:
        reversedNum += "1"
print(reversedNum)