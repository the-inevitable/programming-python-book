"""
Walks through directory tree recursively.
"""

import os
import sys


def recur_lister(top):
    print(f'\n{top}')
    for name in os.listdir(top):
        path = os.path.join(top, name)
        if not os.path.isdir(path):
            print(f'\t{path}')
        else:
            recur_lister(path)


if __name__ == '__main__':
    recur_lister(sys.argv[1])
