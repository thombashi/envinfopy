import re
import sys
from itertools import combinations

import pytest

import envinfopy
from envinfopy import Key


RE_VERSION = re.compile(r"[0-9]\.[0-9]+\.[0-9]+", re.MULTILINE)


class Test_get_uname:
    def test_normal(self):
        value_v0 = envinfopy.get_uname(verbosity_level=0)
        assert len(value_v0) > 0

        value_v1 = envinfopy.get_uname(verbosity_level=1)
        assert len(value_v1) > len(value_v0)

        value_v2 = envinfopy.get_uname(verbosity_level=2)
        assert len(value_v2) > len(value_v1)


class Test_get_envinfo:
    def test_normal(self):
        envinfo = envinfopy.get_envinfo(["pytest", "envinfopy"])
        print(envinfo)

        assert len(envinfo["uname"]) > 0
        assert RE_VERSION.search(envinfo[Key.PYTHON_VERSION])
        assert RE_VERSION.search(envinfo["pytest"])
        assert RE_VERSION.search(envinfo["envinfopy"])

    def test_abnormal_not_installed(self):
        envinfo = envinfopy.get_envinfo(["not-installed-pkg"])
        print(envinfo)

        assert len(envinfo["uname"]) > 0
        assert RE_VERSION.search(envinfo[Key.PYTHON_VERSION])
        assert envinfo["not-installed-pkg"] == "not installed"

    def test_abnormal_empty(self):
        envinfo = envinfopy.get_envinfo([""])

        assert envinfo == envinfopy.get_envinfo()


class Test_dumps:
    @pytest.mark.parametrize(
        ["format"],
        [
            ["text"],
            ["itemize"],
            ["markdown"],
            ["json"],
        ],
    )
    def test_smoke(self, format):
        result_sep = "-" * 40

        output_v0 = envinfopy.dumps(format=format, verbosity_level=0)
        assert len(output_v0) > 20
        assert RE_VERSION.search(output_v0)

        output_v1 = envinfopy.dumps(format=format, verbosity_level=1)
        print(f"{output_v0}\n\n{output_v1}\n{result_sep}", file=sys.stderr)
        assert len(output_v1) > 20
        assert len(output_v1) >= len(output_v0)
        assert RE_VERSION.search(output_v1)

        output_v2 = envinfopy.dumps(format=format, verbosity_level=2)
        print(f"{output_v1}\n\n{output_v2}\n{result_sep}", file=sys.stderr)
        assert len(output_v2) > 20
        assert len(output_v2) >= len(output_v1)
        assert RE_VERSION.search(output_v2)

    @pytest.mark.parametrize(
        ["lhs", "rhs"],
        list(combinations(["text", "itemize", "markdown", "json"], 2)),
    )
    def test_smoke_format(self, lhs, rhs):
        lhs_text = envinfopy.dumps(format=lhs)
        rhs_text = envinfopy.dumps(format=rhs)

        print(f"[{lhs}]\n{lhs_text}\n\n[{rhs}]\n{rhs_text}")

        assert envinfopy.dumps(format=lhs) != envinfopy.dumps(format=rhs)

    def test_smoke_additional_envinfo(self):
        add_key = "hoge"
        add_version = "1.2.3"

        output = envinfopy.dumps(additional_envinfo={add_key: add_version})
        assert re.search(add_key, output, re.MULTILINE)
        assert re.search(re.escape(add_version), output, re.MULTILINE)
