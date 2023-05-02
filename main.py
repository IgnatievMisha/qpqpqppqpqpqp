#1 decorators theory

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