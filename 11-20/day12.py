def find_ways(n):
    c = []
    for i in range(n+1):
        c.append(0)
    c[0] = 1
    c[1] = 1
    for i in range(2,n+1):
        c[i] = c[i-1] + c[i-2]
    return c[n]

print(find_ways(4))
print(find_ways(3))
