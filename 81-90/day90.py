from random import randint
n = 5
l = [2,3]
ll = []
for i in range(n):
    if not i in l:
        ll.append(i)
for i in range(1000):
    print(ll[randint(0,len(ll)-1)])