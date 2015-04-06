class Example(object):
    def __init__(self, x):
        self._x = x

    x = property(lambda self: self._x, doc="read only")


def question01():
    """Can I use lambdas for getters / setters in property()?"""
    print("Can I use lambdas for getters / setters in property()?")
    example = Example("Answer: Yes you can")
    print(example.x)


if __name__ == "__main__":
    question01()
