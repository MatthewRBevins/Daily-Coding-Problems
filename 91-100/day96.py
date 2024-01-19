l = [1,2,3]
for i in l:
    for j in l:
        for k in l:
            if i != j and j != k and i != k:
                print([i,j,k])
