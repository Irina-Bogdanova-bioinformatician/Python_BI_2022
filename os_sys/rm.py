#!/usr/bin/env python

import argparse
import os.path
import sys


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Remove each specified file. By default, it does not remove "
                                                 "directories.")
    parser.add_argument('-r', '--recursive', action='store_true', default=False,
                        help='Remove directories and their contents recursively.')
    parser.add_argument('entities_to_delete', nargs='+', default=sys.stdin)
    args = parser.parse_args()
    for entity in args.entities_to_delete:
        if os.path.isfile(entity):
            os.unlink(entity)
        elif os.path.isdir(entity) and args.recursive:
            for root, dir_names, file_names in os.walk(entity, topdown=False):
                for file in file_names:
                    os.remove(os.path.join(root, file))
                for directory in dir_names:
                    os.rmdir(os.path.join(root, directory))
                os.rmdir(root)
        else:
            print(f"rm.py: cannot remove '{entity}': No such file or directory")
