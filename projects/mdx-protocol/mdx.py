#!/bin/python
import enum
import sys
from enum import IntEnum
from itertools import chain


class Channel:
    VERSION = 1

    def __init__(self, mux_id, data):
        self._mux_id = mux_id
        self._data = data

    def __bytes__(self):
        reserved = 0
        checksum = 0
        length = len(self._data)
        return bytes(chain.from_iterable((
            self.VERSION.to_bytes(2, 'big'),
            reserved.to_bytes(2, 'big'),
            checksum.to_bytes(2, 'big'),
            self._mux_id.to_bytes(2, 'big'),
            length.to_bytes(4, 'big'),
            self._data
        )))


class Cli:
    class ExitCode(enum.IntEnum):
        SUCCESS = 0
        FAILURE = -1

    def main(self, argv=None):
        sys.exit(Cli.ExitCode.SUCCESS)


if __name__ == '__main__':
    Cli.main()
