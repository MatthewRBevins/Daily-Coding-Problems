letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
id = 677
# 27 = AA
# 53 = BA
# works from A-ZZ
string = ""
if id > 26:
    string += letters[round(id/26)-1]
string += letters[id % 26 - 1]
print(string)