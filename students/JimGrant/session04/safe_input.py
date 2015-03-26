def safe_input(prompt):
    user_input = raw_input(prompt)

    return user_input

if __name__ == "__main__":
    print(safe_input("> "))