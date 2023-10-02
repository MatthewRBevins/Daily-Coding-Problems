def autocomplete(arr, query):
    a = []
    for i in arr:
        if i[:len(query)] == query:
            a.append(i)
    return a

arr = ["dog", "deer", "deal"]
query = "de"

print(autocomplete(arr, query))
