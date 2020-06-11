#!/usr/bin/python3

#find largest palindromic numbers from the product of two 3-digit numbers

def palindrome_check(s):
    return s == s[::-1]

            
def largest_palindrome_threedigitproduct():
    max_pal = 1
    i = 999
    while i > 99:
        j = 999
        while j >= i:
            if i*j < max_pal: break
            if palindrome_check(str(i*j)): max_pal = i*j
            j -= 1
        i -= 1
    return max_pal

print(largest_palindrome_threedigitproduct())