## Async io

Link : https://realpython.com/async-io-python/

## Definition

**Coroutines** : specialized generator functions

**Parallelism** consists of performing multiple **operations** at the same time. 

**Multiprocessing** is a means to effect parallelism, and it entails **spreading tasks** over a computer’s 
central processing units (CPUs, or cores). 

**Concurrency** is a slightly broader term than parallelism. It suggests that **multiple tasks** have the ability to
run in an **overlapping** manner. (There’s a saying that concurrency does not imply parallelism.)

**Threading** is a **concurrent execution** model whereby multiple threads take turns executing tasks. One process 
can contain multiple threads.

To reiterate, async IO is a style of **concurrent programming**, but it is not parallelism. It’s more 
**closely aligned with threading** than with multiprocessing but is very much distinct from both of these and is a
**standalone member** in concurrency’s bag of tricks.

**Asynchronous** routines are able to **pause** while waiting on their ultimate result and let other routines
run in the meantime.
**Asynchronous** code, through the mechanism above, **facilitates concurrent execution**. To put it differently, 
asynchronous code gives the look and **feel of concurrency**.

## Example : 
Chess master Judit Polgár hosts a chess exhibition in which she plays multiple amateur players. She has two ways of conducting 
the exhibition: synchronously and asynchronously.

**Synchronous version(DFS)**: Judit plays one game **at a time**, never two at the same time, until the game is complete. 
Each game takes (55 + 5) * 30 == 1800 seconds, or 30 minutes. The entire exhibition takes 24 * 30 == 720 minutes, or 12 hours.

**Asynchronous version(BFS)**: Judit moves from table to table, **making one move at each table**. She leaves the table and
lets the opponent make their next move during the wait time. One move on all 24 games takes Judit 24 * 5 == 120 seconds, 
or 2 minutes. The entire exhibition is now cut down to 120 * 30 == 3600 seconds, or just 1 hour. 

So, cooperative multitasking is a fancy way of saying that a program’s **event loop** communicates with **multiple tasks**
to let each take turns running at the optimal time.

A **coroutine** is a function that can **suspend** its execution before reaching return, and it can indirectly **pass control** 
to another coroutine for some time.

```python
import asyncio
async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")

## Output 
# One
# One
# One
# Two
# Two
# Two
# countasync.py executed in 1.01 seconds.
```

Talking to each of the calls to count() is a **single event loop**, or coordinator. When each task reaches await 
asyncio.sleep(1), the function yells up to the event loop and gives control back to it, saying, 
**I’m going to be sleeping for 1 second. Go ahead and let something else meaningful be done in the meantime.**
Notice it took only **1 second** to complete all task.

## Rules 
1. The syntax **async def** introduces either a native coroutine or an asynchronous generator. The expressions **async with** 
   and **async for** are also valid.

2. The keyword **await passes function control back to the event loop**. (It **suspends** the execution of the surrounding   
   coroutine.) If Python encounters an await f() expression in the scope of g(), this is how await tells the event loop,
   “Suspend execution of g() until whatever I’m waiting on—the result of f()—is returned. In the meantime, go let 
   something else run.”

```python
async def g():
    # Pause here and come back to g() when f() is ready
    r = await f()
    return r
```

3. A function that you introduce with async def is a **coroutine**. It may use **await, return, or yield**, but all of these
   are optional. Declaring async def noop(): pass is valid
    1. Using await and/or return creates a coroutine function. To call a coroutine function, you must **await** it to get 
    its **results**.

    2. It is less common (and only recently legal in Python) to use **yield** in an async def block. This creates an 
    **asynchronous generator**, which you iterate over with async for.

    3. Anything defined with **async def may not use yield from**, which will raise a SyntaxError.

4. Just like it’s a **SyntaxError** to use yield outside of a def function, it is a SyntaxError to use 
   **await outside of an async** def coroutine. You can only use await in the body of coroutines.

```python
async def f(x):
    y = await z(x)  # OK - `await` and `return` allowed in coroutines
    return y

async def g(x):
    yield x  # OK - this is an async generator

async def m(x):
    yield from gen(x)  # No - SyntaxError

def m(x):
    y = await z(x)  # Still no - SyntaxError (no `async def` here)
    return y
```

TODO :: more details left out

----------------------------------------------------------

## Generator

Link : https://realpython.com/introduction-to-python-generators/#example-1-reading-large-files

Generator functions are a special kind of function that return a **lazy iterator**. These are objects that you can 
**loop over like a list**. However, unlike lists, lazy iterators **do not store** their contents in memory. 

A common **use case** of generators is to **work with data streams** or large files, like CSV files. 

**Example 1** to read one row at a time from the given file. This way only one row will occupy memory at a time.

```python
def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row
```

You can also define a **generator expression** (also called a generator comprehension), which has a very similar 
syntax to list comprehensions. In this way, you can use the **generator without calling a function**:

```python
csv_gen = (row for row in open(file_name))
```

This is a more **succinct(few words)** way to create the list csv_gen.

**Example 2**

Generating an **infinite sequence**, however, will require the use of a generator, since your **computer memory is finite**.

```python
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

for i in infinite_sequence():
    print(i, end=" ")
```

TODO :: more details left out

----------------------------------------------------------
