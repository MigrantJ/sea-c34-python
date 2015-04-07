#!/usr/bin/env python

import series


def test_fibonacci():
    assert(series.fibonacci(0) == 0)
    assert(series.fibonacci(1) == 1)
    assert(series.fibonacci(9) == 34)


def test_lucas():
    assert(series.lucas(0) == 2)
    assert(series.lucas(1) == 1)
    assert(series.lucas(9) == 76)


def test_sum_series():
    assert (series.sum_series(9) == 34)
    assert (series.sum_series(9, 2, 1) == 76)
    assert (series.sum_series(9, 2, 4) == 178)
