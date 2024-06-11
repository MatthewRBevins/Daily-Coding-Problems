n = 100
nums = []
for i in range(n):
    nums.append(i+1)
for i in range(int(n/2)):
    ii = i + 1
    j = 0
    j += ii
    if j != 1:
        while ii < n:
            ii += j
            if ii in nums:
                nums.pop(nums.index(ii))
print(nums)