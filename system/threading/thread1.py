"""
Spawn threads until "q" is entered at input.
"""

import _thread


def child(tid):
    print(f'Hello from thread {tid}')


def parent():
    i = 0
    while True:
        i += 1
        _thread.start_new_thread(child, (i,))
        if input() == 'q':
            break


parent()
