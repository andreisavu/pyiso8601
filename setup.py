try:
    from setuptools import setup
except ImportError:
    from distutils import setup

long_description="""Simple module to parse ISO 8601 dates

This module parses the most common forms of ISO 8601 date strings (e.g.
2007-01-14T20:34:22+00:00) into datetime objects.

Changes
=======

0.1.2
-----

* Adding ParseError to __all__ in iso8601 module, allows people to import it.
  Addresses issue 7.
* Be a little more flexible when dealing with dates without leading zeroes.
  This violates the spec a little, but handles more dates as seen in the 
  field. Addresses issue 6.
* Allow date/time separators other than T.

0.1.1
-----

* When parsing dates without a timezone the specified default is used. If no
  default is specified then UTC is used. Addresses issue 4.
"""

setup(
    name="iso8601",
    version="0.1.2",
    description=long_description.split("\n")[0],
    long_description=long_description,
    author="Michael Twomey",
    author_email="micktwomey+iso8601@gmail.com",
    url="http://code.google.com/p/pyiso8601/",
    packages=["iso8601"],
    license="MIT",
)
