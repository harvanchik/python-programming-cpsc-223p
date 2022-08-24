# Name: Jake Harvanchik
# Date: 08/24/2022
# File Purpose: Lab01 main program driver program

from hello import *

print("*** TUFFY TITAN HELLO PROGRAM ***")

print(helloWorld())

print(helloName("Jake"))

print("3 + 3 =", add(3, 3))
print("4 - 1 =", subtract(4, 1))
print("4 * 4 =", multiply(4, 4))
print("4 / 2 =", divide(4, 2))

num = 3

if (isEven(num)): print(num, "is even.")
else: print(num, "is odd.")


numbers = [1, 2, 3, 4]

printList(numbers)

print("The biggest number between 4, 7, and 9 is", biggest(4, 7, 9))

# data = club()

# print(data)