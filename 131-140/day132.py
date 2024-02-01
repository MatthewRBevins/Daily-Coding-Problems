hits = [
    
]
def record(timestamp):
    hits.append(timestamp)
def total():
    return len(hits)
def range(lower, upper):
    count = 0
    for i in hits:
        if i >= lower and i <= upper:
            count += 1
        if i > upper:
            break
    return count
