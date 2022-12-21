#!/usr/bin/env python

import argparse
import sys
import re


def merge_dicts(dict_1, dict_2):
    merged = {}
    for key in dict_2:
        if key not in dict_1:
            merged[key] = dict_2[key]
        else:
            merged[key] = dict_2[key] + dict_1[key]
    return merged


def get_complete_file_info(flag_l, flag_w, flag_c, new_file):
    if not flag_l and not flag_w and not flag_c:
        flag_l, flag_w, flag_c = True, True, True
    all_counts = {}
    lines_counts, words_counts, bytes_counts = 0, 0, 0
    for line in new_file:
        line_decoded = line.decode("utf-8")
        if flag_l and '\n' in line_decoded:
            lines_counts += 1  # count '\n' as in 'wc' (in that case we get (n - 1) lines)
        if flag_w:
            words_counts += len(re.findall(r"\w+'?\w+|\w+\.?\w+", line_decoded))
        if flag_c:
            bytes_counts += len(line)
    if flag_l:
        all_counts["lines"] = lines_counts
    if flag_w:
        all_counts["words"] = words_counts
    if flag_c:
        all_counts["bytes"] = bytes_counts
    return all_counts


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Print newline, word, and byte counts for each FILE, and a total line "
                                                 "if more than one FILE is specified. With no FILE, or when FILE is -, "
                                                 "read standard input.")
    parser.add_argument('-l', '--lines', action='store_true', default=False, help='Show lines count')
    parser.add_argument('-w', '--words', action='store_true', default=False, help='Show words count')
    parser.add_argument('-c', '--bytes', action='store_true', default=False, help='Show bytes count')
    parser.add_argument('files', nargs='+', type=argparse.FileType('rb'), default=sys.stdin)
    args = parser.parse_args()

    if len(args.files) == 1:
        results = get_complete_file_info(args.lines, args.words, args.bytes, args.files[0])
        print(f'{" ".join(map(str, results.values()))} {args.files[0].name}')
    else:
        total = {}
        if args.lines:
            total["lines"] = 0
        if args.words:
            total["words"] = 0
        if args.bytes:
            total["bytes"] = 0
        for file in args.files:
            results = get_complete_file_info(args.lines, args.words, args.bytes, file)
            print(f'{" ".join(map(str, results.values()))} {file.name}')
            total = merge_dicts(total, results)  # total = {**results, **total} does not work
        print(f'{" ".join(map(str, total.values()))} total')
