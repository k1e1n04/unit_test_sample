# setup.py
from setuptools import setup, find_packages

setup(
    name='unit_test_sample',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pytest',
        'pytest-mock',
        'pytest-cov',
    ],
    entry_points={
        'console_scripts': [
            'unit_test_sample = unit_test_sample.main:main',
        ],
    },
)
