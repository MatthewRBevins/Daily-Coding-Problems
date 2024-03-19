parentDict = {
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}
def flatten(dicti, string, level):
    arr = []
    thisDict = dict({})
    origString = string
    for i in dicti.keys():
        string += i
        if str(type(dicti[i])) == "<class 'dict'>":
            for j in flatten(dicti[i], string + ".", 1):
                arr.append(j)
        else:
            arr.append([string,dicti[i]])
        string = origString
    if level == 0:
        for i in arr:
            thisDict[i[0]] = i[1]
        return thisDict
    return arr
print(flatten(parentDict, "", 0))