def question01():
    """Can I have classes nested inside classes as an attribute?"""
    class Question1(object):
        class NestClass(object):
            x = 1

        def __init__(self):
            self.nestclass = self.NestClass()

    print("Can I have classes nested inside classes as an attribute?")
    question1 = Question1()
    print(question1.nestclass.x)
    print("Answer: Yes")


def question02():
    """What happens if I instantiate a class inside its own __init__()?"""
    class Question2(object):
        def __init__(self):
            self.x = Question2()

    print("What happens if I instantiate a class inside its own __init__()?")
    try:
        question2 = Question2()
    except RuntimeError:
        print("Answer: You will very quickly exceed recursion depth limits.")
    else:
        print("Nothing! Stop worrying so much!")


if __name__ == "__main__":
    question01()
    print("")
    question02()