def question01():
    """Can I have class attributes and instance attributes
    named the same thing?
    """
    class Question1(object):
        x = 1

        def __init__(self):
            self.x = 2

    print("Can I have class attributes and instance attributes "
          "named the same thing?")
    question1 = Question1()
    print(Question1.x)
    print(question1.x)
    print("Answer: Yes. Note that if the instance attribute didn't exist, "
          "that would've printed 1 both times!")


if __name__ == "__main__":
    question01()