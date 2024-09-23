from typing import List
from functools import cache
from timeit import timeit


@cache
def fibonachi(number: int) -> List:
    """FIBONACHI NUMBERS"""
    if number <= 1:
        return 1
    else:
        return fibonachi(number - 1) + fibonachi(number - 2)
    
print(timeit('fibonachi(10)', globals=globals(), number=100_000))

print()

@cache  # For Fast working functions
def fibonachi2(n):
    """ Function for Fibonnaci """
    x, y = 1, 1
    print(x, y, end=" ")
    while n > 1:
        x, y = y, x+y
        print(y, end=" ")
        n -= 1
    return y

# res = fibonachi2(6)
print(timeit('fibonachi2(10)', globals=globals(), number=100_000))