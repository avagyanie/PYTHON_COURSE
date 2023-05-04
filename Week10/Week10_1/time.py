
import time
from functools import wraps

# version 1
def outer():
    startTime = time.perf_counter()
    def inner():
        time.sleep(5)
        return 'test'
    inner()
    endTime = time.perf_counter()
    difference = endTime - startTime
    return f'{difference:.4f}'


# version 2
def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper


@timeit
def goSleep(num):
    time.sleep(num)
    return 'Go to sleep'


# version 3

def decor(func):
    def inner(*args, **kwargs):
        print(time.perf_counter())
        result = func(*args, **kwargs)
        print(time.perf_counter())
        return result

    return inner


def ordinary():
    time.sleep(3)
    return "test"

if __name__ == '__main__':
    test = outer()
    print(test)
    goSleep(5)
    goSleep(7)
    goSleep(9)
    goSleep(10)
    test2 = decor(ordinary)
    test2()


