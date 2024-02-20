# https://github.com/ruppysuppy/Daily-Coding-Problem-Solutions/blob/master/Solutions/140.py

arr = [2, 8, 2, 10]
done = []
ones = []
xor = 0
for i in arr:
    print(xor)
    print(i)
    xor = xor^i
    print(xor)
    #00110
    #01010
    #01100
    print("****")
#01100

#10100
rightmost_set_bit = xor & ~(xor - 1)
print("a" + str(rightmost_set_bit))
num1,num2 = 0,0
print("^&&&&&")
for val in arr:
    if val & rightmost_set_bit:
        num1 = num1 ^ val
    else:
        num2 = num2 ^ val
        print(val)
        print(num2)
        print("***")

print(num1)
print(num2)