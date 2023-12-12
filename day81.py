mapping = dict({"2": ["a","b","c"], "3": ["d","e","f"]})
number = "23"
maps = []

def get_all(number, digit, arr, init):
    for i in mapping[number[digit]]:
        arr.append(init + i)
    return arr

for ii,i in enumerate(number):
    for j in mapping[i]:
        maps.append(get_all())
print(maps)
