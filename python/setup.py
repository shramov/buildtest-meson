#!/usr/bin/env python3
# vim: sts=4 sw=4 et

from setuptools import setup, Extension
from Cython.Distutils import build_ext

setup( name = 'buildtest'
     , packages = ['buildtest']
     , include_dirs = ["../src"]
     , cmdclass = {'build_ext': build_ext}
     , ext_modules =
         [ Extension("buildtest.extension", ["buildtest/extension.pyx"], libraries=["buildtest"])
         ]
)
