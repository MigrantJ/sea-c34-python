from os import system
from decimal import *


class DonorList:
    """contains the list of donors and their donations.
    controls access to that data through methods.
    program creates a single instance of this class on start
    """

    def __init__(self):
        # donor names as keys, list of donations as values
        # self.donor_list = {"Joe Donornam": [100, 200, 300], "Mary Moneybags": [500, 400, 500, 500], "Haha": [10, 20], "Mitt Romney": [1000000]}
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
        donation = Decimal(donation).quantize(Decimal('.01'))
        self.donor_list[name].append(donation)

    def get_all_names(self):
        """Return names of all donors in no particular order"""
        return self.donor_list.keys()

    def get_all_names_sorted(self):
        """Return names of all donors sorted by their total donation"""
        total_list, name_list = [], []
        for name in self.donor_list.iterkeys():
            total = self.get_donation_total(name)
            for i, t in enumerate(total_list):
                if total > t:
                    continue
                else:
                    total_list.insert(i, total)
                    name_list.insert(i, name)
                    break
            else:
                total_list.append(total)
                name_list.append(name)
        return name_list

    def get_num_donations(self, name):
        return len(self.donor_list[name])

    def get_donation_total(self, name):
        total = 0
        for d in self.donor_list[name]:
            total += d
        return total

    def get_avg_donation(self, name):
        avg = self.get_donation_total(name) / self.get_num_donations(name)
        avg = Decimal(avg).quantize(Decimal('.01'))
        return avg


donor_data = DonorList()


def print_all_names():
    """Print all donor names"""
    print("List of Donors:")
    print("---------------")
    for n in donor_data.get_all_names():
        print(n)
    print("_______________")


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
        return prompt_for_input(prompt, validator)


def name_validator(user_input):
    """Check to make sure the entered donor name is an alphabetical string.
    User may also type 'list' to print all current donor names.
    """
    if user_input == "list":
        print_all_names()
        return False
    return True


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


def print_email(name, donation):
    """Print an email thanking the donor by name for their donation."""
    print("Dear {},\n\n"
          "Thank you so much for your kind donation of ${}. We here at the "
          "Foundation for Homeless Whales greatly appreciate it. Your "
          "money will go towards creating new oceans on the moon for whales "
          "to live in.\n\n"
          "Thanks again,\n\n"
          "Jim Grant\n"
          "Director, F.H.W.\n"
          .format(name, donation))


def print_report():
    """Print a tabular chart summarizing the donation data, sorted by total.
    For each donor, the following is printed:
    - Donor Name
    - Total money donated
    - Number of donations
    - Average donation amount
    """
    print("{} | {} | {} | {}".format("Name", "Total", ))
    for name in donor_data.get_all_names_sorted():
        total = donor_data.get_donation_total(name)
        s_total = "${}".format(total)
        num = donor_data.get_num_donations(name)
        avg = "${}".format(donor_data.get_avg_donation(name))

        print("{:<20} | {:>9} | {:>3} | {:>9}".format(name, s_total, num, avg))


if __name__ == "__main__":
    prompts = {
        "main": ("Choose from the following:\n"
                 "T - Send a (T)hank You\n"
                 "R - Create a (R)eport\n"
                 "quit - Quit the program",
                 None),

        "name": ("Please enter a name, or choose from the following:\n"
                 "list - Print a list of previous donors\n"
                 "quit - Return to main menu",
                 name_validator),

        "donation": ("Please enter a donation amount or 'quit':",
                     donation_validator),

        "continue": ("Press Enter to Continue...",
                     None)
    }
    while True:
        system('clear')
        print("Welcome to Mailroom Madness")
        main_menu_input = prompt_for_input(*prompts["main"])
        if main_menu_input is None:
            break
        elif main_menu_input.lower() == "t":
            name = prompt_for_input(*prompts["name"])
            if name:
                donation = prompt_for_input(*prompts["donation"])
                if donation:
                    donor_data.add_donation(name, donation)
                    system('clear')
                    print_email(name, donation)
                    prompt_for_input(*prompts["continue"])
        elif main_menu_input.lower() == "r":
            system('clear')
            print_report()
            prompt_for_input("Press Enter to Continue")
