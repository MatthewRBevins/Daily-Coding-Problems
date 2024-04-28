numeral = "XIV"
indices = ['I','V','X','L','C','D','M']
nums = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}
num = 0
passNext = False
for i in range(len(numeral)):
    if passNext:
        passNext = False
    else:
        if i < len(numeral)-1 and indices.index(numeral[i+1]) > indices.index(numeral[i]):
            num += nums[numeral[i+1]] - nums[numeral[i]]
            passNext = True
        else:
            num += nums[numeral[i]]
print(num)