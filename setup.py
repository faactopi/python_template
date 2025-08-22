# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='library',
    version='0.0.1',
    description='Faactopi python template library',
    long_description=readme,
    author='Francis Pradel',
    author_email='francis.pradel@faactopi.com',
    url='https://github.com/faactopi/python_template',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

