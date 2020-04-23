import os
import time


def child(pipe_out):
    zzz = 0
    while True:
        time.sleep(zzz)
        msg = f'Spam {zzz}'.encode()
        os.write(pipe_out, msg)
        zzz = (zzz + 1) % 5


def parent():
    # make 2-ended pipe
    pipe_in, pipe_out = os.pipe()
    if (child_pid := os.fork()) == 0:
        child(pipe_out)
    else:
        while True:
            line = os.read(pipe_in, 32)
            print(f'Parent {os.getpid()} got [{line}] from {child_pid} at {time.time()}')


parent()
