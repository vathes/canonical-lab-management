#!/usr/bin/env python
from setuptools import setup, find_packages
from os import path
import sys

here = path.abspath(path.dirname(__file__))

long_description = """"
Canonical DataJoint for lab management
"""

with open(path.join(here, 'requirements.txt')) as f:
    requirements = f.read().split()

setup(
    name='canonical-lab-management',
    version='0.0.1',
    description="Canonical Lab Management Pipeline",
    long_description=long_description,
    author='DataJoint NEURO',
    author_email='info@vathes.com',
    license='MIT',
    url='https://github.com/vathes/canonical-lab-management',
    keywords='neuroscience lab manamgement datajoint',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=requirements,
)
