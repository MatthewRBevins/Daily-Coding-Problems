def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
def car(f):
    def c(a,b):
        return a
    return f(c)
def cdr(f):
    def c(a,b):
        return b
    return f(c)
print(cdr(cons(3,4)))
