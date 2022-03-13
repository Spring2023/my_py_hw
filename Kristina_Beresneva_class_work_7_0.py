#1.
value = int(input('Enter a naturak number: '))
pruint('The reciprocal of', value, 'is', 1/value)

#2.
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)
except:
    print('I do not know what to do.')

#3.
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)
except ValueError:
    print('I do not know what to do.')
except ZeroDivisionError:
    print('Division by xero is not allowed in our Universe.')

#4.
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)
except ValueError:
    print('I do not know what to do.')
except ZeroDivisionError:
    print('Division by xero is not allowed in our Universe.')
except:
    print('Something strange has happend here... Sorry!')

#5.
tempreture = float(input('Enter current temperature: '))

if tempreture > 0:
    print("Above zero")
elif tempreture < 0:
    print("Below zero")
else:
    print("Zero")

#6.
while True:
    try:
        number = int(input("Enter an integer number: "))
        print(number / 2)
        break
    except:
        print("Warning: the value entered is not a valid number. Try again...")

#7.
while True:
    try:
        number = int(input("Enter an integer number: "))
        print(5 / number)
        break
    except (ValueError, ZeroDivisionError):
        print("Wrong value or No division by zero rule broken.")
    except:
        print("Sorry, something went wrong...")

#8.
while True:
    try:
        number = int(input("Enter an integer number: "))
        print(5 / number)
        break
    except ValueError:
        print("Wrong value.")
    except ZeroDivisionError:
        print("Sorry. I cannot divide by zero.")
    except:
        print("I don't know what to do...")

        
