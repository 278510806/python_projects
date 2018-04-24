'''
下面的代码在说明：python的多线程比单线程还弱！！
对于计算密集型的任务，多线程要比单线程性能低45%左右
因此python的多线程只适合于io密集型任务，而且，多个线程
都应该是io密集的，两种任务不能混合，否则io密集型任务
只能等待计算密集型任务执行完才可以获得cpu执行

---------------------摘自网络-------------------------
任何一个线程被唤起时都能成功获得到GIL（因为只有释放了GIL才会引发线程调度）。
但当CPU有多个核心的时候，问题就来了。从伪代码可以看到，从release GIL到
acquire GIL之间几乎是没有间隙的。所以当其他在其他核心上的线程被唤醒时，
大部分情况下主线程已经又再一次获取到GIL了。这个时候被唤醒执行的线程只能
白白的浪费CPU时间，看着另一个线程拿着GIL欢快的执行着。然后达到切换时间
后进入待调度状态，再被唤醒，再等待，以此往复恶性循环。
------------------------------------------------------------
'''
import threading
import time
def task():
    i=0
    for i in range(100000000):
        i+=1
    return True

def single():
    '''
    为了减少线程库本身性能损耗对测试结果带来的影响，这里单线程的代码同样使用了线程。只是顺序的执行两次，模拟单线程。
    :return:
    '''
    beginTime=time.time()
    for i in range(2):
        t=threading.Thread(target=task)
        t.start()
        t.join()
    endTime=time.time()
    print('result:{}'.format(endTime-beginTime))
def multi():
    '''
    多线程
    :return:
    '''
    lst={}
    beginTime=time.time()
    for tid in range(2):
        t=threading.Thread(target=task)
        t.start()
        lst[tid]=t
    for i in range(2):
        lst[i].join()
    endTime=time.time()
    print('result:{}'.format(endTime-beginTime))

if __name__=='__main__':
    multi()
