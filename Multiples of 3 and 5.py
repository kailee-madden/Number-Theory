#!/usr/bin/python3

#find the sum of all multiples of 3 or 5 below 1000
sum = 0
for n in range(3,1000):
    if n % 3 == 0 or n % 5 == 0:
        sum += n

print(sum)

def find_multiples_or(max, factors): 
    #find the list of multiples for a maximum number given the list of potential factors
    #if any of the numbers in the given list are a factor then the number is a multiple
    all_multiples = []
    for n in range(2, max+1):
        for m in factors:
            if n % m ==0:
                all_multiples.append(n)
                break
    return all_multiples

print(find_multiples_or(10, [3, 5]))

def find_multiples_and(max, factors): 
    #find the list of multiples for a maximum number given the list of potential factors
    #only a multiple is all the given numbers in the factors list are factors
    all_multiples = []
    for n in range(2, max+1):
        for m in factors:
            if n % m ==0:
                if m == factors[-1]: all_multiples.append(n)
                continue
            else:
                break
    return all_multiples

print(find_multiples_and(10, [2, 3]))


