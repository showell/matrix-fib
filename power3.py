import recurse


def recurse_power(base, n):
    base_cases = {0: 1, 1: base}

    def split(n):
        return (n // 2, n % 2)

    def combine(a, b):
        return a * a * b

    return recurse.spicy(n, base_cases, split, combine)


def test():
    n = 2000
    p3 = recurse_power(3, n)
    assert p3 == 3**n
    print()
    print(f"    3 ** {n} = {p3}")


test()
