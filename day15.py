from random import randint
from typing import Generator


def element_stream() -> Generator[int, None, None]:
    while True:
        # Returns the generator, essentially the next item to be generated
        yield randint(1, 10000)

def random_selector(generator: Generator[int, None, None]) -> int:
    arr = []
    for i in range(10):
        arr.append(next(generator))
    return arr[randint(0,9)]

rand_values = []
for i in range(100):
    rand_values.append(random_selector(element_stream()))
print(rand_values)
