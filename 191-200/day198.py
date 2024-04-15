set = [3, 5, 10, 20, 21]
bestSubset = []
bestLen = 0
for i in range(len(set)):
    for j in range(i, len(set)+1):
        subset = set[i:j]
        works = True
        for k in range(len(subset)):
            for l in range(len(subset)):
                if subset[k] % subset[l] != 0 and subset[l] % subset[k] != 0:
                    works = False
        if works and len(subset) > bestLen:
            bestLen = len(subset)
            bestSubset = subset
print(bestSubset)