import sys

from argparse import ArgumentParser


__DEFAULT = ['mongodb']
ARG_NAME = 'database'


def create():
    parser = ArgumentParser(description='batch script for count slack post each channel.')
    parser.add_argument(ARG_NAME,
                        choices=['csv', 'mongodb'],
                        help='show verbose message')
    return parser


def parse(parser):
    args = None
    if len(sys.argv) == 1:
        args = __DEFAULT

    result = parser.parse_args(args)
    return result
