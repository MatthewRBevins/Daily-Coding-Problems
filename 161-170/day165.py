arr = [3,4,9,6,1]
n = []
for i in range(len(arr)):
    a = 0
    for j in range(i+1,len(arr)):
        if arr[j] < arr[i]:
            a += 1
    n.append(a)
print(n)