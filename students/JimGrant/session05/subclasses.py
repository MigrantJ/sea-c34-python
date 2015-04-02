def question01():
    """Is there a way to call parent class methods without referring to the
    parent class by name?
    """

    class Question1(object):
        def __init__(self):
            print("Parent init")

    class SubQuestion1(Question1):
        def __init__(self):
            super(SubQuestion1, self).__init__()
            print("Child init")

    print("Is there a way to call parent class methods without referring to "
          "the parent class by name?")
    question1 = SubQuestion1()
    print("Answer: Yes, with super().")


def question02():
    """Can I make an example of polymorphism?"""
    class Question2(object):
        def speak(self):
            print("I'm the parent")

    class SubQuestion2(Question2):
        def speak(self):
            print("I'm the child")

    print("Can I make an example of polymorphism?")
    a_list = [Question2() if i % 2 == 0 else SubQuestion2() for i in range(5)]
    for c in a_list:
        c.speak()
    print("Answer: Yes")


def question03():
    """Can I get class attributes from a parent class?"""

    class Question3(object):
        x = 1

    class SubQuestion3(Question3):
        def __init__(self):
            print(Question3.x)

    print("Can I get other attributes from a parent class?")
    question3 = SubQuestion3()
    print("Answer: Yes")


def question04():
    """Can a sub-class inherit from multiple parents?"""

    class Question4A(object):
        def __init__(self):
            print("Parent A")

        def bark(self):
            print("Woof")

    class Question4B(object):
        def __init__(self):
            print("Parent B")

        def meow(self):
            print("Meow")

    class SubQuestion4(Question4A, Question4B):
        x = 1

    print("Can a sub-class inherit from multiple parents?")
    question4 = SubQuestion4()
    question4.bark()
    question4.meow()
    print("Answer: Yes, in a limited fashion. "
          "Note that only the first parent's init was called.")


if __name__ == "__main__":
    question01()
    print("")
    question02()
    print("")
    question03()
    print("")
    question04()