"""
Execute statements repeatedly
Conditions are used to stop the execution of loops
Iterable items are Strings, Lists, Tuples, Dictionaries
"""

# x=0
# while x < 10:
#     print("Value of x is: " + str(x))
#     x = x+1

l = []
num = 0

while num < 10:
    l.append(num)
    print("value of num is: " + str(num))
    num += 1
print(l)