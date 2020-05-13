"""
FROM PracticePython.org
Exercise 2
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

    If the number is a multiple of 4, print out a different message.
    Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

"""

# ask_num = input("Give me a number")
ask_num = 20

if int(ask_num) % 2 == 0:
    print('Your number is even')
else:
    print('Your number is odd')

if int(ask_num) % 4 == 0:
    print('Your number is divisible by 4')
else:
    print('Your number is not divisible by 4')

num = input("Give me another number to check")
check = input("Give me another number to divide by")

if int(num) % int(check) == 0:
    print('Your number ' + num + ' is divisible by ' + check)
else:
    print('Your number ' + num + ' is not divisible by ' + check)

num=1000000
check=768

if num % check == 0:
    print('Your number ' + str(num) + ' is divisible by ' + str(check))
else:
    print('Your number ' + str(num) + ' is not divisible by ' + str(check))