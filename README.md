# **multicpu**
Set the number of cpu and thread using ONE function:
>result = ***multi_cpu***(process_job, jobs, cpu_num, thread_num)

cpu_num: the number of cpu.
thread_num: the number of thread in one cpu.

Installation
------------

Tomorrow is conveniently available via pip:
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


IO-Intensive Function (Naive) 
-----------------
```
import time

def process_job(job):
    count = 10000000
    while count>0:
        count -= 1
    return job

jobs = [i for i in range(10)]

if __name__ == "__main__":
    result = []
    for job in jobs:
        result.append(process_job(job))
```

Output:
>Time:  **7.70** seconds
>result: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


----------


IO-Intensive Function (Multi-thread) 
-----------------
```
import time
from concurrent import futures

def process_job(job):
    count = 10000000
    while count>0:
        count -= 1
    return job

jobs = [i for i in range(10)]

if __name__ == "__main__":
    result = []
    thread_pool = futures.ThreadPoolExecutor(max_workers=5)
    result = thread_pool.map(process_job, jobs)
```
Output:
>Time:  **22.50** seconds
>result: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


----------


IO-Intensive Function (**multicpu**) 
-----------------
```
import time
from concurrent import futures

def process_job(job):
    count = 10000000
    while count>0:
        count -= 1
    return job

jobs = [i for i in range(10)]

if __name__ == "__main__":
    result = multi_cpu(process_job, jobs, 5, 1)
```
Output:
>Time:  **2.26** seconds
>result: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


How Does it Work?
-----------------

Feel free to read the source for a peek behind the scenes -- it's less than 50 lines of code.

