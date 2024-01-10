# simulate doubly linked list because im too lazy to code it
arr = [1,4,3,4]
head = 0
tail = len(arr)-1
for i in range(len(arr)):
    if arr[head] != arr[tail]:
        print("NO")
        break
    head += 1
    tail -= 1