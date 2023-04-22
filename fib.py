import math

ROOT5 = math.sqrt(5)
PHI = (1 + ROOT5) / 2


def closed_fib(n):
    v = (PHI**n) / ROOT5
    return int(v)


def test():
    fib = {}
    fib[0] = 0
    fib[1] = 1
    for i in range(2, 100):
        fib[i] = fib[i - 1] + fib[i - 2]
        print()
        print(f"fib[{i}]        == {fib[i]}")
        print(f"closed_fib({i}) == {closed_fib(i)}")
        if i > 50 and fib[i] != closed_fib(i):
            print(
                f"""
                ROUNDING ERROR!

                closed_fib({i}) has about {int(math.log(closed_fib(i), 2))} bits"""
            )
            break


test()
