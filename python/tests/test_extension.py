#!/usr/bin/env python3
# vim: sts=4 sw=4 et

import buildtest.extension as E

def test_basic():
    assert E.call(100) == 100
