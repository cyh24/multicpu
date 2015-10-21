import multiprocessing
from concurrent import futures

class Multicpu():

    def __init__(self, cpu_num, thread_num):
        self.cpu_num    = cpu_num
        self.thread_num = thread_num

    
    def _multi_cpu(self, func, job_queue):
        if getLen(job_queue) == 0:
            return []
        index = get_index(job_queue, self.cpu_num)

        cpu_pool = multiprocessing.Pool(processes=self.cpu_num)
        result_queue = cpu_pool.map(_multi_thread, [ [func, self.cpu_num, self.thread_num, job_queue[idx[0]: idx[1]+1]] for idx in index])

        result = []
        for rl in result_queue:
            for r in rl:
                result.append(r)
        return result 


def _multi_thread(argv):
    thread_num = argv[2]
    if getLen(argv[3]) < thread_num:
        thread_num = argv[3]
    thread_pool = futures.ThreadPoolExecutor(max_workers=thread_num)

    result = thread_pool.map(argv[0], argv[3])
    
    return [ r for r in result]

def get_index(job_queue, split_num):
    job_num = getLen(job_queue)

    if job_num < split_num:
        split_num = job_num
    each_num = job_num/split_num
    
    index = [ [i*each_num, i*each_num+each_num-1] for i in range(split_num)]
    
    residual_num = job_num%split_num
    for i in range(residual_num):
        index[split_num - residual_num + i][0] += i
        index[split_num - residual_num + i][1] += i+1
    
    return index


def getLen(_list):
    if _list == None:
        return 0
    return len(_list)
    

def multi_cpu(func, job_queue, cpu_num=1, thread_num=1):
    multicpu_instance = Multicpu(cpu_num, thread_num)

    return multicpu_instance._multi_cpu(func, job_queue) 
