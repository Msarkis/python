"""
FROM PracticePython.org
Exercise 4: Divisors
Create a program that:
 1. asks the user for a number
 2. prints out a list of all the divisors of that number.
"""

ask_num = 30

print("The divisors of " + str(ask_num) + " are ")
y=[]

i = 1
n= 0

while (i < ask_num):
    y.append(i)
    i = i+1

for n in y:
    if ask_num % n == 0:
        print(ask_num / n )

print("\nAnother solution\n")
devisors = [i for i in range(1,ask_num) if ask_num % i == 0]
print(str(ask_num) + " is divisible by ", str(devisors))