"""
Splits a large file into chunks of given size.
All provided paths must be absolute.
"""

import os
import sys
import argparse

kb = 1024
mb = 1024 * kb


def split_file(path_to_file, path_to_parts, size):
    if not os.path.exists(path_to_parts):
        print(f'Creating directory {os.path.abspath(path_to_parts)}...')
        os.mkdir(path_to_parts)
    else:
        consent = input(f'All files in {path_to_parts} directory will be removed.\nContinue? (yes/no):\n')
        if consent in ('yes', 'y'):
            print(f'Removing all files from directory {os.path.abspath(path_to_parts)}')
            for filename in os.listdir(path_to_parts):
                os.remove(os.path.join(path_to_parts, filename))
        else:
            print('Exiting.')
            sys.exit()

    part_num = 0

    inp = open(path_to_file, 'rb')
    print('Started writing...')
    while True:
        if not (chunk := inp.read(size)):
            break
        part_num += 1
        filename = os.path.join(path_to_parts, f'part{part_num}')
        file_obj = open(filename, 'wb')
        file_obj.write(chunk)
        file_obj.close()
        print(f'Part {part_num} written')

    inp.close()

    return part_num


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Split one large file into chunk of given size')
    parser.add_help = True

    parser.add_argument(
        '--pathToFile',
        help='Path to the file to be splitted.',
        type=str,
        required=True
    )

    parser.add_argument(
        '--pathToParts',
        help="Path to a directory for the file parts. If it doesn't exist - it will be created.",
        type=str,
        required=True
    )

    parser.add_argument(
        '--size',
        help='Whole number part size in megabytes. Default is 10.',
        type=int,
        default=10
    )

    args = parser.parse_args()

    print(split_file(args.pathToFile, args.pathToParts, args.size * mb))
