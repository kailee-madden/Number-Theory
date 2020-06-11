#!/usr/bin/python3

#find largest prime factor of 600851475143

import time
import math

start_time = time.clock()

def sieve_eratosthenes(n): #find prime numbers up to given number
    prime_list = [p for p in range(3, n+1, 2)]
    prime_list.insert(0,2)
    i = 3
    while i <= math.sqrt(n):
        if i in prime_list:
            for j in range(i*2, n+1, i):
                if j in prime_list:
                    prime_list.remove(j)
        i += 1
    return prime_list

def prime_sum(n): #find sum of all primes up to a given n
    primes = sieve_eratosthenes(n)
    return sum(primes)
print(prime_sum(2000000))

def prime_factors(n): #find prime factors list for a given number
    divisor = 2
    primes = []
    while n > 1:
        if n % divisor == 0: 
            primes.append(divisor)
            n = n/divisor
            while n % divisor == 0:
                n = n/divisor
        divisor +=1
    return primes

def largest_prime(n): #find largest prime factor of a composite number
    divisor = 2
    previous_divisor = 1
    while n > 1:
        if n % divisor == 0: 
            previous_divisor = divisor
            n = n/divisor
            while n % divisor == 0:
                n = n/divisor
        divisor +=1
    return previous_divisor

def is_prime(n): #check if a number n is prime
    if n == 1: return False
    elif n < 4: return True #both 2 and 3 are prime
    elif n % 2 == 0: return False #divisible by two
    elif n < 9: return True #already excluded all evens so leaves only 5 and 7
    elif n % 3 == 0: return False #divisible by 3
    else:
        r = math.floor(math.sqrt(n)) #r rounded to the greatest integer r so that r*r <=n
        f = 5 #this will be the form of 6k +/1 which is the form of all primes other than 2 and 3
        while f <= r:
            if n % f == 0: return False
            if n % (f+2) == 0: return False
            f = f+6
        return True

def nth_prime(limit): #find nth prime number
    count = 1 #since 2 is prime and we're going to skip it
    candidate = 1
    while count != limit:
        candidate = candidate + 2
        if is_prime(candidate): count += 1
    return candidate
      
def nthprime_bruteforce(n): #find nth prime number via brute force method
    prime = 2
    nth = 1
    num = 3
    while nth != n:
        for i in range(2, num):
            if num % i == 0:
                break
            if i == num-1:
                prime = num
                nth += 1
        num += 2
    return prime

#num = 600851475143
#print(largest_prime(10))
#print(prime_factors(10))
#print(sieve_eratosthenes(10))
print("{} seconds".format(time.clock() - start_time))
#print(nthprime(10001))