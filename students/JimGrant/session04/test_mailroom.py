import mailroom as mr
from decimal import *
D = mr.DonorList


def get_dec(value):
    return Decimal(value).quantize(Decimal('.01'))


class Test_DonorList_Modify:
    d = None

    def setup_method(self, method):
        self.d = D()

    def teardown_method(self, method):
        self.d = None

    def test_init(self):
        assert(self.d.donor_list == {})

    def test_add_donor(self):
        name = "Test"
        self.d.add_donor(name)
        assert(self.d.donor_list == {name: []})
        assert(self.d.donor_exists(name))

    def test_add_donation(self):
        name1 = "Test1"
        donation1 = get_dec(500)
        name2 = "Test2"
        donation2 = get_dec(1000)
        self.d.add_donor(name1)
        self.d.add_donation(name1, donation1)
        assert(self.d.donor_list[name1] == [donation1])
        self.d.add_donation(name2, donation2)
        assert(self.d.donor_list == {name1: [donation1], name2: [donation2]})