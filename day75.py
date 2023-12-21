arr = [0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]
options = []

def findMaxIndex(arr):
    maxi = -1
    maxindex = -1
    for i in range(len(arr)):
        if arr[i] > maxi:
            maxi = arr[i]
            maxindex = i
    return maxindex
curr = -1
greatestseq = []
while True:
    options = []
    for ii,i in enumerate(arr):
        c = 0
        for j in range(ii,len(arr)):
            if arr[j] > i and i > curr:
                c+=1
        options.append(c)
    if max(options) == 0:
        if arr[len(arr)-1] > curr:
            greatestseq.append(arr[len(arr)-1])
            break
    curr = arr[findMaxIndex(options)]
    arr = arr[findMaxIndex(options)+1:]
    greatestseq.append(curr)
print(greatestseq)