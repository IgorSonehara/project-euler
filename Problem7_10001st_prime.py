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

i = 2
count = 0
while True:
    if isPrime(i):
        count = count + 1
        if count == 10001:
            break
    
    i = i + 1

print(i)