#!/usr/bin/env python3

"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

import argparse
from textwrap import dedent

from . import dumps
from .__version__ import __version__


def parse_option() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=dedent(
            """\
            Issue tracker: https://github.com/thombashi/envinfopy/issues
            """
        ),
    )
    parser.add_argument(
        "-V", "--version", action="version", version="%(prog)s {}".format(__version__)
    )

    parser.add_argument(
        "--packages",
        default="",
        help="comma-separated packages that extract versions.",
    )
    parser.add_argument(
        "--format",
        choices=["text", "markdown"],
        default="text",
        help="output format",
    )

    return parser.parse_args()


def main() -> None:
    options = parse_option()

    print(dumps(options.packages.split(","), options.format))


if __name__ == "__main__":
    main()
