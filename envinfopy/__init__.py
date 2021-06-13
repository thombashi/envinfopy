"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

import json
import platform
import sys
from collections import OrderedDict, namedtuple
from typing import Dict, List, Mapping, Optional, Sequence, Tuple, Union, cast

import pkg_resources

from .__version__ import __author__, __copyright__, __email__, __license__, __version__


BasicEnvInfo = namedtuple("BasicEnvInfo", "uname py_implementation py_version")


class Key:
    UNAME = "uname"
    PLATFORM = "platform"
    PYTHON = "Python"
    PYTHON_IMPLEMENTATION = "python_implementation"
    PYTHON_VERSION = "python_version"


def get_uname(verbosity_level: int = 0) -> str:
    uname = platform.uname()

    if verbosity_level == 0:
        return f"{uname.system}"
    if verbosity_level == 1:
        return f"{uname.system} {uname.release}"

    return f"{uname.system} {uname.release} {uname.machine}"


def get_envinfo(
    packages: Optional[Sequence[str]] = None, verbosity_level: int = 0
) -> Dict[str, str]:
    envinfo = {
        Key.UNAME: get_uname(verbosity_level),
        Key.PYTHON_IMPLEMENTATION: platform.python_implementation(),
        Key.PYTHON_VERSION: platform.python_version(),
    }

    system = platform.system()
    if system == "Linux":
        try:
            from distro import linux_distribution

            envinfo[Key.PLATFORM] = " ".join(linux_distribution()[:2])
        except ImportError:
            pass
    elif system == "Windows":
        envinfo[Key.PLATFORM] = " ".join(platform.win32_ver()[:3])
    elif system == "Darwin":
        mac_ver = platform.mac_ver()
        envinfo[Key.PLATFORM] = " ".join([mac_ver[0], mac_ver[2]])

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


def _pop_basic_envinfo(envinfo: Dict[str, str]) -> BasicEnvInfo:
    return BasicEnvInfo(
        uname=envinfo.pop(Key.UNAME),
        py_implementation=envinfo.pop(Key.PYTHON_IMPLEMENTATION),
        py_version=envinfo.pop(Key.PYTHON_VERSION),
    )


def _dumps_markdown(envinfo: Dict[str, str]) -> str:
    import pytablewriter as ptw

    basic_envinfo = _pop_basic_envinfo(envinfo)
    matrix = [
        [Key.UNAME, basic_envinfo.uname],
        [Key.PYTHON, f"{basic_envinfo.py_implementation} {basic_envinfo.py_version}"],
    ] + [[key, value] for key, value in envinfo.items()]
    writer = ptw.MarkdownTableWriter(headers=["Module", "Version"], value_matrix=matrix, margin=1)

    return writer.dumps()


def _dumps_json(envinfo: Dict[str, str]) -> str:
    basic_envinfo = _pop_basic_envinfo(envinfo)
    outputs = {
        Key.UNAME: basic_envinfo.uname,
        Key.PYTHON: f"{basic_envinfo.py_implementation} {basic_envinfo.py_version}",
    }
    outputs.update(envinfo)

    return json.dumps(outputs, indent=4)


def dumps(
    packages: Optional[Sequence[str]] = None,
    format: Optional[str] = None,
    additional_envinfo: Optional[Mapping[str, str]] = None,
    verbosity_level: int = 0,
) -> str:
    envinfo: Dict[str, str] = OrderedDict()

    if additional_envinfo is not None:
        envinfo.update(additional_envinfo)

    envinfo.update(get_envinfo(packages, verbosity_level=verbosity_level))

    format_name = ""
    if format:
        format_name = format.strip().casefold()

    if format_name == "markdown":
        try:
            return _dumps_markdown(envinfo)
        except ImportError:
            print(
                "required modules not installed. try to install dependencies with:\n"
                "    pip install envinfopy[markdown]\n",
                file=sys.stderr,
            )
    elif format_name == "json":
        return _dumps_json(envinfo)

    basic_envinfo = _pop_basic_envinfo(envinfo)
    lines = [
        f"{Key.UNAME}: {basic_envinfo.uname}",
        f"{Key.PYTHON} version: {basic_envinfo.py_implementation} {basic_envinfo.py_version}",
    ]
    lines.extend([f"{key} version: {value}" for key, value in envinfo.items()])

    if format_name == "itemize":
        return "\n".join(f"- {line}" for line in lines)

    return "\n".join(lines)
