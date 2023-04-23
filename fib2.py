import matrix


def power(base, n):
    assert n >= 1
    if n == 1:
        return base

    a = power(base, n // 2)
    result = a * a

    if n % 2:
        result *= base

    return result


def recurse_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    q_matrix = matrix.Matrix22(
        (0, 1),
        (1, 1),
    )
    m = power(q_matrix, n)
    return m.tr


if __name__ == "__main__":

    def simple_fib(n):
        if n == 0:
            return 0
        a, b = 0, 1
        for i in range(n - 1):
            a, b = (b, a + b)
        return b

    fibs = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    for i in range(len(fibs)):
        assert simple_fib(i) == fibs[i]
        assert recurse_fib(i) == fibs[i]
    assert simple_fib(20000) == recurse_fib(20000)
    print(recurse_fib(20000))
