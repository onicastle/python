import sys
import math
import random
##NOTE YOU NEED TO WORK ON THIS NUMPY Installation, Tuples and Reading external files and revisit your notes
import numpy ##this adds arrays and matrices
h = numpy.array([1,0,2])
print(h)
##This is to learn and refer whenever I have doubts with the syntax.
x = int(input("hello pls enter a number\n"))
##i had to specify the data type of the input
##this can be done with all kinds of types

y = 6
##Range
start = 0
counter = 1
stop = 3
##Logical Operators
if(y != x) and not(x == 0):
    if (x == y) or (x == 13):
        print(x)
    elif y < x:
        print("Input is great just like us baby")
    else:
        print("no comment teehee")
else:
    print(y+x)

##For Loops with range
for k in range(start, x):
    counter = counter + 1
print(counter)

##List, they can have mix data types or nothing
myList = ["Hello","Do we stan?",3]
z = []
#To refer to index
myList[0] = 3
myList[1] = "teehee"

print(myList[0])
print(myList[1])
##here we concat lists
firstList = [1,2,3]
secondList = [4,5,6]
print(firstList + secondList)
##Methods for List
firstList.append(3) ##we added an extra 3
firstList.remove(3) ##we removed the third index which we recently added
for p in range(0, len(secondList)):
    print (secondList[p])
    ##Prints
    ##4
    ##5
    ##6
for item in myList:
    print (item)
    ##same as below but the data stored in the first one
for f in range(-1,10):
    w = 2*f+4
    print("w = ",w)
##while loops
x1 = 0
while x1 <= 5:
    print (x1)
    x1 = x1 + 1
##let's make a recursive function function
n = int(input())
def factorial(n):
    if(n ==0):
        return 1
    else:
        return n*factorial((n-1))

print(factorial(n))    
##Working with Strings
##kinda like list
a = "Hello"
print(a[1])
print(a[0:2]) ##He
r = a[3]
print(r)
print(a[1] == "H")

def printString(s):
    for j in range(0, len(s)):
        print(s[j])

##Modules have functions (see In-built functions visit python/library/functions)
