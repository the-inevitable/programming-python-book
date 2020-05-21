import threading


class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1


def worker(local_items, local_counter):
    for _ in range(local_items):
        local_counter.increment()


def run_threads(func, local_items, local_counter):
    threads = []
    for i in range(5):
        args = (local_items, local_counter)
        thread = threading.Thread(target=func, args=args)
        threads.append(thread)
        thread.start()
    for t in threads:
        t.join()


items = 100000
counter = Counter()

run_threads(worker, items, counter)

print(f'Counter should be {5 * 100000}. Found {counter.count}')
