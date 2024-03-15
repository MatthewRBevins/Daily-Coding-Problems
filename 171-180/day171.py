entries = [
    {"timestamp": 1526579928, "count": 3, "type": "enter"},
    {"timestamp": 1526580382, "count": 2, "type": "enter"}
]
# assume timestamps are sorted
peopleIn = 0
eras = []
for i in entries:
    if i["type"] == "enter":
        peopleIn += i["count"]
    else:
        peopleIn -= i["count"]
    eras.append([i["timestamp"], peopleIn])
mostPeople = 0
bestEra = []
for i in range(len(eras)):
    if eras[i][1] > mostPeople:
        if i < len(eras)-1:
            mostPeople = eras[i][1]
            bestEra = [eras[i][0], eras[i+1][0]]
        else:
            bestEra = [eras[i][0], "present"]
print(bestEra)