import re
import sys

import pytest
from subprocrunner import SubprocessRunner


RE_VERSION = re.compile(r"[0-9]\.[0-9]+\.[0-9]+", re.MULTILINE)


class Test_cli:
    def test_help(self, tmpdir):
        runner = SubprocessRunner([sys.executable, "-m", "envinfopy", "-h"])
        runner.run()
        assert runner.returncode == 0

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
        runner = SubprocessRunner(
            [sys.executable, "-m", "envinfopy", "--format", format, "pathvalidate", "envinfopy"]
        )
        runner.run()

        print(runner.stdout)

        assert runner.returncode == 0
        assert RE_VERSION.search(runner.stdout)
        assert re.search("envinfopy", runner.stdout, re.MULTILINE)
