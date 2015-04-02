def step1(the_dict):
    """Print the dict by passing it to a string format method."""
    print("{name} is from {city}, and he likes {cake} cake, {fruit} fruit, "
          "{salad} salad, and {pasta} pasta".format(**the_dict))


def step2():
    """Using a list comprehension, build a dictionary of numbers from zero to
    fifteen and the hexadecimal equivalent.
    """
    r = range(0, 16)
    print(dict(zip(r, [hex(i) for i in r])))


def step3():
    """Do the previous entirely with a dict comprehension."""
    print({n: hex(n) for n in range(16)})


if __name__ == "__main__":
    food_prefs = {u"name": u"Jim",
                  u"city": u"Seattle",
                  u"cake": u"chocolate",
                  u"fruit": u"orange",
                  u"salad": u"caesar",
                  u"pasta": u"spaghetti"}
    step1(food_prefs)
    step2()
    step3()