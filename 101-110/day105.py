import time
def debouncedF(f, N):
    time.sleep(N/1000)
    return f()

def f():
    print("hello")
N = 500
debouncedF(f, N)