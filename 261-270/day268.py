num = 2
# Uses a binary number with a "1" in every power of 4
print((num & -num) & 0x55555554)