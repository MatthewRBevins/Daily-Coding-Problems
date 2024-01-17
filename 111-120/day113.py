string = "hello world here"
string = string.split(" ")
string.reverse()
def join(string, delimiter):
    s = ""
    for i in string:
        s += i
        s += delimiter
    return s
print(join(string, " "))