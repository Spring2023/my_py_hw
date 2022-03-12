#Author Kristina Beresneva
#25.02.2022
#task: по году, месяцу и дню вывести какой день года по счету
year = int(input("Введите год: "))   #спрашиваем год
month = int(input("Введите месяц: "))  #спрашиваем месяц
day = int(input("Введите день: "))   #спрашиваем день

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]   #создаем список с днями

def is_year_leap(year):                #определяем функцию с условиями, когда год високосный      
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def day_of_year(year, month, day):       #считаем количество дней
    if day > 7 and day < 1:
        return None
    else:
        if is_year_leap(year) == True: 
            days[1] = 29
            x = month - 1
            y = 0
            for i in days[0 : x]:
                y += i 
            z = y + day
            return z
        else:
            x = month - 1
            y = 0
            for i in days[0 : x]:
                y += i
            z = y + day
            return z

print(day_of_year(year, month, day))        #выводим результат
print(day_of_year(2000, 12, 31))            #выводим результат
print(day_of_year(1900, 2, 28))             #выводим результат
print(day_of_year(2016, 1, 31))             #выводим результат



    
