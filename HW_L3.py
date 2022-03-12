#3.1 task: провести манипуляции со списком
hat_list = [1, 2, 3, 4, 5]
print (len(hat_list))   #вывести длину списка
num = int(input("Введите число: ")) #спрашиваем число
hat_list[2] = num           #меняем число в списке на введенное
print (hat_list)            #вывести новый список
del hat_list[-1]            #удаляем последний элемент списка
print (hat_list)            #вывести новый список
print (len (hat_list))      #вывести длину нового списка

#3.2 task: создать список участников группы и добавлять/удалять их
beatles = []           #создать пустой список
print (beatles)        #вывести пустой список
beatles.append ("JohnLennon")   #добавить в пустой список
beatles.append ("Paul McCartney")
beatles.append ("George Harrison")
print (beatles)          #вывести новый список
for i in range (2):
    beatles.append (str(input("Введите имя: "))) #добавить еще участников
print (beatles)
del beatles [3: 5]     #удалить двух последних
print (beatles)
beatles.insert (0, "Ringo Starr")  #вставить нового участника в начало списка
print (beatles)
print (len(beatles), type(beatles))  #вывести длину списка и тип

#3.3 task: отсортировать список
n = int(input("Введите количество чисел: "))  #спрашиваем количество чисел
list = []                                   #создаем пустой список

if n > 0:                                  
    for i in range(n):
        a = int(input("Введите число: "))   #спрашиваем число
        list.append (a)                     #добавляем число в список
    print (list)                            #выводим список

swapped = True

while swapped:                            #сортируем список
    swapped = False
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            swapped = True
            list[i], list[i + 1] = list[i + 1], list[i]        
print (list)                            #выводим готовый список
list.sort()                             #пробуем готовую функцию
print (list)

#3.4 task: создать список с уникальными значениями
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]  #дан список
new_list = []                #создаем пустой список
for i in my_list:
    if i in new_list:           #проверяем есть ли значение в списке
        continue
    else:
        new_list.append(i)      #добавляем уникальные значения в новый список
print ("The list with unique elements only:", new_list)  #выводим результат

#3.5 task: вывести сумму введенных чисел
s = input("Введите числа через пробел: ")  #спрашиваем числа
l1 = s.split(" ")                #используем разделитель
print (l1)
numbers = []                  #создаем пустой список
for i in l1:                  #добавляем каждое число в список
    numbers.append(int(i))
print (numbers)
print ("Сумма чисел равна:",sum(numbers)) #выводим сумму чисел

#3.6 task: создать второй список чисел, которые встречаются не один раз в первом списке
s = input()  #вводим числа
l1 = s.split(" ")           #используем разделитель
l2 = []                      #создаем пустой список
for i in l1:                   #ищем повторяющиеся
    if l1.count(i) > 1 and i not in l2:
        l2.append(i)
print (" ".join(map(str,l2)))  #выводим результат

#3.7 task: вывести среднее арифметическое введенных чисел
s = input()  #вводим числа через пробел
print (s)
l1 = s.split(" ")                #добавляем разделитель
print (l1)
numbers = []                  #создаем пустой список
for i in l1:                  #добавляем каждое число в список
    numbers.append(int(i))
print (numbers)
print (sum(numbers) / len(numbers))    #выводим среднее арифметическое

#3.8 task: спросить 2 числа, вывести числа, делящиеся на 3, из последовательности двух введенных
a = int(input())     #спрашиваем число
b = int(input())      #спрашиваем число
l = []                #создаем пустой список
for i in range(a, b + 1):   #добавляем подходящие числа в список
    if i % 3 == 0:
        l.append(i)
print (l)               #выводим список
print (sum(l) / len(l))    #выводим среднее арифметическое
    



