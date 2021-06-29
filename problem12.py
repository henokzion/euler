import math
num_of_divisors = 0
num = 0
adder = 1

while num_of_divisors < 500:
    num_of_divisors = 0
    num = num + adder
    adder = adder + 1
    for i in range(1,int(math.sqrt(num))):
        if (num % i == 0):
            num_of_divisors = num_of_divisors + 1
    num_of_divisors = num_of_divisors * 2
    if num % int(math.sqrt(num)) == 0:
        num_of_divisors = num_of_divisors + 1
    print(num, num_of_divisors)

print(num)