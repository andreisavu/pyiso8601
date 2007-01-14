try:
    from setuptools import setup
except ImportError:
    from distutils import setup

long_description="""Simple utilities for handling ISO 8601 dates
"""

setup(
    name='iso8601',
    version="0.1",
    description=long_description.split("\n")[0],
    long_description=long_description,
    author="Michael Twomey",
    author_email="micktwomey+iso8601@gmail.com",
    #url="",
    packages=["iso8601"],
)
