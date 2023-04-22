import math
import recurse


def recurse_fib(n):
    base_cases = {0: 0, 1: 1}
    split = lambda n: (n - 1, n - 2)
    combine = lambda a, b: a + b
    return recurse.spicy(n, base_cases, split, combine)


def test():
    fib = {}
    fib[0] = 0
    fib[1] = 1
    assert recurse_fib(0) == 0
    assert recurse_fib(1) == 1
    for i in range(2, 5001):
        fib[i] = fib[i - 1] + fib[i - 2]
        recurse_val = recurse_fib(i)
        assert recurse_val == fib[i]
        print()
        print(f"       fib({i}) = ")
        print("       ", recurse_val)


test()
