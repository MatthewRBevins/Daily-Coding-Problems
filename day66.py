from random import randint
def toss_biased():
    bias = randint(0,5)
    if bias < 1:
        return 1
    else:
        return 0

def toss_unbiased():
    s = 0
    for i in range(1000):
        s += toss_biased()
    if s % 2 == 0:
        return 0
    else:
        return 1

b = [0,0]
ub = [0,0]
for i in range(1000):
    b[toss_biased()] += 1
for i in range(1000):
    ub[toss_unbiased()] += 1
print(b)
print(ub)
