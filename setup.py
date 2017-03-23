#! /usr/bin/python
import os
from setuptools import setup, find_packages

setup(
    name='elected-targets',
    version='0.1',
    author='MoveOn.org',
    author_email='opensource@moveon.org',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/MoveOnOrg/elected-targets',
    description='A Django app for elected petition targets',
    classifiers=[],
)
