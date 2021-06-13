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

.. image:: https://github.com/thombashi/envinfopy/actions/workflows/lint_and_test.yml/badge.svg
    :target: https://github.com/thombashi/envinfopy/actions/workflows/lint_and_test.yml
    :alt: CI status of Linux/macOS/Windows

.. image:: https://coveralls.io/repos/github/thombashi/envinfopy/badge.svg?branch=master
    :target: https://coveralls.io/github/thombashi/envinfopy?branch=master
    :alt: Test coverage: coveralls

envinfopy is a Python Library to get execution environment information.


Installation
============================================
::

    pip3 install envinfopy


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

    pip3 install envinfopy[all]  # install optional dependencies

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

    $ pip3 install envinfopy[all]  # install optional dependencies

    $ python3 -m envinfopy envinfopy setuptools --format markdown
    |   Module   |              Version              |
    | ---------- | --------------------------------- |
    | uname      | Linux 4.19.104-microsoft-standard |
    | Python     | CPython 3.8.5                     |
    | platform   | Ubuntu 18.04                      |
    | envinfopy  | 0.0.4                             |
    | setuptools | 57.0.0                            |

Command help
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

    usage: __main__.py [-h] [-V] [-v] [--format {text,markdown,json,itemize}] packages [packages ...]

    positional arguments:
      packages              package names to extract versions

    optional arguments:
      -h, --help            show this help message and exit
      -V, --version         show program's version number and exit
      -v, --verbose
      --format {text,markdown,json,itemize}
                            output format

    Issue tracker: https://github.com/thombashi/envinfopy/issues


Dependencies
============================================
Python 3.6+
