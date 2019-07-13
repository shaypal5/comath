comath
######

|PyPI-Status| |PyPI-Versions| |Build-Status| |Codecov| |LICENCE|

A small pure-python package for math-related utility functions.

.. code-block:: python

  >>> from comath.array import percentile
  >>> percentile([4,6,8,9,11], 0.4)
  7.0

.. contents::

.. section-numbering::


Installation
============

Install ``comath`` with:

.. code-block:: bash

  pip install comath


Use
===

``comath`` is divided into four sub-modules.

array
-----

Array operations like percentile and median.


func
----

Utility function like a smooth step function and closest larger power of 2.


metric
------

Computing moving metrics (moving average, precision and variance).


segment
----------

Defines a one-dimensional line segment.


Contributing
============

Package author and current maintainer is Shay Palachy (shay.palachy@gmail.com); You are more than welcome to approach him for help. Contributions are very welcomed.

Installing for development
--------------------------

Clone:

.. code-block:: bash

  git clone git@github.com:shaypal5/comath.git


Install in development mode with test dependencies:

.. code-block:: bash

  cd comath
  pip install -e ".[test]"


Running the tests
-----------------

To run the tests, use:

.. code-block:: bash

  python -m pytest --cov=comath --doctest-modules


Adding documentation
--------------------

This project is documented using the `numpy docstring conventions`_, which were chosen as they are perhaps the most widely-spread conventions that are both supported by common tools such as Sphinx and result in human-readable docstrings (in my personal opinion, of course). When documenting code you add to this project, please follow `these conventions`_.

.. _`numpy docstring conventions`: https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt
.. _`these conventions`: https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt


Credits
=======
Created by Shay Palachy  (shay.palachy@gmail.com).

.. |PyPI-Status| image:: https://img.shields.io/pypi/v/comath.svg
  :target: https://pypi.python.org/pypi/comath

.. |PyPI-Versions| image:: https://img.shields.io/pypi/pyversions/comath.svg
   :target: https://pypi.python.org/pypi/comath

.. |Build-Status| image:: https://travis-ci.org/shaypal5/comath.svg?branch=master
  :target: https://travis-ci.org/shaypal5/comath

.. |LICENCE| image:: https://img.shields.io/pypi/l/comath.svg
  :target: https://pypi.python.org/pypi/comath

.. |Codecov| image:: https://codecov.io/github/shaypal5/comath/coverage.svg?branch=master
   :target: https://codecov.io/github/shaypal5/comath?branch=master
