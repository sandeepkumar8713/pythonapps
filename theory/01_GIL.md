# Python Notes

## Thread
1. A **thread** is a **stream of instructions** within a process. 
2. Each thread has its own **instruction pointer, set of registers and stack memory**. 
3. The **virtual address space** is process specific, or common to all threads within a process. 
4. So, data on the heap can be readily accessed by all threads, for good or ill.
5. Multi-threading is a more **light weight form of concurrency**: there is **less context** per thread than per process. 
6. As a result thread lifetime, context switching and synchronisation **costs are lower**. The shared
address space (noted above) means data sharing requires **no extra work**.

## Process
1. **Multi-processing** has the opposite benefits. Since processes are **insulated from each other by the OS**. 
2. An error in one process **cannot bring down another process**. 
3. Contrast this with multi-threading, in which an error in one thread can bring **down all the threads in the process**. 
4. Further, individual processes may run as **different users and have different permissions**. 
5. When we open a **new tab in browser a new process** is created. So that 1 tab crash should not stop browser.

## GIL 
Link : https://realpython.com/python-gil/

1. The **Python Global Interpreter** Lock or GIL, in simple words, is a mutex (or a lock) that allows only one thread to hold
   the control of the Python interpreter.
2. This means that only one thread can be in a **state of execution** at any point in time. The impact of the GIL isn’t 
   visible to developers who execute single-threaded programs, but it can be a performance bottleneck in **CPU-bound** and multi-threaded code.
3. Since the GIL allows only one thread to execute at a time even in a multi-threaded architecture with more 
  **than one CPU core**, the GIL has gained a reputation as an **“infamous”** feature of Python.

## Reason
1. Python uses **reference counting** for memory management. It means that objects created in Python have a reference count
   variable that keeps track of the number of references that point to the **object**. When this count reaches zero, the
   memory occupied by the object is **released**.

```python
import sys
a = []
b = a
sys.getrefcount(a) # Output 3, The list object was referenced by a, b and the argument passed to sys.getrefcount().
```

2. The problem was that this reference count variable needed **protection from race conditions** where two threads increase
   or decrease its value simultaneously. If this happens, it can cause either **leaked memory** that is never released or,
   even worse, incorrectly release the memory while a reference to that object still exists.

3. This reference count variable can be kept safe by adding locks to **all data structures** that are shared across threads
   so that they are not modified inconsistently. But adding a lock to each object or groups of objects means **multiple locks** 
   will exist which can cause another problem— **Deadlocks** (deadlocks can only happen if there is more than one lock). 
   Another side effect would be **decreased performance** caused by the repeated acquisition and release of locks.

4. The GIL is a **single lock on the interpreter** itself which adds a rule that execution of any **Python bytecode** requires 
   acquiring the interpreter lock. This prevents deadlocks (as there is only one lock) and doesn’t introduce much 
   performance overhead. But it effectively makes any **CPU-bound** Python program single-threaded.

5. Python has been around since the days when operating systems did not have a concept of threads. Python was designed to be 
   easy-to-use in order to make development quicker and more and more developers started using it.  A lot of extensions 
   were being written for the **existing C libraries** whose features were needed in Python. To prevent inconsistent changes, 
   these C extensions required a **thread-safe memory management** which the GIL provided. C libraries that were not
   thread-safe became easier to integrate. And these C extensions became one of the reasons why Python was readily
   adopted by different communities.

## Remove GIL
1. The GIL does not have much impact on the performance of **I/O-bound** multi-threaded programs as the lock is shared
   between threads while they are waiting for I/O.
2. But a program whose threads are **entirely CPU-bound**, e.g., a program that processes an image in parts using threads, 
   would not only become single threaded due to the lock but will also see an increase in execution time, as seen in the 
   above example, in comparison to a scenario where it was written to be entirely single-threaded. 
3. The GIL can obviously be removed and this has been done multiple times in the past by the developers and researchers but all 
   those attempts **broke the existing C extensions** which depend heavily on the solution that the GIL provides.
4. Of course, there are other solutions to the problem that the GIL solves but some of them decrease the performance of 
   single-threaded and multi-threaded I/O-bound programs and some of them are just too difficult. After all, 
   you wouldn’t want your existing Python programs to run slower after a new version comes out, right?

## But Python 3 did bring a major improvement to the existing GIL—
1. We discussed the impact of GIL on “only CPU-bound” and “only I/O-bound” multi-threaded programs but what about the programs 
   where some threads are I/O-bound and some are CPU-bound?
2. In such programs, Python’s GIL was known to **starve the I/O-bound threads** by not giving them a chance to acquire the GIL 
   from CPU-bound threads.
3. This was because of a mechanism built into Python that forced threads to release the GIL after a **fixed interval** of 
   continuous use and if nobody else acquired the GIL, **the same thread** could continue its use.

## Alternative 
**Multi-processing vs multi-threading**: The most popular way is to use a multi-processing approach where you use multiple 
processes instead of threads. Each Python process gets its own Python interpreter and memory space so the GIL won’t be a problem. 
Python has a multiprocessing module which lets us create processes easily like this.

```python
import time
from threading import Thread
COUNT = 50000000

def countdown(n):
    while n>0:
        n -= 1

t1 = Thread(target=countdown, args=(COUNT//2,))
t2 = Thread(target=countdown, args=(COUNT//2,))

start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()

print('Time taken in seconds -', end - start)
```

## Asyncio
1. asyncio (this technique is available not only in Python, other languages and/or frameworks also have it, e.g. Boost.ASIO)
  is a method to effectively handle a **lot of I/O operations** from many simultaneous sources **without need of parallel code** 
  execution. So it's just a solution (a good one indeed!) for a particular task, **not for parallel processing in general**.

2. asyncio is essentially threading where not the CPU but you, as a programmer (or actually your application), 
  **decide where and when does the context switch happen**. In Python you use an **await** keyword to suspend the execution
  of your coroutine (defined using async keyword).

3. asyncio is often a perfect fit for **IO-bound and high-level structured network code**.

asyncio provides a set of **high-level APIs** to:
1. run Python coroutines concurrently and have full control over their execution;
2. **perform network IO and IPC**;
3. **control subprocesses**;
4. **distribute tasks via queues**;
5. **synchronize concurrent code**;

Additionally, there are **low-level APIs** for library and framework developers to:
1. create and manage event loops, which provide asynchronous APIs for networking, running subprocesses, handling OS signals, etc;
2. implement efficient protocols using transports;
3. bridge callback-based libraries and code with async/await syntax.

4. https://superfastpython.com/asyncio-vs-threading/
   1. The Python language was changed to accommodate asyncio with the addition of expressions and types.
   2. More specifically, it was changed to support coroutines as first-class concepts. In turn, coroutines are the unit of 
      concurrency used in asyncio programs.
   3. A coroutine is a function that can be **suspended and resumed**.
   4. **Coroutines** are a more generalized form of subroutines. Subroutines are entered at one point and exited at another 
       point. Coroutines can be entered, exited, and resumed **at many different points**. — Python Glossary
   5. A coroutine may suspend for many reasons, such as executing another coroutine, e.g. awaiting another task, or waiting
      for some external resources, such as a socket connection or process to return data.
   6. Many coroutines can be **created and executed at the same time**. They have control over when they will suspend and
      resume, allowing them to cooperate as to when concurrent tasks are executed.
