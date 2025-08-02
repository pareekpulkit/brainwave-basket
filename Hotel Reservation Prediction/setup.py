from setuptools import setup, find_packages 

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name = 'Hotel-Reservatio-Prediction',
    version='0.1',
    author='Pulkit Pareek',
    packages=find_packages(),
    install_requires = requirements
)

