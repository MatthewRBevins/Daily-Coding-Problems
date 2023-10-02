import time

def job_scheduler(f, n):
    time.sleep(n/1000)
    f()

def print_hi():
    print("hi")

job_scheduler(print_hi, 2000)
