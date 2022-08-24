# Name: Jake Harvanchik
# Date: 08/24/2022
# File Purpose: Multiple hello functions

def helloWorld():
    return "Hello, world!"

def helloName(name):
    return "Hello, " + name + "!"

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a // b

# check if a number is even
# return true if the number is even; return false if the number is odd
def isEven(num):
    return num % 2 == 0

# print the contents of a list
def printList(list):
    print("Starting to print the list.")
    for num in list: print(num)
    print("Printed list is done.")

# determine the largest number out of three numbers
def biggest(a, b, c):
    max = a
    if (b > max): max = b
    if (c > max): max = c
    return max
