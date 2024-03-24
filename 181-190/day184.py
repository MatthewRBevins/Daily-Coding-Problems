nums = [42, 56, 13]
for i in (min(nums),1,-1):
    lcd = True
    for j in nums:
        if j % i != 0:
            lcd = False
    if lcd:
        print(i)
        break