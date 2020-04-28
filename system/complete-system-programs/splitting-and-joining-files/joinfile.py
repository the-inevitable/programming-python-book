"""
Joins parts of a file from splitfile.py into a single file.
Parts must have name in a format of 'partN' where N is a part number.
All provided paths must be absolute.
"""

import os
import sys
import argparse


def join_parts(path_to_parts, path_to_file):
    if not all([filename.startswith('part') for filename in os.listdir(path_to_parts)]):
        print(f'All file parts must have a name in format of "partN", where N is a part number.')
        sys.exit()

    if not (os.path.isdir(path_to_parts) and os.path.exists(path_to_parts)):
        print(f'Directory {os.path.abspath(path_to_parts)} does not exist or is empty.')

    if os.path.exists(path_to_file):
        consent = input(f'File with path {path_to_file} already exists. It will be overwritten. Continue? (yes/no):\n')
        if consent not in ('yes', 'y'):
            print('Exiting.')
            sys.exit()

    output = open(path_to_file, 'wb')
    print(f'File {path_to_file} created.')

    parts = os.listdir(path_to_parts)
    parts.sort(key=lambda x: int(x[4:]))

    print('Writing...')
    for part in parts:
        file_obj_bytes = open(os.path.join(path_to_parts, part), 'rb').read()
        output.write(file_obj_bytes)
        print(f'{part} written')

    output.close()

    return f'Written file {path_to_file}. The size is {round(os.path.getsize(path_to_file) / 1024 / 1024, 3)} Mb.'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Join file parts into a single file.')
    parser.add_help = True

    parser.add_argument(
        '--pathToParts',
        help='Path to a directory with file parts.',
        type=str,
        required=True
    )

    parser.add_argument(
        '--pathToFile',
        help='Path to a file to be created / overwritten.',
        type=str,
        required=True
    )

    args = parser.parse_args()

    print(join_parts(args.pathToParts, args.pathToFile))
