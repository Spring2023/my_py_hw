#1.
try:
    print("Let's try to do this")
    print("#"[2])
    print("We succeded!")
except:
    print("We failed")
print("We're done")

#2.
try:
    print("alpha"[1/0])
except ZeroDivisionError:
    print("zero")
except IndexingError:
    print("index")
except:
    print("some")

#3.
try:
    y = 1 / 0
except ZeroDivisionError:
    print("Oooppsss...")
    
print("THE END.")

try:
    y = 1 / 0
except ArithmeticError:
    print("Oooppsss...2")

print("THE END.2")

#4.
try:
    y = 1 / 0
except ZeroDivisionError:
    print("Zero Division!")
except ArithmeticError:
    print("Arithmetic problem!")

print("THE END.")


try:
    y = 1 / 0
except ArithmeticError:
    print("Arithmetic problem!")
except ZeroDivisionError:
    print("Zero Division!")

print("THE END.")

#5.
def bad_fun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("Arithmetic Problem!")
    return None

bad_fun(0)

print("THE END.")

def bad_fun1(n):
    return 1 / n

try:
    bad_fun1(0)
except ArithmeticError:
    print("What happend? An exception was raised!")

print("THE END.")

#6.
def bad_fun(n):
    raise ZeroDivisionError
        
try:
    bad_fun(0)
except ArithmeticError:
    print("What happend? An error?")

print("THE END.")

#7.
def bad_fun(n):
    try:
        return n / 0
    except:
        print("I did it again!")
        raise
        
try:
    bad_fun(0)
except ArithmeticError:
    print("I see!")

print("THE END.")

#8.
import math

x = float(input("Enter a number: "))
assert x >= 0.0

x = math.sqrt(x)

print(x)

#9.
try:
    print(1 / 0)
except ZeroDivisionError:
    print("Zero")
except ArithmeticError:
    print("arith")
except:
    print("some")

try:
    print(1 / 0)
except ArithmeticError:
    print("arith")
except ZeroDivisionError:
    print("zero")
except:
    print("some")

#10.
def foo(x):
    assert x
    return 1 / x

try:
    print(foo(0))
except ZeroDivisionError:
    print("zero")
except:
    print("some")

#11.
from math import tan, radians
angle = int(input('Enter integral angle in degrees: '))
assert angle % 180 != 90
print(tan(radians(angle)))

#12.
from time import sleep

seconds = 0
while True:
    try:
        print(seconds)
        seconds += 1
        sleep(1)
    except KeyboardInterrupt:
        print("Don't do that!")

#13.
string = 'x'
try:
    while True:
        string = string + string
        print(len(string))
except MemoryError:
    print('This is not funny!')

#14.
from math import exp

ex = 1

try:
    while True:
        print(exp(ex))
        ex *= 2
except OverflowError:
    print('The number is too big.')

#15.
try:
    import math
    import time
    import abracadabra

except:
    print('One of your imports has failed.')

