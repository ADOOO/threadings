#coding=utf-8

import time 
import threading 
import Queue


class BaiduScan(threading.Thread): 
    def __init__(self, queue): 
        threading.Thread.__init__(self)
        self._queue = queue 

    def run(self):
        while not self._queue.empty():
            try:
                msg = self._queue.get_nowait() 
                #print 'msg is :%d'%msg
                self.url(msg)
            except Exception,e:
                print e
                break
    def url(self,msg):
        print 'AAAA+%s'%(msg)


def main():
    queue = Queue.Queue()
    for i in range(20):
        queue.put(i)

    threads = []
    for i in xrange(threads_count):
        threads.append(BaiduScan(queue))

    for t in threads:
        t.start()

    for t in threads:
        t.join()

if __name__ == '__main__':
    threads_count = 10
    main()
