#!/usr/bin/env python

import argparse
import sys


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Write sorted concatenation of all FILE(s) to standard output. "
                                                 "With no FILE, or when FILE is -, read standard input.")
    parser.add_argument('files', nargs='+', type=argparse.FileType('r'), default=sys.stdin)
    args = parser.parse_args()

    all_lines = []
    for file in args.files:
        for line in file:
            all_lines.append(line.strip())
    all_lines.sort()
    for line in all_lines:
        print(line)
