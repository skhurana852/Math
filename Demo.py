#This is a Demo File which shows you how to use Math101.py
#Some new functions are available although I will be adding new functions soon

from Math101 import isPrime,factorial,isPallindrome,GCD,LCM

#Taking Input
n = int(input('Enter the No'))

# Using isPrime() Function
if isPrime(n) == True:
    print('Prime No')
else:
    print('Not a Prime no')

#Using factorial function()

print(factorial(n))

#Using isPallindrome() Function

print(isPallindrome(n))

#Using  GCD
print(GCD(15,35))

#Using LCM
print(LCM(10,20))

#In the same manner you can use functions such as swap, average etc..
#Don't Forget to import Math101 and Math101 and your file should be in same folder
#....
