import threading
import time
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED


def func2(n):
    print('thread {} starts\n'.format(threading.current_thread().name))
    time.sleep(2)
    print('thread {} ends \n'.format(threading.current_thread().name))
    return n


if __name__ == '__main__':
    print('main thread is {}'.format(threading.current_thread().name))
    start_time = time.time()
    executor = ThreadPoolExecutor(5)
    all_tasks = [executor.submit(func2, i) for i in range(8)]
    wait(all_tasks, return_when=ALL_COMPLETED)
    end_time = time.time()
    print('total time is {}'.format(str(end_time - start_time)))
