import re

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
    def test_smoke(self):
        output = envinfopy.dumps()

        assert len(output) > 20
        assert RE_VERSION.search(output)
