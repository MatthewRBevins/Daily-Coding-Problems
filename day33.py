sequence = [2, 1, 5, 7, 2, 0, 5]
for i,j in enumerate(sequence):
    seq = sequence[0:i+1]
    seq.sort()
    if i % 2 == 0:
        print(seq[i//2])
    else:
        print(seq[(i//2)] + (seq[((i//2)+1)] - seq[(i//2)])/2)
