#!/usr/bin/python

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

    
setup(
    name='Wise Old Man',
    version='1.0.0',
    description='Wise Old Man is a portfolio tracking and analysis software for individuals looking to maximize IIR.',
    long_description=readme,
    author='Adam Plotzker',
    author_email='pladamgregory@gmail.com',
    url='https://github.com/aws-samples/wise-old-man-technologies',
    license=license,
    
    requires=[
        'path',
        'pathlib',
        'jsonschema',
        'pandas',
        'urllib3',
        'pyarrow',
        'inquirer',
        'requests',
        'flatten-json',
        'pyarrow'
    ],
    packages=find_packages(exclude=('tests', 'docs'))
)






