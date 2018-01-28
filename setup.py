# -*- coding: utf-8 -*-

# Learn more: https://github.com/ebadali/postcodes

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='postcodes',
    version='0.1.0',
    description='postcodes package',
    long_description=readme,
    author='Ebad Ali',
    author_email='ebadalie@gmail.com',
    url='https://github.com/ebadali/postcodes',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

