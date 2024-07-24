# setup.py

from setuptools import setup, find_packages

setup(
    name='addition',
    version='0.1.0',
    packages=find_packages(where='app'),
    package_dir={'': 'app'},
    py_modules=['addition'],
    entry_points={
        'console_scripts': [
            'addition = addition:add',
        ],
    },
)
