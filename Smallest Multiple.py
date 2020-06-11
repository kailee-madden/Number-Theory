#!/usr/bin/python3

import math
from math import *
import time

start_time = time.clock()

#finding the smallest multiple of 1-20
def specific_smallest_multiple(): #specifically to solve the euler problem, generic functions below
    num = 2280
    divisors = [3,6,7,8,9,11,12,13,14,15,16,17,18]
    no_remainder = False

    while not no_remainder:
        num += 380
        for i in divisors:
            if num % i == 0:
                if i == 18: no_remainder = True
                continue
            else:
                break
    print(num)

#function to generally find the smallest multiple given the upper bound of the number list
def smallest_multiple(n): #brute force method
    divisors = [i for i in range(2, n+1)]
    remainder = True
    multiple = 0

    while remainder:
        multiple += 2
        for i in divisors:
            if multiple % i == 0:
                if i == divisors[-1]: remainder = False
                continue
            else:
                break
    return multiple

#find list of all primes
def sieve_eratosthenes(n):
    prime_list = [p for p in range(2, n+1)]
    i = 2
    while i <= math.sqrt(n):
        if i in prime_list:
            for j in range(i*2, n+1, i):
                if j in prime_list:
                    prime_list.remove(j)
        i += 1
    return prime_list


#prime algorithms approach
def small_multiple(k):
    primes = sieve_eratosthenes(k) #find the prime list for 2-k
    a = [1 for x in range(len(primes))]
    N = 1
    i = 0
    check = True
    for prime in primes:
        a[i] = 1
        if check:
            if prime <= math.sqrt(k): a[i] = math.floor(math.log(k)/math.log(prime))
            else:
                check = False
        N = N * prime**a[i]
        i += 1
    return int(N)

print(small_multiple(20))
print("{} seconds".format(time.clock() - start_time))
