"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

import platform
from typing import Dict, List, Mapping, Optional, Sequence, Tuple, Union, cast

import pkg_resources

from .__version__ import __author__, __copyright__, __email__, __license__, __version__


def get_envinfo(packages: Optional[Sequence[str]] = None) -> Dict[str, str]:
    uname = platform.uname()
    envinfo = {
        "uname": "{} {} {} {}".format(uname.system, uname.node, uname.release, uname.machine),
        "implementation": platform.python_implementation(),
        "version": platform.python_version(),
    }

    if not packages:
        return envinfo

    for pkg in packages:
        if not pkg:
            continue

        key = "{} version".format(pkg)
        try:
            envinfo[key] = pkg_resources.get_distribution(pkg).version
        except pkg_resources.DistributionNotFound:
            envinfo[key] = "not installed"

    return envinfo


def dumps(packages: Optional[Sequence[str]] = None, format: Optional[str] = None) -> str:
    envinfo = get_envinfo(packages)
    uname = envinfo.pop("uname")
    implementation = envinfo.pop("implementation")
    version = envinfo.pop("version")

    lines = ["uname: {}".format(uname), "{} version: {}".format(implementation, version)]
    lines.extend(["{}: {}".format(key, value) for key, value in envinfo.items()])

    if format and format.strip().lower() == "markdown":
        lines = ["- {}".format(line) for line in lines]

    return "\n".join(lines)
