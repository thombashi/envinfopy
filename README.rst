.. contents:: **envinfopy**
   :backlinks: top
   :depth: 2


Summary
============================================
.. image:: https://badge.fury.io/py/envinfopy.svg
    :target: https://badge.fury.io/py/envinfopy
    :alt: PyPI package version

.. image:: https://img.shields.io/pypi/pyversions/envinfopy.svg
    :target: https://pypi.org/project/envinfopy
    :alt: Supported Python versions

.. image:: https://img.shields.io/pypi/implementation/envinfopy.svg
    :target: https://pypi.org/project/envinfopy
    :alt: Supported Python implementations

.. image:: https://github.com/thombashi/envinfopy/workflows/Tests/badge.svg
    :target: https://github.com/thombashi/envinfopy/actions?query=workflow%3ATests
    :alt: Linux/macOS/Windows CI status

.. image:: https://coveralls.io/repos/github/thombashi/envinfopy/badge.svg?branch=master
    :target: https://coveralls.io/github/thombashi/envinfopy?branch=master
    :alt: Test coverage: coveralls

envinfopy is a Python Library to get execution environment information.


Installation
============================================
::

    pip install envinfopy


Usage
============================================

Library usage
--------------------------------------------
.. code-block:: python

    >>> import envinfopy
    >>> envinfopy.get_envinfo(["envinfopy"])
    {'uname': 'Linux ubuntu1804 4.15.0-112-generic x86_64', 'implementation': 'CPython', 'version': '3.8.5', 'envinfopy version': '0.0.1'}

Get environment information as Markdown:

.. code-block:: python

    >>> import envinfopy
    >>> print(envinfopy.dumps(["envinfopy"], "markdown"))
    - uname: Linux ubuntu1804 4.15.0-112-generic x86_64
    - CPython version: 3.8.5
    - envinfopy version: 0.0.1


CLI usage
--------------------------------------------
::

    $ python -m envinfopy --packages envinfopy --format markdown
    - uname: Linux ubuntu1804 4.15.0-112-generic x86_64
    - CPython version: 3.8.5
    - envinfopy version: 0.0.2


Dependencies
============================================
Python 3.5+
no external dependencies.
