#Author Kristina Beresneva
#25.02.2022
#task: создать конвертер
#american_mile = 1.609344 
#american_gallon = 3.785411784 
#gallon = liters / american_gallon
#miles = 100 * 1000 / american_mile

def liters_100km_to_miles_gallon(liters):     #определяем функцию для расчета
    miles_gallon = ((100 * 3.785411784) / liters / 1.609344)
    return miles_gallon

def miles_gallon_to_liters_100km(miles):      #определяем функцию для расчета
    liters_100km = ((100 * 3.785411784) / (miles * 1.609344))
    return liters_100km


print(liters_100km_to_miles_gallon(3.9))      #выводим результат
print(liters_100km_to_miles_gallon(7.5))      #выводим результат
print(liters_100km_to_miles_gallon(10.))      #выводим результат
print(miles_gallon_to_liters_100km(60.3))     #выводим результат
print(miles_gallon_to_liters_100km(31.4))     #выводим результат
print(miles_gallon_to_liters_100km(23.5))     #выводим результат
