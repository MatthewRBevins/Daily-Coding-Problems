import math
list = [1,2,1,1,3,4,0]
nums = []
freqs = []
for i in list:
    if not i in nums:
        nums.append(i)
        freqs.append(1)
    else:
        freqs[nums.index(i)] += 1
a = []
for i in range(len(freqs)):
    if freqs[i] >= math.floor(len(list)/2):
        a.append(nums[i])
print(max(a))