inp = [1,2,3,4,5]
def mapper(val):
    m = 1
    for i in inp:
        m *= i
    m /= val
    return m
out = list(map(mapper, inp))
print(out)
