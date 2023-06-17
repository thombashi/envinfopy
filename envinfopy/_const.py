from enum import Enum, unique


CGROUP_RPOC = "/proc/1/cgroup"


class Key:
    UNAME = "uname"
    PLATFORM = "platform"
    PYTHON = "Python"
    PYTHON_IMPLEMENTATION = "python_implementation"
    PYTHON_VERSION = "python_version"
    RUN_ON_DOCKER = "Run on Docker"


@unique
class OutputFormat(Enum):
    MARKDOWN = "markdown"
    ITEMIZE = "itemize"
    JSON = "json"
    TEXT = "text"
