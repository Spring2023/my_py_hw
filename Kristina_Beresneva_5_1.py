#Author Kristina Beresneva
#28.02.2022
#task: посчитать факториал числа

n = int(input())   #спрашиваем число

def factorial(n):   #создаем функцию для подсчета факториала
    if n < 0:
        return None
    if n < 2:
        return 1
    else:
        factor_val = 1
        for i in range(2, n+1):
            factor_val *= i
        return factor_val
print(factorial(n))    #выводим результат

for n in range(-1, 9):   #для проверки правильности
    print(factorial(n))

  
   
        
        
    
    
        







