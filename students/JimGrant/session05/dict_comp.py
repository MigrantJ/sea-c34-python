def step1(the_dict):
    """Print the dict by passing it to a string format method."""
    print("{name} is from {city}, and he likes {cake} cake, {fruit} fruit, "
          "{salad} salad, and {pasta} pasta".format(**the_dict))


if __name__ == "__main__":
    food_prefs = {u"name": u"Jim",
                  u"city": u"Seattle",
                  u"cake": u"chocolate",
                  u"fruit": u"orange",
                  u"salad": u"caesar",
                  u"pasta": u"spaghetti"}
    step1(food_prefs)