# def my_decorator(func):
#     def wrapper(name):
#         print("operations before the function")
#         func(name)
#         print("operations after the function")
#     return wrapper

# @my_decorator    
# def sayHello(name):
#     print("hello",name)    

# sayHello("ali")
import math
import time

def calculate_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        time.sleep(1)

        func(*args, **kwargs)

        finish = time.time()
        print("Function " + func.__name__ +  str(finish - start ) + " seconds")
    return inner    

@calculate_time
def exponentiation(a,b):    
    print(math.pow(a,b))

    
@calculate_time
def factorial(num):   
    print(math.factorial(num))

@calculate_time
def adding(a,b):
    print(a + b)    

exponentiation(2,3)
factorial(4)
adding(10 , 20)