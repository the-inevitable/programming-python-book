"""
Find the largest file with a given extension in a given directory.
"""

import os
import argparse

debug = False


def find_largest_file(path, ext):
    all_sizes = []
    for (dir_name, sub_dirs, file_names) in os.walk(path):
        for file_name in file_names:
            if file_name.endswith(ext):
                full_name = os.path.join(dir_name, file_name)
                full_name_size = os.path.getsize(full_name)
                if debug:
                    print(dir_name, full_name, full_name_size)
                all_sizes.append(
                    (full_name, full_name_size)
                )
    if not all_sizes:
        return f'Could not find files with extension "{ext}" to compare in {path}.'
    all_sizes.sort(key=lambda x: x[1], reverse=True)
    largest_name = all_sizes[0][0]
    largest_size = round(all_sizes[0][1] / 1024 / 1024, 3)
    return f'The largest file in the "{path}" is: {largest_name} with the size of {largest_size} Mb.'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find the largest file.')

    parser.add_argument(
        '--path',
        help='Path to desired directory.',
        type=str,
        default='/home/vlad/projects',
        required=True
    )
    parser.add_argument(
        '--ext',
        help='File extension to find. ("txt", "py", "java")',
        type=str,
        default='',
    )

    args = parser.parse_args()

    print(find_largest_file(args.path, args.ext))
