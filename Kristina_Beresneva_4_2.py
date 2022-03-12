#Author Kristina Beresneva
#25.02.2022
#task: проверить год високосный или нет
year = int(input("Введите год: "))                    #спрашиваем год
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
if is_year_leap(year) == True:        #выводим результат
    print("True")
else:
    print("False")
 
test_data = [1900, 2000, 2016, 1987]     #годы для проверки
test_results = [False, True, True, False]
for i in range(len(test_data)):               #проверяем каждый данный год
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")                     #выводим результат
    else:
        print("Failed")                 #выводим результат  
