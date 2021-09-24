#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
import math

def isPrime(n):
    flag = 1

    if n <= 1:
        flag = 0
    else:
        for i in range(2, (int)(math.sqrt(n))+1):
            if n % i == 0:
                flag = 0
                break

    return flag

n = 600851475143
largest = 0

i = 1
while (i * i) <= n:
    if n % i == 0:
        if isPrime(i):
            largest = i
    i = i + 1

print(largest)