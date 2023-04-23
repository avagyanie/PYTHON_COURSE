"""
Write function which take a function as an input and run it and print how count how many times 
I have run the input provide functions.
"""



def outer(func):
    count = 0
    def inner(*args):
        nonlocal count
        count += 1
        print(f"Function has been called {count} times.")
        return func(*args)
    
    return inner

def my_func(*args):
    return args

result = outer(my_func)
result(1, 2, 3)
result(1, 2)
result(1)
result(0)
