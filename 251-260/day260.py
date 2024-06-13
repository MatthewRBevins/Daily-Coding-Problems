seq = [0, 1, 2, 3, 4]
orders = [0, 1, 1, -1, 1]
for i in range(1,len(seq)):
    if orders[i-1] == 1 and seq[i] > seq[i-1]:
        temp = seq[i]
        seq[i] = seq[i-1]
        seq[i-1] = temp
    if orders[i-1] == -1 and seq[i] < seq[i-1]:
        temp = seq[i]
        seq[i] = seq[i-1]
        seq[i-1] = temp
print(seq)