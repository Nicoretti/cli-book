#!/bin/python
import os
import sys
import argparse
from enum import IntEnum
from struct import unpack, pack, calcsize
from itertools import chain


class DecodeError(Exception):
    pass


class Header:
    VERSION = 1
    RESERVED = 0
    BINARY_FORMAT = '>HHHHI'

    def __init__(self, mux_id, length, reserved=RESERVED, version=VERSION):
        self._version = version
        self._reserved = reserved
        self._mux_id = mux_id
        self._length = length

    @property
    def version(self):
        return self._version

    @property
    def reserved(self):
        return self._reserved

    @property
    def mux_id(self):
        return self._mux_id

    @property
    def checksum(self):
        return 0

    @property
    def length(self):
        return self._length

    def __bytes__(self):
        return pack(
            Header.BINARY_FORMAT,
            self.version,
            self.checksum,
            self.reserved,
            self.mux_id,
            self.length
        )

    @staticmethod
    def from_bytes(src):
        if len(src) != calcsize(Header.BINARY_FORMAT):
            raise DecodeError("Invalid amount of input bytes")
        version, checksum, reserved, mux_id, length = unpack(
            Header.BINARY_FORMAT,
            src
        )
        return Header(mux_id=mux_id, length=length, reserved=reserved, version=version)


class Channel:

    def __init__(self, mux_id, data):
        self._header = Header(mux_id=mux_id, length=len(data))
        self._data = bytes(data)

    @property
    def mux_id(self):
        return self._header.mux_id

    @property
    def data(self):
        return self._data

    def __eq__(self, other):
        return self.mux_id == other.mux_id and self.data == other.data

    def __ne__(self, other):
        return not (self == other)

    def __bytes__(self):
        return bytes(chain.from_iterable((
            bytes(self._header),
            self.data
        )))

    @staticmethod
    def from_bytes(data):
        size = calcsize(Header.BINARY_FORMAT)
        header = Header.from_bytes(data[0:size])
        remaining = data[size:]
        if len(remaining) < header.length:
            raise DecodeError("Not enough bytes to decode message")
        return Channel(mux_id=header.mux_id, data=remaining[0:header.length])


class Cli:
    class ExitCode(IntEnum):
        SUCCESS = 0
        FAILURE = -1

    class File:

        def __init__(self, mode='r', bufsize=-1, encoding=None, errors=None):
            self._mode = mode
            self._bufsize = bufsize
            self._encoding = encoding
            self._errors = errors

        def __call__(self, string):
            dispatch = {
                'r': lambda: sys.stdin,
                'rb': lambda: os.fdopen(sys.stdin.fileno(), 'rb', closefd=False),
                'w': lambda: sys.stdout,
                'wb': lambda: os.fdopen(sys.stdout.fileno(), 'wb', closefd=False)
            }
            if string == '-':
                try:
                    return dispatch[self._mode]()
                except KeyError as ex:
                    raise ValueError(f'argument "-" with mode {self._mode}')
            try:
                return open(string, self._mode, self._bufsize, self._encoding,
                            self._errors)
            except OSError as e:
                args = {'filename': string, 'error': e}
                message = "can't open '{filename}s': {error}s"
                raise argparse.ArgumentTypeError(message.format(args))

    def main(self, argv=None):
        p = self.create_parser()
        args = p.parse_args(argv)
        args.func(args)
        return Cli.ExitCode.SUCCESS

    @staticmethod
    def decode(settings):
        return NotImplementedError()

    @staticmethod
    def encode(settings):
        return NotImplementedError()

    @staticmethod
    def create_parser():
        parser = argparse.ArgumentParser("mdx", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        sub = parser.add_subparsers(dest='subcommand', required=True, metavar='subcommand', help='[encode, decode]')

        decode = sub.add_parser('decode', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        decode.add_argument('input', type=Cli.File('rb'), default='-', help='binary input')
        decode.add_argument('output', type=Cli.File('w'), default='-', help='decoded output')
        decode.set_defaults(func=Cli.decode)

        encode = sub.add_parser('encode', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        encode.add_argument('output', type=Cli.File('wb'), default='-', help='binary output')
        encode.add_argument('input', type=Cli.File('rb'), default='-', help='input(s) to be encoded')
        encode.add_argument('-c', '--chunk-size', type=int, default=1024, help='in bytes')
        encode.set_defaults(func=Cli.encode)

        return parser


if __name__ == '__main__':
    sys.exit(Cli().main())
