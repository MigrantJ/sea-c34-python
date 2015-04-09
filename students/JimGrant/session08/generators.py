def intsum():
    i = 0
    j = 1
    while True:
        yield i
        i += j
        j += 1


def doubler():
    i = 1
    while True:
        yield i
        i *= 2


def fib():
    pass


def prime():
    pass