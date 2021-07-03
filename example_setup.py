'''
Example setup file for building python package
'''
from setuptools import setup, find_packages
import sys

if sys.version_info < (3,0):
    sys.exit('Python 2 is not supported for this package')

with open("README.md", "r") as readme_file:
    README = readme_file.read()

with open("requirements.txt", 'r') as f:
    REQUIREMENTS = f.read().splitlines()

setup(
    name="lp",
    version="1.0.0",
    author="Jesse DeSimone, Ph.D.",
    author_email="desimone.neuro@gmail.com",
    description="client retention classification",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/jessedesimone/lp-analytics",
    packages=find_packages(),
    install_requires=REQUIREMENTS,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    entry_points={
        'console_scripts': [
            'lp-analytics=main:main'
        ]
    }
)
