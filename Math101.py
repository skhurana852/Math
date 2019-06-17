#Function to check Pallindrome
def isPallindrome(n):
    temp = n
    var = 0
    while n >= 1:
        i = int(n%10)
        var = var*10 + i 
        n = n/10
    if var == temp:
        return True
    else:
        return False

# Function to compute Average

def avg(a,b):
    avg = (a+b)/2
    return avg

#Function to compute factorial

def factorial(n):
    if n>1:
        return n * factorial(n-1)
    else:
        return 1

#Function to compute GCD

def GCD(a,b):               #Euclidean Algorithm
    if a ==0:
        return b
    else:
        return GCD(b%a, a)

#Function to compute LCM

def LCM(a,b):
    return (a*b)/GCD(a,b)


#Function to check if it is Prime or not
def isPrime(n):
    flag= True
    for i in range(2,int(n/2)+1):
        if int(n%i) == 0:
            flag = False
            break
        else:
            flag = True
    return flag

#Function to swap
def swap(a,b):
    temp = a
    a = b
    b = temp
