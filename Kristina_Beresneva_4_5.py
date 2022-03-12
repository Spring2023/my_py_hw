#Author Kristina Beresneva
#25.02.2022
#task: вывести простое число или нет
num = int(input("Введите число: "))  #спрашиваем число
def is_prime(num):                   #определяем условия функции
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5 + 1)):
        if num % i == 0:
            return False
    else:
        return True
print(is_prime(num))                 #выводим результат

for i in range(1, 20):               #выводим все простые числа в заданном диапозоне
    if is_prime(i + 1):
        print(i + 1, end=" ")        
