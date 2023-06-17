from enum import Enum, unique


class Key:
    UNAME = "uname"
    PLATFORM = "platform"
    PYTHON = "Python"
    PYTHON_IMPLEMENTATION = "python_implementation"
    PYTHON_VERSION = "python_version"


@unique
class OutputFormat(Enum):
    MARKDOWN = "markdown"
    ITEMIZE = "itemize"
    JSON = "json"
    TEXT = "text"
