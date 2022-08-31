import os
import orjson

from . import g


def get_system_info():
    """return the system information"""
    print("*" * 80)
    print(f"{os.name}")
    print(f"{os.uname().sysname}")
    print(f"{os.uname().nodename}")
    print("*" * 80)
    return os.uname()


def get_all_environ() -> bytes:
    environ_dict = {}
    for k, v in os.environ.items():
        environ_dict.update({k: v})
    print("*" * 80)
    print(environ_dict)
    print("*" * 80)
    return orjson.dumps(environ_dict)


def add_one(number: int) -> int:
    return number + 1


if __name__ == "__main__":
    get_all_environ()
    print(g.url)