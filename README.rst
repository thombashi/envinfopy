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
    {'uname': 'Linux', 'python_implementation': 'CPython', 'python_version': '3.8.5', 'platform': 'Ubuntu 18.04', 'envinfopy': '0.0.4'}

Get environment information as Markdown:

::

    pip install envinfopy[all]  # install optional dependencies

.. code-block:: python

    >>> import envinfopy
    >>> print(envinfopy.dumps(["envinfopy"], format="markdown"))
    |  Module   |    Version    |
    | --------- | ------------- |
    | uname     | Linux         |
    | Python    | CPython 3.8.5 |
    | platform  | Ubuntu 18.04  |
    | envinfopy | 0.0.4         |

CLI usage
--------------------------------------------
::

    $ pip install envinfopy[all]  # install optional dependencies

    $ python -m envinfopy --packages envinfopy,setuptools --format markdown
    |   Module   |              Version              |
    | ---------- | --------------------------------- |
    | uname      | Linux 4.19.104-microsoft-standard |
    | Python     | CPython 3.8.5                     |
    | platform   | Ubuntu 18.04                      |
    | envinfopy  | 0.0.4                             |
    | setuptools | 57.0.0                            |


Dependencies
============================================
Python 3.6+
