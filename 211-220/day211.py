string = "abracadabra"
pattern = "abr"
indices = []
for i in range(len(string)):
    if string[i:i+len(pattern)] == pattern:
        indices.append(i)
print(indices)