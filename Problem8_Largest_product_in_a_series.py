num = 40319989

greatest = 0
product = 1
var = 0

for i in range(num):
    product = product * i
    if var == 4:
        if product > greatest:
            greatest = product
            var = 0
            product = 1
    var = var + 1

print(greatest)
