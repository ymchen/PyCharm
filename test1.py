#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: YiMin-Chan|cyimin@tianjianpro.com
# @Date:   2022-06-06 10:40:16
# @version:  1.0.0
# @filename:  队列测试2
# @file_path:  D:\ChenYiMin\TJFJ\PYTHON_EXP1\PYTHON_3_LEARN\python队列\队列测试2.py
# @Last Modified by:   YiMin-Chan
# @Last Modified time: 2022-06-06 10:47:33
import time
from multiprocessing import Process, Queue


def write_to_queue(queue):
    for index in range(5):
        print('write {} to {}'.format(str(index), queue))
        queue.put(index)
        time.sleep(1)


def read_from_queue(queue):
    while True:
        result = queue.get(True)
        print('get {} from {}'.format(str(result), queue))


if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write_to_queue, args=(q,))
    pr = Process(target=read_from_queue, args=(q,))
    # 启动子进程pw，写入:
    pr.daemon = True
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    # pr.terminate()
