"""
multiprocessing.Process works like threading.Thread, but
runs function call in parallel in a process instead of a thread.
Locks can be used to synchronize, e.g. prints on some platforms.
"""

import os
from multiprocessing import Process, Lock


# It will work the same without Lock, here it is just for example.
def who_am_i(label, lck):
    with lck:
        print(f'{label}: name:{__name__} pid:{os.getpid()}')


if __name__ == '__main__':
    lock = Lock()
    who_am_i('function call', lock)

    p = Process(target=who_am_i, args=('spawned child', lock))
    p.start()
    p.join()

    for i in range(5):
        Process(target=who_am_i, args=(f'Run process {i}', lock)).start()

    with lock:
        print('Main process exiting.')
