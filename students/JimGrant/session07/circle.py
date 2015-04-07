#!/usr/bin/env python
"""circle class --

fill this in so it will pass all the tests.
"""
import math


class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return u"Circle with radius: %.6f" % self.radius

    def __repr__(self):
        return u"Circle(%s)" % self.radius

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __cmp__(self, other):
        return self.radius - other.radius

    def __ne__(self, other):
        return self.radius != other.radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return math.pi * (self.radius ** 2)