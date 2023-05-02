#1 decorators theory
import time

def my_decorator_func(func): #3
    def wrapper(): #4
        print("blablabla")
        func()
        print("bububu")
    return wrapper


@my_decorator_func #2
def say_hello(): #1
    print("Hello")
say_hello()

#____________________________________________________

def delay_decorator(func):
    def wrapper(*args, **kwargs):
        time.sleep(3)
        return func(*args, **kwargs)
    return wrapper


@delay_decorator
def sleepy():
    print("i`m sleep")
sleepy()