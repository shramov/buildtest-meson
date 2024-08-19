# vim: sts=4 sw=4 et
# cython: language_level=3

cdef extern from "buildtest.h":
    cdef int buildtest_call(int v)
