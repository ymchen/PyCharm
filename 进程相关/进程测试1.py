#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: YiMin-Chan|cyimin@tianjianpro.com
import os
import time
from multiprocessing import Process


def func():
    print('process {} starts'.format(os.getpid()))
    time.sleep(2)
    print('process {} ends'.format(os.getpid()))


if __name__ == '__main__':
    print('main process is {}'.format(os.getpid()))
    start_time = time.time()
    p1 = Process(target=func)
    p2 = Process(target=func)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end_time = time.time()
    print('total time is {}'.format(str(end_time - start_time)))
