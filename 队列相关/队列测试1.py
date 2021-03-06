import threading
import time


def write_to_queue(queue1):
    for index in range(5):
        print('write {} to {}'.format(str(index), queue1))
        queue1.put(index)
        time.sleep(1)


def read_from_queue(queue1):
    while True:
        result = queue1.get(True)
        print('get {} from {}'.format(str(result), queue1))


if __name__ == '__main__':
    print('main thread is {}'.format(threading.current_thread().name))
    start_time = time.time()
    from queue import Queue

    queue = Queue()
    tw = threading.Thread(target=write_to_queue, args=(queue,))
    tr = threading.Thread(target=read_from_queue, args=(queue,))
    # tr.setDaemon=True 设置为守护线程,当写入进程停止时，读进程也随之停止
    tr.daemon = True
    tw.start()
    tr.start()
    tw.join()
    end_time = time.time()
    print('total time is {}'.format(str(end_time - start_time)))
