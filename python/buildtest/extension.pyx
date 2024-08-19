#!/usr/bin/env python
# vim: sts=4 sw=4 et

from .extension cimport *

def call(v):
    return buildtest_call(v)
