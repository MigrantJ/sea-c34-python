class Example(object):
    @staticmethod
    def yesreturner():
        return "Yes"


class SubExample(Example):
    pass


def question01():
    """Do sub-classes inherit static methods?"""
    print("Do sub-classes inherit static methods?")
    print("Answer: {}".format(SubExample.yesreturner()))


if __name__ == "__main__":
    question01()
