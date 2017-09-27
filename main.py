#!/usr/bin/env python3

"""
Data cleaner script to execute my data quality measures on.
"""

from __future__ import print_function
import os
import sys
import argparse
import csv


def main(arguments):
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('file_in', help="Raw input file.", type=argparse.FileType('r'))
    parser.add_argument('file_out', help="Cleaned output file.", type=argparse.FileType('w'))
    parser.parse_args(arguments)

    filename_in = arguments[0]
    filename_out = arguments[1]

    header = []
    rows_in = []
    rows_out = []

    # Open the file and turn the rows into a list
    with open(filename_in, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)

        header = rows[0]  # retrieve the header
        print("Header: {}\n\n".format(header))
        rows.pop(0)  # remove the header from our rows

        rows_in = rows

    rows_out = clean_rows(header, rows_in)

    for row in rows_out:
        print("Row out: {}".format(row))

    write_file(header, rows_out, filename_out)


def write_file(header, rows, filename):
    with open(filename, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)

        spamwriter.writerow(header)

        for row in rows:
            spamwriter.writerow(row)


def clean_rows(header_in, rows_in):
    rows_out = []
    for line in rows_in:
        chocolate = line[1]
        gender = line[3]

        # Convert to lower before validation
        chocolate = chocolate.lower()
        gender = gender.lower()

        if is_valid_chocolate(chocolate) and is_valid_gender(gender):
            line = transform_valid_line(line)

            rows_out.append(line)

    return rows_out


def transform_valid_line(line):
    transformed_line = line
    transformed_line[1] = transform_chocolate(line[1])
    transformed_line[3] = transform_gender(line[3])
    return transformed_line


def transform_chocolate(chocolate):
    return chocolate.lower()


def transform_gender(gender):
    transformed_gender = gender.lower()

    if transformed_gender == 'm':
        transformed_gender = 'male'

    if transformed_gender == 'f':
        transformed_gender = 'female'

    return transformed_gender


def is_valid_chocolate(chocolate):
    if not chocolate:  # Check if empty
        return False

    if not str.isalnum(chocolate):
        return False

    if len(chocolate.split()) > 2:
        return False

    return True


def is_valid_gender(gender):
    if not gender:  # Check if empty
        return False

    if not str.isalnum(gender):
        return False

    if len(gender.split()) > 2:
        return False

    return True


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
