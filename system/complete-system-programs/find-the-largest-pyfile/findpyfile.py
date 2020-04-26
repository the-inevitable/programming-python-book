"""
Find the largest file with a given extension in a given directory.
"""

import os
import glob
import argparse


def find_largest_file(path, ext):
    all_files = glob.glob(os.sep.join([path, '*.' + ext]))
    all_sizes = [os.path.getsize(filename) for filename in all_files]
    all_sizes_dict = {filename: file_size for (filename, file_size) in zip(all_files, all_sizes)}
    largest_file = ''.join([name for name in all_sizes_dict if all_sizes_dict[name] == max(all_sizes)])
    return largest_file


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
        default='py',
        required=True
    )

    args = parser.parse_args()

    print(find_largest_file(args.path, args.ext))
