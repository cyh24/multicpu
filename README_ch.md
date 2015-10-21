# **multicpu**

使用multicpu之后，你需要一个函数，就可以定义你程序运行时所需的**CPU数量**和每个cpu占用的**线程数量**：
>result = ***multi_cpu***(process_job, jobs, cpu_num, thread_num)

***cpu_num***: 使用的CPU数量. <br>
***thread_num***: 每个cpu占用的**线程数量**.

安装指南
------------

***multicpu*** 可以直接使用pip就可以安装了
```
pip install multicpu
```
或者，你也可以用`git clone` 下载源代码，然后用`setup.py`安装:
```
git clone git@github.com:cyh24/multicpu.git
sudo python setup.py install
```


>***"Talk is cheap, show me your performance."***

因为源代码才**60行**不到，所以，你自己去看完全不会有卡住的地方，这里简单粗暴地直接上代码：


----------


如果你的程序是 **不是IO密集型**
-----------------
```
import time

def process_job(job):
    time.sleep(1)
    return job

jobs = [i for i in range(20)]

```
如果你的程序 **IO密集型**
-----------------
```
import time

def process_job(job):
    count = 100000000
    while count>0:
        count -= 1
    return job

jobs = [i for i in range(20)]

```

----------

没有使用任何多线程处理的方法：
----------
```
import time

if __name__ == "__main__":
    result = []
    for job in jobs:
        result.append(process_job(job))
```


使用了python的线程池：
-----------------
```
import time
from concurrent import futures

if __name__ == "__main__":
    result = []
    thread_pool = futures.ThreadPoolExecutor(max_workers=10)
    result = thread_pool.map(process_job, jobs)
```


----------


使用**multicpu**：
-----------------
```
import time
from concurrent import futures

if __name__ == "__main__":
    result = multi_cpu(process_job, jobs, 10, 1)
```

效果：
-----------------
| **Function** | **Non-Thread** | **Multi-Thread(10)** | **multicpu(10,1)**| **multicpu(10,2)** |
|:--------|:---------:|:-------:|:-------:|:-------:|
| IO | 146.42 (s) | 457.53 (s) | 16.34 (s) |42.81 (s)
| Non-IO | 20.02 (s) | 2.01 (s) | 2.02 (s) |1.02 (s)


How Does it Work?
-----------------

Feel free to read the source for a peek behind the scenes -- it's less than 60 lines of code.


