#Author Kristina Beresneva
#25.02.2022
#task: создать калькулятор
def plus(a, b):                       #определяем функции математических операций
    print ("Сумма: ", a, "+", b, "=", a + b)
def minus(a, b):
    print ("Разность: ", a, "-", b, "=", a - b)
def umnozh(a, b):
    print ("Произведение: ", a, "*", b, "=", a * b)
def div(a, b):
    print ("Частное: ", a, "/", b, "=", a / b)
def div1(a, b):
    print ("Целочисленное деление: ", a, "//", b, "=", a // b)
def stepen(a, b):
    print ("Возведение в степень: ", a, "**", b, "=", a ** b)
def ostat(a, b):
    print ("Остаток от деления: ", a, "%", b, "=", a % b)
    
while True:                  #проводим операции, пока пользователь не введет exit
    operation = input("Выберите операцию: +, -, *, /, //, **, % ")
    if operation == "exit":
        break
    num1 = int(input("Введите число: "))
    num2 = int(input("Введите число: "))
    if operation == "+":
        plus(num1, num2)
    elif operation == '-':
        minus(num1, num2)
    elif operation == '*':
        umnozh(num1, num2)
    elif operation == '/':
        div(num1, num2)
    elif operation == '//':
        div1(num1, num2)
    elif operation == '**':
        stepen(num1, num2)
    elif operation == '%':
        ostat(num1, num2)
    else:
        print("Неправильный ввод")
