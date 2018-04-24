'''
通过一个示例演示线程的创建
'''

import threading
import time


def task(num, name):
    '''
    获取给定整数的所有素数
    :param num:
    :param name:
    :return:
    '''
    lst = []
    i = 2
    beginTime = time.time()
    while True:
        if i == num // 2+1:
            break
        m = num % i
        if m == 0:
            lst.append(i)
        i += 1
    endTime = time.time()
    print('%s:%d' % (name, endTime - beginTime), lst)


if __name__ == '__main__':
    lst = []
    for i in range(3):
        t = threading.Thread(target=task, args=(12345678, i))
        lst.append(t)
    for t in lst:
        t.start()
    for t in lst:
        t.join()
