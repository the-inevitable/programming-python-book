"""
Uses mutexes to know when threads are done in parent/main thread,
instead of time.sleep. Lock stdout to avoid co-mingled prints.
"""

import _thread

stdout_mutex = _thread.allocate_lock()
exit_mutexes = [False] * 10


def counter(my_id, count):
    for i in range(count):
        stdout_mutex.acquire()
        print(f'[{my_id}] => {i}')
        stdout_mutex.release()
    exit_mutexes[my_id] = True


# Signal main thread.
for j in range(10):
    _thread.start_new_thread(counter, (j, 100))

while False in exit_mutexes:
    pass

print('Main thread exiting.')
