# -*- coding: utf-8 -*-

# sympy_random_matrix
# -------------------
# create random matrix for sympy (created by auxilium)
#
# Author:   Jan-Philipp Hoffmann
# Version:  0.1, copyright Friday, 05 July 2024
# Website:  https://github.com/Jan-Philipp Hoffmann/sympy_random_matrix
# License:  Apache License 2.0 (see LICENSE file)


import logging

logging.getLogger(__name__).addHandler(logging.NullHandler())

__doc__ = 'create random matrix for sympy (created by auxilium)'
__license__ = 'Apache License 2.0'

__author__ = 'Jan-Philipp Hoffmann'
__email__ = 'jan-philipp.hoffmann@h-da.de'
__url__ = 'https://github.com/Jan-Philipp Hoffmann/sympy_random_matrix'

__date__ = 'Friday, 05 July 2024'
__version__ = '0.1'
__dev_status__ = '3 - Alpha'  # '4 - Beta'  or '5 - Production/Stable'

__dependencies__ = ()
__dependency_links__ = ()
__data__ = ()
__scripts__ = ()
__theme__ = ''

# this is just an example to demonstrate the auxilium workflow
# it can be removed safely

# in order to import a member from a subpackage or submodule
# use relative import `from .subpackage import SomeThing`


class Line(object):
    r""" This a example class (by auxilium)

    The |Line| objects implements a straight line,
    i.e. a function $y = f(x)$ with

    $$  f(x) = a + b \\cdot x  $$

    where $a$ and $b$ are numbers.

    >>> from sympy_random_matrix import Line
    >>> a, b = 1, 2
    >>> line = Line(a, b)
    >>> line.y(x=3)
    7
    >>> line(3)  # Line objects are callable
    7
    >>> line.a
    1
    >>> line.b
    2

    """
    def __init__(self, a=0, b=1):
        self._a = a
        self._b = b

    @property
    def a(self):
        """ a value """
        return self._a

    @property
    def b(self):
        """ b value """
        return self._b

    def y(self, x=1):
        """ gives y value depending on x value argument

        :param x: x value
        :return: $a + b * x$

        """
        return self._a + self._b * x

    def __call__(self, x=1):
        return self.y(x)
