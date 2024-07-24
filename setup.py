# setup.py
import os
from setuptools import setup, find_packages

def read_version():
    version = {}
    version_file_path = os.path.join(os.path.dirname(__file__), 'version.py')
    if os.path.exists(version_file_path):
        with open(version_file_path) as fp:
            exec(fp.read(), version)
        return version['__version__']
    else:
        raise FileNotFoundError(f"Version file not found: {version_file_path}")

setup(
    name='addition',
    version=read_version(),             # Read version dynamically from version.py
    packages=find_packages(where='app'),    #This will searches for packages within the app directory.
    package_dir={'': 'app'},            # indicates that the root of the package hierarchy is in the app directory.
    py_modules=['addition'],            # THis specifies that the addition module should be included in the distribution. This assumes that there is an addition.py file directly in the app directory.
    entry_points={                      #The entry_points argument specifies that a console script named addition should be created, which will execute the add function from the addition module when called.
        'console_scripts': [
            'addition = addition:main',
        ],
    },
)
