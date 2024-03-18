from random import randint
costs1 = []
costs2 = []
for i in range(10000):
    last = 0
    cur = 0
    cost = 0
    while True:
        cost += 1
        cur = randint(1,6)
        if last == 5 and last == cur:
            break
        last = cur
    costs1.append(cost)
for i in range(10000):
    last = 0
    cur = 0
    cost = 0
    while True:
        cost += 1
        cur = randint(1,6)
        if last == 5 and cur == 6:
            break
        last = cur
    costs2.append(cost)
print(sum(costs1)/1000)
print(sum(costs2)/1000)