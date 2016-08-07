#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='anndi',
      version='0.2',
      description="Experimental dependency injection that uses annotations.",
      author='Vladimir Iakovlev',
      author_email='nvbn.rm@gmail.com',
      url='https://github.com/nvbn/anndi',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples',
                                      'tests', 'tests.*', 'release']))
