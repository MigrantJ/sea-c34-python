import unittest


class Thingy(object):
    def __init__(self):
        print("How do I use the setup and teardown functionality of unittest?")

    def do_a_thing(self):
        return True

    def dispose(self):
        print("Answer: Like this!")


class ThingyTestCase(unittest.TestCase):
    def setUp(self):
        self.thingy = Thingy()

    def test_the_thingy(self):
        print("Test 1")
        self.assertTrue(self.thingy.do_a_thing())

    def tearDown(self):
        self.thingy.dispose()
        self.thingy = None


def question01():
    """How do I use the setup and teardown functionality of unittest?"""
    unittest.main()


if __name__ == "__main__":
    question01()
