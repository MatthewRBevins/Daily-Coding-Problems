import math
def get_digit(number, n):
    return (number // 10**n) % 10
def num_digits(n):
    if n == 0:
        return 1
    return int(math.log10(abs(n))) + 1

# Example usage:
number = 121
digit_index = 2  # Get the 3rd digit from the right (indexing starts from 0)
result = get_digit(number, digit_index)

for i in range(num_digits(number)):
    print(get_digit(number, i))
    if get_digit(number, i) != get_digit(number, num_digits(number)-i-1):
        print("NO")
        break
