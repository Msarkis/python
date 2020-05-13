"""
FROM PracticePython.org
Exercise 1: Character Input
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

    Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
    Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

"""

name = "Marianne"
age = 47
onehundred = 100-age
date = 2020
onehund = onehundred + date


response = "Hello " + name + ", your age is " + str(age) + ", and you will turn 100 in year " + str(onehund) + '\n'
inputtimes = 10

print(response)
print(response*inputtimes)