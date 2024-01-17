# Solution adapted from https://github.com/ruppysuppy/Daily-Coding-Problem-Solutions/blob/master/Solutions/007.py
code = [1,1,1,1]
c = []
for i in range(len(code)+1):
    c.append(0)
c[0] = 1
c[1] = 1
# Each element in c is how many possible codes there are for that many digits
for i in range(2,len(code)+1):
    if code[i-1] != 0:
        c[i]  = c[i-1]
    if code[i-2] == 1 or (code[i-2] == 2 and code[i-1] <= 6):
        c[i] += c[i-2]
print(c[len(code)])
