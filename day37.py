# Solution from https://github.com/ruppysuppy/Daily-Coding-Problem-Solutions/blob/master/Solutions/037.py

initSet = [1,2,3]
# []
# [1],[2],[3],[4],[5]
# [1,2],[1,3],[1,4],[1,5],[2,3],[2,4],[2,5],[3,4],[3,5],[4,5]
# [1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5],[2,3,4],[2,3,5],[2,4,5],[3,4,5]
#, [1,2,3,4],[1,2,3,5],[1,2,4,5],[1,3,4,5],[2,3,4,5]
# first loop - number of items to keep out
power_set = [[]]
# generating the power set
for elem in initSet:
    # generating the new sets
    additional_sets = []
    print(power_set)
    for subset in power_set:
        subset_copy = [subset_elem for subset_elem in subset]
        subset_copy.append(elem)
        additional_sets.append(subset_copy)
    # adding the new sets to the power set
    power_set.extend(additional_sets)
print(power_set)
