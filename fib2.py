import recurse
import matrix


def recurse_power(base, n, one):
    base_cases = {0: one, 1: base}

    def split(n):
        return (n // 2, n % 2)

    def combine(a, b):
        return a * a * b

    return recurse.spicy(n, base_cases, split, combine)


def recurse_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    identity = matrix.Matrix22(
        (1, 0),
        (0, 1),
    )
    q_matrix = matrix.Matrix22(
        (0, 1),
        (1, 1),
    )
    m = recurse_power(q_matrix, n, identity)
    return m.tr


if __name__ == "__main__":
    fibs = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    for i in range(len(fibs)):
        assert recurse_fib(i) == fibs[i]
    print(recurse_fib(20000))
