#3.1 task: найти наибольшее из 4 чисел
a = int(input("Введите число: "))  #спрашиваем у пользователя число
b = int(input("Введите число: "))
c = int(input("Введите число: "))
d = int(input("Введите число: "))
if a > b:                           #сравниваем числа
    if a > c:
        if a > d:
            print("Наибольшее число:", a, type(a))   #выводим результат
elif b > c:
    if b > d:
        print("Наибольшее число:", b, type(b))
elif c > d:
    print("Наибольшее число:", c, type(c))
else:
    print("Наибольшее число:", d, type(d))

#3.2 task: найти наибольшее и наименьшее из 6 чисел
a = int(input("Введите число: "))    #спрашиваем у пользователя число
b = int(input("Введите число: "))
c = int(input("Введите число: "))
d = int(input("Введите число: "))
e = int(input("Введите число: "))
f = int(input("Введите число: "))
x = max(a, b, c, d, e, f) #пробуем готовую функцию
print (x)                 #выводим результат
y = min(a, b, c, d, e, f) #пробуем готовую функцию
print (y)

if a > b:          #наша программа
    if a > c:
        if a > d:
            if a > e:
                if a > f:
                    print("Наибольшее число:", a, type(a))
elif b > c:
    if b > d:
        if b > e:
            if b > f:
                print("Наибольшее число:", b, type(b))
elif c > d:
    if c > e:
        if c > f:
            print("Наибольшее число:", c, type(c))
elif d > e:
    if d > f:
        print("Наибольшее число:", d, type(d))
elif e > f:
    print("Наибольшее число:", e, type(e))
else:
    print("Наибольшее число:", f, type(f))

#3.3 task: спросить у пользователя название цветка (название цветка должно быть с большой буквы)
flower = str(input("Введите название цветка: "))     #спрашиваем у пользователя
if flower == "Spathiphyllum":                        #проверяем условия
    print("Yes - Spathiphyllum is the best plant ever!")    #выводим результат
elif flower == "spathiphyllum":
    print("No, I want a big Spathiphyllum")
else:
    print("Spathiphyllum!", "Not", flower, "!")

#3.4 task: создать калькулятор налогов
money = float(input("Введите доходы: "))    #спрашиваем у пользователя доходы
tax = round(money / 100 * 15)  #для примера с округлением
cash = money - tax
if money > 0:
    if money < 100:
        print (tax)   #выводим налоги
        print (cash)  #выводим остаток после налогов
    elif money > 100:
        print (cash)
        print (tax)
else:
    if money < 0:
        print ("Nothing")
    if money == 0:
        print ("Nothing")

#3.5 task: необходимо определить год високосный или нет
year = int(input("Введите год: "))    #справшиваем год
if year > 1800 and year < 2022:       #проверяем валидность
    if year % 4 != 0:                 #проверяем условия
        print ("Common year")   
    elif year % 100 != 0:
        print ("Leap year")
    elif year % 400 != 0:
        print ("Common year")
    else:
        print ("Leap year")
else:
    print ("Not within the Gregorian calendar period")  #выводим результат

#3.6 task: необходимо спрашивать число до тех пор, пока пользователь его не угадает
secret = 1409
num = int(input("Введите число: "))   #спрашиваем число
while num != secret:                   #проходим цикл, пока не угадает
    print ("Ha ha! You're stuck in my loop!")
    num = int(input("Введите число: "))
if num == secret:
    print (num, "Well done, muggle! You are free now", sep="\n")  #выводим результат

#3.7 task: посчитать до 5 миссиссиппи с интервалом в секунду
import time   
for i in range (1, 6):     #считаем от 1 до 5
    print (i, "Mississippi")
    time.sleep(1)           #временной интервал 1 секунда
print ("Ready or not, here I come")

#3.8 task: запрашивать у пользователя слово, пока не угадает "chupacabra"
word = str(input("Введите слово: "))    #спрашиваем слово
while word != "chupacabra":             #проходим цикл, пока не угадает
    word = str(input("Введите слово: "))
    continue
print("You're successfully left the loop!")   #выводим результат

#3.9 task: исключить гласные буквы из слова
user_word = (str(input("Введите слово: ")))  #спрашиваем слово
user_word = user_word.upper()                #делаем буквы слова большими
for i in user_word:                          #удаляем гласные
    if i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
        continue
    else:
        print (i)                            #выводим результат

#3.10 task: вывести в одну строку слово без гласных
user_word = (str(input("Введите слово: ")))   #спрашиваем слово
user_word = user_word.upper()                 #делаем буквы слова большими
resStr = str()
for i in user_word:                           #удаляем гласные
    if i == "A" or i == "E" or i == "I" or i == "O" or i == "U":    
        continue
    else:
        resStr += i
print (resStr)                                #выводим результат

#3.11 task: создать последовательность Коллаца
c0 = 15
while c0 != 1:               #пока число не 1, продолжаем цикл
    if c0 % 2 == 0:
        c0 = c0 // 2
        print (c0)
    else:
        c0 = 3 * c0 + 1
        print (c0)

#3.12 task: пока пользователь не введет "exit" проводить математические операции
a = int(input("Введите число: "))           #спрашиваем число
b = int(input("Введите число: "))           #спрашиваем число
operation = input("choose: +, -, *, **, /, //, %: ")           #предлагаем выбрать операцию
while operation != "exit":                  #проходим цикл, пока не введет "exit"
    if operation == "+":
        print (a + b)
    if operation == "-":
        print (a - b)
    if operation == "*":
        print (a * b)
    if operation == "/":
        print (a / b)
    if operation == "//":
        print (a // b)
    if operation == "%":
        print (a % b)
    operation = (input("choose: +, -, *, **, /, //, %: "))
    continue
