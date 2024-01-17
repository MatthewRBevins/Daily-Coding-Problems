from random import randint
def rand5():
    return randint(1,5)
def rand7():
    a = 0
    for i in range(10000):
        a += rand5()
    return a % 7 + 1

for i in range(10):
    distr = [0,0,0,0,0,0,0]
    for j in range(1000):
        distr[rand7()-1] += 1
    print(distr)


