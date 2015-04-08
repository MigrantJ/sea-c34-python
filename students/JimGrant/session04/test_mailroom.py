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


class Test_DonorList_Get:
    d = None
    name1 = "Name1"
    name2 = "Name2"
    name3 = "Name3"
    donations = {
        name1: [get_dec(500)],
        name2: [get_dec(714), get_dec(325)],
        name3: [get_dec(0.05), get_dec(0.07)]
    }

    @classmethod
    def setup_class(cls):
        cls.d = D()
        for n, dlist in cls.donations.iteritems():
            for d in dlist:
                cls.d.add_donation(n, d)

    @classmethod
    def teardown_class(cls):
        cls.d = None

    def test_get_all_names(self):
        assert(self.donations.keys() == self.d.get_all_names())

    def test_get_all_names_sorted(self):
        assert(self.d.get_all_names_sorted() ==
               [self.name3, self.name1, self.name2])

    def test_get_num_donations(self):
        assert(self.d.get_num_donations(self.name1) == 1)
        assert(self.d.get_num_donations(self.name2) == 2)
        assert(self.d.get_num_donations(self.name3) == 2)

    def test_get_donation_total(self):
        assert(self.d.get_donation_total(self.name1) == get_dec(500))
        assert(self.d.get_donation_total(self.name2) == get_dec(1039))
        assert(self.d.get_donation_total(self.name3) == get_dec(0.12))

    def test_get_avg_donation(self):
        def get_avg(dlist):
            sum = reduce(lambda x, y: x + y, dlist)
            return get_dec(sum / len(dlist))
        assert(self.d.get_avg_donation(self.name1) ==
               get_avg(self.d.donor_list[self.name1]))
        assert(self.d.get_avg_donation(self.name2) ==
               get_avg(self.d.donor_list[self.name2]))
        assert(self.d.get_avg_donation(self.name3) ==
               get_avg(self.d.donor_list[self.name3]))