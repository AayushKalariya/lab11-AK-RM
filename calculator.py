#https://github.com/AayushKalariya/lab11-AK-RM
# Partner 1: Aayush Kalariya
# Partner 2: Rayan Mubarak

import math 

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    if a == 0:
        raise ZeroDivisionError
    return b/a

def logarithm(a, b): 
    if b == 0:
        raise ValueError
    if a == 1:
        raise ValueError
    return math.log(b,a)

def exp(a,b):
    return a**b

def square_root(a):
    if a < 0:
        raise ValueError 
    return math.sqrt(a)

def hypotenuse(a, b): 
    return math.hypot(a, b)