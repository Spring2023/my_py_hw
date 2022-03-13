#Author Kristina Beresneva
#28.02.2022
#task: вывести числа Фибоначчи
n = int(input())   #спрашиваем число

def fib(n):        #создаем функцию
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n+1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum

for n in range(0, n):
    print(fib(n))    #выводим результат

for n in range(-1, 25):    #для примера
    print(fib(n))

for n in range(1, 10):      #для примера
    print(n, "->", fib(n))

  
   
        
        
    
    
        







