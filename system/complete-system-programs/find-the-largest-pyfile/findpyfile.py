"""
Find the largest file with a given extension in a given directory.
"""

import os
import sys
import glob
import argparse


def find_largest_file(path, ext):
    all_files = glob.glob(os.sep.join([path, ext]))
    all_sizes = [os.path.getsize(filename) for filename in all_files]
    return max(all_sizes)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find the largest file.')

    parser.add_argument('--path', required=True)
    parser.add_argument('--ext', required=True)