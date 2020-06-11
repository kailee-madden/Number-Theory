#!/usr/bin/python3

#find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

def sum_squares_dif(num):
    sum_squares = 0
    square_sum = 0
    for n in range(1, num+1):
        sum_squares += n**2
        square_sum += n
    return(abs(square_sum**2 - sum_squares))

print(sum_squares_dif(10))