import re
import sys

from subprocrunner import SubprocessRunner


RE_VERSION = re.compile(r"[0-9]\.[0-9]+\.[0-9]+", re.MULTILINE)


class Test_cli:
    def test_help(self, tmpdir):
        runner = SubprocessRunner([sys.executable, "-m", "envinfopy", "-h"])
        runner.run()
        assert runner.returncode == 0

    def test_smoke(self, tmpdir):
        runner = SubprocessRunner([sys.executable, "-m", "envinfopy", "--packages", "envinfopy"])
        runner.run()

        print(runner.stdout)

        assert runner.returncode == 0
        assert RE_VERSION.search(runner.stdout)
        assert re.search("envinfopy version:", runner.stdout, re.MULTILINE)
