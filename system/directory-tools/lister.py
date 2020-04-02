"""
Command-line lister.
"""

import os
import sys


def lister(top):
    for (current_dir, sub_dirs, file_names) in os.walk(top):
        print(f'\n{current_dir}')
        for fname in file_names:
            print(f'\t{os.path.join(current_dir, fname)}')


if __name__ == '__main__':
    lister(sys.argv[1])
