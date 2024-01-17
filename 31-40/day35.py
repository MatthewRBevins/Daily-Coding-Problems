letters = ['G','B','R','R','B','R','G']
possible = ['R','G','B']
count = [0,0,0]
used = [0,0,0]
for i in letters:
    count[possible.index(i)]+=1
places = [[], [], []]
used[0] = 0
used[1] = count[0]
used[2] = count[1]+count[0]
orig = used.copy()
for index,val in enumerate(letters):
    if (index >= orig[0] and index < used[0]) or (index >= orig[1] and index < used[1]) or (index >= orig[2] and index < used[2]):
        pass
    else:
        temp = letters[used[possible.index(val)]]
        letters[used[possible.index(val)]] = val
        letters[index] = temp
        used[possible.index(val)] += 1
print(letters)
