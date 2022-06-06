import threading
import time


def func2(n):
    print('thread {} starts'.format(threading.current_thread().name))
    time.sleep(2)
    print('thread {} ends'.format(threading.current_thread().name))
    return n


if __name__ == '__main__':
    print('main thread is {}'.format(threading.current_thread().name))
    start_time = time.time()
    t1 = threading.Thread(target=func2, args=(1,))
    t2 = threading.Thread(target=func2, args=(2,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end_time = time.time()
    print('total time is {}'.format(str(end_time - start_time)))
