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
        self.donor_list[name].append(donation)

donor_data = DonorList()

if __name__ == "__main__":
    donor_data.add_donation("Homer Donor", 100)
    donor_data.add_donation("Rhonda Donor", 200)
    donor_data.add_donation("Homer Donor", 300)
    print(donor_data)