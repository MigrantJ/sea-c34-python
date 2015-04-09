def intsum():
    i, j = 0, 1
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
    i, j = 0, 1
    while True:
        yield j
        i, j = j, i + j


def prime():
    i = 2
    while True:
        if i < 4 or i % 2 != 0 and i % 3 != 0:
            yield i
        i += 1