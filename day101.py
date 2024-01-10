inputNum = 68
def checkPrime(num):
    for i in range(2,num-1):
        if num % i == 0:
            return False
    return True
for i in range(inputNum, 0, -1):
    if checkPrime(i) and checkPrime(inputNum-i):
        print(str(i) + " AND " + str(inputNum-i))