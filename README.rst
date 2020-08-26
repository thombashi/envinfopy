.. contents:: **pyenvinfo**
   :backlinks: top
   :depth: 2


Summary
============================================
.. image:: https://badge.fury.io/py/pyenvinfo.svg
    :target: https://badge.fury.io/py/pyenvinfo
    :alt: PyPI package version

.. image:: https://img.shields.io/pypi/pyversions/pyenvinfo.svg
    :target: https://pypi.org/project/pyenvinfo
    :alt: Supported Python versions

.. image:: https://img.shields.io/pypi/implementation/pyenvinfo.svg
    :target: https://pypi.org/project/pyenvinfo
    :alt: Supported Python implementations

.. image:: https://github.com/thombashi/pyenvinfo/workflows/Tests/badge.svg
    :target: https://github.com/thombashi/pyenvinfo/actions?query=workflow%3ATests
    :alt: Linux/macOS/Windows CI status

.. image:: https://coveralls.io/repos/github/thombashi/pyenvinfo/badge.svg?branch=master
    :target: https://coveralls.io/github/thombashi/pyenvinfo?branch=master
    :alt: Test coverage: coveralls

pyenvinfo is a Python Library to get execution environment information.


Installation
============================================
::

    pip install pyenvinfo


Usage
============================================

Library usage
--------------------------------------------
.. code-block:: python

    >>> import pyenvinfo
    >>> pyenvinfo.get_envinfo(["pyenvinfo"])
    {'uname': 'Linux ubuntu1804 4.15.0-112-generic x86_64', 'implementation': 'CPython', 'version': '3.8.5', 'pyenvinfo version': '0.0.1'}

Get environment info as Markdown:

.. code-block:: python

    >>> import pyenvinfo
    >>> print(pyenvinfo.dumps(["pyenvinfo"], "markdown"))
    - uname: Linux ubuntu1804 4.15.0-112-generic x86_64
    - CPython version: 3.8.5
    - pyenvinfo version: 0.0.1


CLI usage
--------------------------------------------
::

    $ python -m pyenvinfo --packages pyenvinfo
    uname: Linux ubuntu1804 4.15.0-112-generic x86_64
    CPython version: 3.8.5
    pyenvinfo version: 0.0.1


Dependencies
============================================
Python 3.5+
no external dependencies.
