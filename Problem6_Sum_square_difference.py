sumSquares = squareSum = 0

for i in range(1, 101):
    sumSquares = sumSquares + i ** 2
    squareSum = squareSum + i

print(squareSum ** 2 - sumSquares)