
import time
from functools import wraps
from functools import lru_cache

def clock(func):
   def clocked(*args):
       t0 = time.perf_counter()
       result = func(*args) 
       elapsed = time.perf_counter() - t0
       name = func.__name__
       arg_str = ', '.join(repr(arg) for arg in args)
       print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
       return result
   return clocked

@lru_cache
def fib(n):
    # 1, 2, 3, 5, 8, 13,...
    if n==0:
        return 1
    elif n==1: 
        return 2
    else:
        return fib(n-1) + fib(n-2)

def new_fib(n):
    a,b = 1,2
    for _ in range(n):
        b, a = a+b, b
    return a

def time_fib(n):
    t0 = time.perf_counter()
    result = fib(n)
    elapsed = time.perf_counter()-t0    
    name = fib.__name__
    arg_str = n
    print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))

def time_new_fib(n):
    t0 = time.perf_counter()
    result = new_fib(n)
    elapsed = time.perf_counter()-t0    
    name = new_fib.__name__
    arg_str = n
    print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))

if __name__ == "__main__":
    # for n in range(4):
    #     time_fib(n)
    val = 35
    time_fib(val)
    time_new_fib(val)
