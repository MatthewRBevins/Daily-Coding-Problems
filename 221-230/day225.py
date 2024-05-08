N = 5
k = 2
prisoners = []
for i in range(1, N+1):
    prisoners.append(i)
c = (k-1)
while len(prisoners) > 1:
    del prisoners[c]
    c += 1
    if c == len(prisoners):
        c = 0
    if c == len(prisoners)+1:
        c = 1
print(prisoners[0])