'''
def make_functions():
    flist = []

    for i in [1, 2, 3]:
        def print_i():
            print(i)
        flist.append(print_i)

    return flist

functions = make_functions()
for f in functions:
    f()
'''

def make_functions():
    flist = []

    for i in [1, 2, 3]:
        def print_i():
            return i
        flist.append(print_i())

    return flist

functions = make_functions()
for f in functions:
    print(f)