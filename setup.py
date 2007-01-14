try:
    from setuptools import setup
except ImportError:
    from distutils import setup

long_description="""Simple module to parse ISO 8601 dates

This module parses the most common forms of ISO 8601 date strings into
datetime objects.
"""

setup(
    name="iso8601",
    version="0.1",
    description=long_description.split("\n")[0],
    long_description=long_description,
    author="Michael Twomey",
    author_email="micktwomey+iso8601@gmail.com",
    url="http://code.google.com/p/pyiso8601/",
    packages=["iso8601"],
)
