import os
from multiprocessing import Pool


def powers(x):
    return 2**x


if __name__ == '__main__':
    workers = Pool(processes=1)

    results = workers.map(powers, range(20))

    print(results[-2:])
