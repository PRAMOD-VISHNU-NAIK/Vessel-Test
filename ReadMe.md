# Addition Package

This package contains a simple function to add two numbers.

## Usage

```python
from addition import add

result = add(2, 3)
print(result)  # Output: 5




## MANIFEST.in
Error: version.py file is not being found during the build process because it's not being included in the source distribution (sdist). To fix this, we need to ensure that version.py is included in the package.

To include version.py in the distribution, you can use a MANIFEST.in file and add the below code

    include version.py
