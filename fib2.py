import recurse
import matrix


def recurse_power(base, n, one):
    base_cases = {0: one, 1: base}

    def split(n):
        return (n // 2, n % 2)

    def combine(a, b):
        return a * a * b

    return recurse.spicy(n, base_cases, split, combine)


def recurse_fib_matrix(n):
    identity = matrix.Matrix22(1, 0, 0, 1)
    m = matrix.Matrix22(0, 1, 1, 1)
    return recurse_power(m, n, identity)


def recurse_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    m = recurse_fib_matrix(n)
    return m.tr


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
