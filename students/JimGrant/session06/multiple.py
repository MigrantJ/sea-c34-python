class Animal(object):
    def __init__(self, name):
        self.name = name

    def announce(self):
        print("I am a {}".format(self.name))


class FlyMixin(object):
    def fly(self):
        print("I'm flying")


class SwimMixin(object):
    def swim(self):
        print("I'm swimming")


class FlyingFish(SwimMixin, FlyMixin, Animal):
    def __init__(self):
        Animal.__init__(self, "flying fish")


def question01():
    """What would an example of mixins look like?"""
    flyingfish = FlyingFish()
    flyingfish.announce()
    flyingfish.swim()
    flyingfish.fly()


if __name__ == "__main__":
    question01()
