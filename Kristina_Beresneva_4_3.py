#Author Kristina Beresneva
#25.02.2022
#task: по году и месяцу вывести количество дней в этом месяце
year = int(input("Введите год: "))   #спрашиваем год
month = int(input("Введите месяц: "))  #спрашиваем месяц

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

def days_in_month(year, month):           #определяем функцию для количества дней в месяце
    if month > 12 or month < 1 or year < 1582:   #проверяем валидность года и месяца
        return None
    else:
        if is_year_leap(year) == True and month == 2:    #определяем количество дней
            res = 29
            return res
        else:
            res = days[month - 1]
            return res
print(days_in_month(year, month))        #выводим результат

test_years = [1900, 2000, 2016, 1987]     #годы для проверки
test_month = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):               #проверяем каждый данный год
    yr = test_years[i]
    mo = test_month[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")                     #выводим результат
    else:
        print("Failed")                 #выводим результат  





    
