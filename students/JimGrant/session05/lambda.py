def function_builder(n):
    return [lambda x, e=i: x + e for i in range(n)]

if __name__ == "__main__":
    the_list = function_builder(4)
    for f in the_list:
        print(f(5))
    assert(the_list[0](2) == 2)
    assert(the_list[1](2) == 3)
    print("All tests pass")