from os import system


class DonorList:
    """contains the list of donors and their donations.
    controls access to that data through methods.
    program creates a single instance of this class on start
    """
    def __init__(self):
        # donor names as keys, list of donations as values
        # Example: {"Joe Donorname": [100, 200], "Mary Moneybags": [100000000]}
        self.donor_list = {}

    def __str__(self):
        return str(self.donor_list)

    def add_donor(self, name):
        """Add a new donor to the data."""
        self.donor_list[name] = []

    def donor_exists(self, name):
        """Return true if donor is found in data, false if not."""
        return name in self.donor_list

    def add_donation(self, name, donation):
        """Add a donation to a donor's history.
        If donor does not exist, create donor in data.
        """
        if not self.donor_exists(name):
            self.add_donor(name)
        self.donor_list[name].append(float(donation))

donor_data = DonorList()


def safe_input(prompt):
    """Allow canceling input without errors"""
    try:
        user_input = raw_input(prompt)
    except EOFError:
        user_input = None
    except KeyboardInterrupt:
        user_input = None

    return user_input


def prompt_for_input(prompt, validator=None):
    """Request input from the user and return it if valid.
    If input is not valid, prompt is repeated.
    User may exit to main menu at any time by entering 'quit'
    Args:
        prompt(string) - Prompt containing the user's choices and info
        validator(function) - Checks input. Returns True or False. Optional.
    """
    print(prompt)
    user_input = safe_input("> ")
    if user_input == "quit" or user_input is None:
        return None

    if (validator and validator(user_input)) or not validator:
        return user_input
    else:
        prompt_for_input(prompt, validator)


def donation_validator(user_input):
    """Check to make sure the supplied donation amount is a positive float."""
    try:
        num = float(user_input)
        if num <= 0:
            raise ValueError
        return True
    except ValueError:
        print("ERROR! Please enter a positive number!")
        return False


if __name__ == "__main__":
    while True:
        system('clear')
        main_menu_input = prompt_for_input("(t)hank you or create (r)eport")
        if main_menu_input == "t":
            print("Thank you menu")
            prompt_for_input("Press Enter to Continue")
        elif main_menu_input == "r":
            print("Report menu")
            prompt_for_input("Press Enter to Continue")
        else:
            break