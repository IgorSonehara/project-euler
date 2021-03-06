#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def evenlyDivisible(n):
    for i in range(1, 21):
        if n % i != 0:
            return False
    return True

n = 1
while True:
    if evenlyDivisible(n):
        print(n)
        break

    n = n + 1