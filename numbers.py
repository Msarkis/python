#Ask for number, and tell user if odd or even
# Marianne 12/10/2019
num = int(input("Enter a number: "))
mod = num % 2
if num % 4 == 0 :
    print("{} is divisible by 4.".format(num))
elif num % 2 == 0:
    print("{} is not divisible by 4, but is an even number.".format(num))
else:
    print("{} is not divisible by 4, but is an odd number.".format(num))
