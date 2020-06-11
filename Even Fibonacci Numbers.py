#!/usr/bin/python3

#find all even fibonacci numbers below four million

sum = 2
n = 2
n_1 = 3
while n_1 < 4000000:
    if n_1 % 2 == 0: sum += n_1
    n, n_1 = n_1, n_1 + n #variable swapping

print(sum)