import time
import _thread


def count(my_id, n):
    for i in range(n):
        print(f'[{my_id}] => {i}')
        time.sleep(1)


for j in range(5):
    _thread.start_new_thread(count, (j, 5))

time.sleep(6)
print('Main thread exiting.')
