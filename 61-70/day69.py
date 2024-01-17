l = [-10,-10,5,2]
l.sort()
smallest = l[:2]
largest = l[len(l)-3:]
print(smallest)
print(largest)

print(max(largest[0]*largest[1]*largest[2], largest[2]*smallest[0]*smallest[1]))