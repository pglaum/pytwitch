import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="twitch",
    version="0.0.1",
    author="Philipp Glaum",
    author_email="p@pglaum.de",
    description=("A library for the Twitch Helix API"),
    license="GPLv3",
    keywords="api twitch",
    url="https://github.com/pglaum/pytwitch",
    packages=["twitch", "twitch.models"],
    install_requires=["pydantic", "requests"],
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
