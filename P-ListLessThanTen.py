"""
FROM PracticePython.org
Exercise 3: List Less Than Ten

Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

and write a program that prints out all the elements of the list that are less than 5.

Extras:

    Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
    Write this in one line of Python.
    Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

print("Print out all elements of list a <= 5")
print("*"*20)
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print('a= ' + str(a))

n = 0
while n <= 10:
    if a[n] <= 5:
        print(a[n])
    n=n+1
    print( "*" * 20 )

print("FIRST TAKE: 1: Get length of list; 2. Print out all elements of list a <= 5")
print("*"*20)
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print('a= ' + str(a))

n = 0
length = int(len(a)) - 1
print(length)

while n <= length:
    if a[n] <= 5:
        print(a[n])
    n=n+1

print( "SCOND TAKE: 1: Get length of list; 2. Print out all elements of list a <= 5" )
print( "*" * 20 )
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
print( 'a= ' + str( a ) )

for i in a:
    if i <= 5:
        print( i )
"""


print("make a new list that has all the elements less than 5 from this list in it and print out this new list.")
print( "*" * 20 )
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

for i in a:
    if i <= 5:
        b.append(i)
        print( b )

#ANOTHER WAY TO SOLVE
print("OR")

mylist= []
[mylist.append(list) for list in a if list <= 5]
print (mylist)

print("Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.")
ask_num = input("Give me a number")
for i in a:
    if i <= int(ask_num):
        print( i )