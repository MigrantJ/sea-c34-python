def safe_input(prompt):
    try:
        user_input = raw_input(prompt)
    except (EOFError, KeyboardInterrupt):
        user_input = None

    return user_input

if __name__ == "__main__":
    print(safe_input("> "))
