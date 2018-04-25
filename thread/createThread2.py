'''
创建线程的另一种方式：
继承threading.Thread
'''
import threading
import time


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def getResult(self):
        return self.res

    def run(self):
        print('starting', self.name, 'at:', time.ctime())
        self.res = self.func(*self.args)
        print(self.name, 'finished at:', time.ctime())


def fib(n):
    '''
    斐波那契
    :param n:
    :return:
    '''
    # print(n)
    time.sleep(0.05)
    if n < 2: return 1
    return fib(n - 1) + fib(n - 2)


def fac(n):
    '''
    阶乘
    :param n:
    :return:
    '''
    time.sleep(0.05)
    if n < 2: return 1
    return n * fac(n - 1)


def sum(n):
    '''
    求和
    :param n:
    :return:
    '''
    time.sleep(0.05)
    if n < 2: return 1
    return n + sum(n - 1)


funcs = [fib, fac, sum]
# -------------single---------------------------------------------
# for func in funcs:
# print('starting', func.__name__, 'at:', time.ctime())
# func(10)
# print(func.__name__, 'finished at:', time.ctime())
# --------------end single------------------------------------------------

# -------------multi----------------------------------------------
threads = []
for func in funcs:
    threads.append(MyThread(func, (10,), func.__name__))
for t in threads:
    t.start()
for t in threads:
    t.join()
# ------------end multi--------------------------------------------
