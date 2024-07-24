# setup.py

from setuptools import setup, find_packages

setup(
    name='addition',
    version='0.1.0',
    packages=find_packages(where='app'),    #This will searches for packages within the app directory.
    package_dir={'': 'app'},            # indicates that the root of the package hierarchy is in the app directory.
    py_modules=['addition'],            # THis specifies that the addition module should be included in the distribution. This assumes that there is an addition.py file directly in the app directory.
    entry_points={                      #The entry_points argument specifies that a console script named addition should be created, which will execute the add function from the addition module when called.
        'console_scripts': [
            'addition = addition:add',
        ],
    },
)
