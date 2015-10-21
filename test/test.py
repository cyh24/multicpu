import time
import requests

import numpy as np
import multiprocessing
from concurrent import futures

from multicpu import multi_cpu

def process_job(job):
    #time.sleep(1)
    count = 10000000
    while count>0:
        count -= 1
    return job


jobs = [i for i in range(10)]

def test_multi_cpu_thread(cpu_num, thread_num):
    print "multi_cpu_thread: cpu_num=%d, thread_num=%d"%(cpu_num, thread_num)
    result = multi_cpu(process_job, jobs, cpu_num, thread_num)
    print result

def test_multi_cpu(cpu_num):
    print "multi_cpu: cpu_num=", cpu_num
    cpu_pool = multiprocessing.Pool(processes=cpu_num)
    result = cpu_pool.map(process_job, jobs)
    print result

def test_multi_thread(thread_num):
    print "multi_thread: thread_num=", thread_num
    thread_pool = futures.ThreadPoolExecutor(max_workers=thread_num)
    result = thread_pool.map(process_job, jobs)
    print [r for r in result]

def test_no_thread():
    print "no thread."
    result = []
    for job in jobs:
        result.append(process_job(job))
    print result


def aa():
    start = time.time()
    test_no_thread()
    end = time.time()
    print "Time: %f seconds\n" % (end - start)

    start = time.time()
    test_multi_thread(5)
    end = time.time()
    print "Time: %f seconds\n" % (end - start)

    start = time.time()
    test_multi_cpu(5)
    end = time.time()
    print "Time: %f seconds\n" % (end - start)

if __name__ == "__main__":
    start = time.time()
    test_multi_cpu_thread(3, 1)
    end = time.time()
    print "Time: %f seconds\n" % (end - start)
