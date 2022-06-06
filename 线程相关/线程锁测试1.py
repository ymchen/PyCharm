import threading
import time


def increase(var, lock):
    global total_increase_times
    for i in range(1000000):
        if lock.acquire():
            var[0] += 1
            lock.release()
            total_increase_times += 1


def decrease(var, lock):
    global total_decrease_times
    for i in range(1000000):
        if lock.acquire():
            var[0] -= 1
            lock.release()
            total_decrease_times += 1


if __name__ == '__main__':
    print('main thread is {}'.format(threading.current_thread().name))
    start_time = time.time()
    lock = threading.Lock()
    var = [5]
    total_increase_times = 0
    total_decrease_times = 0
    t1 = threading.Thread(target=increase, args=(var, lock))
    t2 = threading.Thread(target=decrease, args=(var, lock))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(var)
    print('total increase times: {}'.format(str(total_increase_times)))
    print('total decrease times: {}'.format(str(total_decrease_times)))
    end_time = time.time()
    print('total time is {}'.format(str(end_time - start_time)))
