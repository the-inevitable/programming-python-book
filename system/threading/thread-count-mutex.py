"""
Synchronize access to stdout: because it is shared global,
thread outputs may be intermixed if not synchronized.
"""

import time
import _thread


def counter(my_id, count):
    for i in range(count):
        time.sleep(1)
        mutex.acquire()
        print(f'[{my_id}] => {i}')
        mutex.release()


mutex = _thread.allocate_lock()

for j in range(5):
    _thread.start_new_thread(counter, (j, 5))

time.sleep(6)
print('Main thread exiting.')
