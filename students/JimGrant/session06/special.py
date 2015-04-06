class Addable(object):
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Addable(self.value + other)

    def __str__(self):
        return str(self.value)

def question01():
    """If I implement __add__ in a class, can I use the + operator
    to add it to integers?
    """
    print("If I implement __add__ in a class, can I use the + operator "
          "to add it to integers?")
    inst = Addable(5)
    print("This should be seven: {}".format(inst + 2))
    print("Answer: Yes. Wow this is cool!")


if __name__ == "__main__":
    question01()
