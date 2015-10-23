# **multicpu**  ([中文版](http://blog.csdn.net/cyh_24/article/details/49314709))
Set the number of cpu and thread using ONE function:
>result = ***multi_cpu***(process_job, jobs, cpu_num, thread_num)

***cpu_num***: the number of cpu. <br>
***thread_num***: the number of thread in one cpu.

Installation
------------

Multicpu is conveniently available via pip:
```
pip install multicpu
```

or installable via `git clone` and `setup.py`
```
git clone git@github.com:cyh24/multicpu.git
sudo python setup.py install
```


Usage
-----
The multicpu library enables you to utilize the benefits of multi-cpu and multi-threading with minimal concern about the implementation details.

>***"Talk is cheap, show me your performance."***

Let's take a look at how simple it is to speed up an inefficient chunk of blocking code with minimal effort.


----------


Non-IO-Intensive Function 
-----------------
```
def process_job(job):
    time.sleep(1)
    return job

jobs = [i for i in range(20)]

```
IO-Intensive Function 
-----------------
```
def process_job(job):
    count = 100000000
    while count>0:
        count -= 1
    return job

jobs = [i for i in range(20)]

```

----------

Non-Thread
----------
```
if __name__ == "__main__":
    result = []
    for job in jobs:
        result.append(process_job(job))
```


Multi-thread
-----------------
```
from concurrent import futures

if __name__ == "__main__":
    result = []
    thread_pool = futures.ThreadPoolExecutor(max_workers=10)
    result = thread_pool.map(process_job, jobs)
```


----------


multicpu
-----------------
```
from multicpu import multi_cpu

if __name__ == "__main__":
    result = multi_cpu(process_job, jobs, 10, 1)
```

Performance
-----------------
| **Function** | **Non-Thread** | **Multi-Thread(10)** | **multicpu(10,1)**| **multicpu(10,2)** |
|:--------|:---------:|:-------:|:-------:|:-------:|
| IO | 146.42 (s) | 457.53 (s) | 16.34 (s) |42.81 (s)
| Non-IO | 20.02 (s) | 2.01 (s) | 2.02 (s) |1.02 (s)


How Does it Work?
-----------------

Feel free to read the source for a peek behind the scenes -- it's less than 60 lines of code.
