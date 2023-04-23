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
    fibs = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    for i in range(len(fibs)):
        assert recurse_fib(i) == fibs[i]
    print(recurse_fib(20000))
