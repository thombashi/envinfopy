import re

import envinfopy


RE_VERSION = re.compile(r"[0-9]\.[0-9]+\.[0-9]+", re.MULTILINE)


class Test_get_envinfo:
    def test_normal(self):
        envinfo = envinfopy.get_envinfo(["pytest", "envinfopy"])
        print(envinfo)

        assert len(envinfo["uname"]) >= 10
        assert RE_VERSION.search(envinfo["version"])
        assert RE_VERSION.search(envinfo["pytest version"])
        assert RE_VERSION.search(envinfo["envinfopy version"])

    def test_abnormal_not_installed(self):
        envinfo = envinfopy.get_envinfo(["not-installed-pkg"])
        print(envinfo)

        assert len(envinfo["uname"]) >= 10
        assert RE_VERSION.search(envinfo["version"])
        assert envinfo["not-installed-pkg version"] == "not installed"

    def test_abnormal_empty(self):
        envinfo = envinfopy.get_envinfo([""])

        assert envinfo == envinfopy.get_envinfo()


class Test_dumps:
    def test_smoke(self):
        output = envinfopy.dumps()

        assert len(output) > 20
        assert RE_VERSION.search(output)
