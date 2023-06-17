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

    python3 -m pip install envinfopy


Usage
============================================

Library usage
--------------------------------------------

Get execution environment information as a dictionary:

.. code-block:: python

    >>> import envinfopy
    >>> envinfopy.get_envinfo()
    {'uname': 'Linux', 'python_implementation': 'CPython', 'python_version': '3.11.4', 'platform': 'Ubuntu 22.04.2 LTS'}

Get execution environment information and specific package version information:

.. code-block:: python

    >>> import envinfopy
    >>> envinfopy.get_envinfo(["envinfopy"])
    {'uname': 'Linux', 'python_implementation': 'CPython', 'python_version': '3.11.4', 'platform': 'Ubuntu 22.04.2 LTS', 'envinfopy': '0.1.0'}

Get environment information as Markdown:

::

    python3 -m pip install envinfopy[markdown]  # install optional dependencies

.. code-block:: python

    >>> import envinfopy
    >>> print(envinfopy.dumps(["envinfopy"], format="markdown"))
    |  Module   |      Version       |
    | --------- | ------------------ |
    | uname     | Linux              |
    | Python    | CPython 3.11.4     |
    | platform  | Ubuntu 22.04.2 LTS |
    | envinfopy | 0.1.0              |

CLI usage
--------------------------------------------
::

    $ python3 -m install envinfopy[cli]  # install optional dependencies

    $ python3 -m envinfopy envinfopy setuptools --format markdown
    |   Module   |                 Version                 |
    | ---------- | --------------------------------------- |
    | uname      | Linux 5.15.90.1-microsoft-standard-WSL2 |
    | Python     | CPython 3.11.4                          |
    | platform   | Ubuntu 22.04.2 LTS                      |
    | envinfopy  | 0.0.7                                   |
    | setuptools | 67.8.0                                  |

Command help
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

    usage: __main__.py [-h] [-V] [-v] [--format {text,markdown,md,json,itemize}] packages [packages ...]

    positional arguments:
      packages              PyPI package names to extract versions

    options:
      -h, --help            show this help message and exit
      -V, --version         show program's version number and exit
      -v, --verbose
      --format {text,markdown,md,json,itemize}
                            output format

    Issue tracker: https://github.com/thombashi/envinfopy/issues


Dependencies
============================================
Python 3.7+
