"""
Fork basics: start 5 copies of this program running in parallel with the original.
Each copy counts up to 5 on the same stdout stream--forks copy process memory, including file descriptors.
"""

import os
import time


def counter(count):
    for i in range(count):
        time.sleep(1)
        print(f'{os.getpid()} => {i}')


for i in range(5):
    pid = os.fork()
    if pid != 0:
        print(f'Process {pid} spawned')
    else:
        counter(5)
        os._exit(0)


print('Main process exiting.')
