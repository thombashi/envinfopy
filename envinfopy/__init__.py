"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

import platform
import sys
from typing import Dict, List, Mapping, Optional, Sequence, Tuple, Union, cast

import pkg_resources

from .__version__ import __author__, __copyright__, __email__, __license__, __version__


class Key:
    UNAME = "uname"
    PYTHON_IMPLEMENTATION = "python_implementation"
    PYTHON_VERSION = "python_version"


def get_uname(verbosity_level: int = 0) -> str:
    uname = platform.uname()

    if verbosity_level == 0:
        return f"{uname.system}"
    if verbosity_level == 1:
        return f"{uname.system} {uname.machine}"

    return f"{uname.system} {uname.release} {uname.machine}"


def get_envinfo(
    packages: Optional[Sequence[str]] = None, verbosity_level: int = 0
) -> Dict[str, str]:
    envinfo = {
        Key.UNAME: get_uname(verbosity_level),
        Key.PYTHON_IMPLEMENTATION: platform.python_implementation(),
        Key.PYTHON_VERSION: platform.python_version(),
    }

    if not packages:
        return envinfo

    for pkg in packages:
        if not pkg:
            continue

        try:
            envinfo[pkg] = pkg_resources.get_distribution(pkg).version
        except pkg_resources.DistributionNotFound:
            envinfo[pkg] = "not installed"

    return envinfo


def _dumps_markdown(envinfo: Dict[str, str]) -> str:
    import pytablewriter as ptw

    uname = envinfo.pop(Key.UNAME)
    py_implementation = envinfo.pop(Key.PYTHON_IMPLEMENTATION)
    py_version = envinfo.pop(Key.PYTHON_VERSION)

    matrix = [
        [Key.UNAME, uname],
        [f"{py_implementation}", py_version],
    ] + [[key, value] for key, value in envinfo.items()]
    writer = ptw.MarkdownTableWriter(headers=["Module", "Version"], value_matrix=matrix, margin=1)

    return writer.dumps()


def dumps(
    packages: Optional[Sequence[str]] = None, format: Optional[str] = None, verbosity_level: int = 0
) -> str:
    envinfo = get_envinfo(packages, verbosity_level=verbosity_level)

    if format:
        format_name = format.strip().lower()
        if format_name == "markdown":
            try:
                return _dumps_markdown(envinfo)
            except ImportError:
                print(
                    "required modules not installed. try to install dependencies with:\n"
                    "    pip install envinfopy[markdown]\n",
                    file=sys.stderr,
                )

    uname = envinfo.pop(Key.UNAME)
    py_implementation = envinfo.pop(Key.PYTHON_IMPLEMENTATION)
    py_version = envinfo.pop(Key.PYTHON_VERSION)

    lines = [
        f"{Key.UNAME}: {uname}",
        f"{py_implementation} version: {py_version}",
    ]
    lines.extend([f"{key} version: {value}" for key, value in envinfo.items()])

    return "\n".join(lines)
