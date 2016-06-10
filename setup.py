# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='reliability-polynomial',
    version='0.0.1',
    description='Reliability Polynomial',
    long_description=readme,
    author='Ryan Dougherty',
    author_email='ryan.dougherty@asu.edu',
    url='https://github.com/ryandougherty/Reliability-Polynomial',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

