#!/usr/bin/env python

import argparse
import os


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="List information about the FILEs (the current directory by default).")
    parser.add_argument('-a', '--all', action='store_true', default=False, help='Do not ignore entries starting with .')
    parser.add_argument('dir', nargs='?', default=os.getcwd())
    args = parser.parse_args()

    if not args.all:
        print(" ".join([file for file in os.listdir(args.dir) if not file.startswith('.')]))
    else:
        print(" ".join(os.listdir(args.dir)))
