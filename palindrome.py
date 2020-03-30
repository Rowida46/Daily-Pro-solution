### Given an integer, check if that integer is a palindrome. For this problem do not convert the integer to a string to check if it is a palindrome.


import math

def is_palindrome(n):
  # Fill this in.
    l = []
    while n :
        l.append(n%10)
        n //=10
    if l[::-1] == l:
        return True
    else :
        return False
print (is_palindrome(1234321))
# True
print( is_palindrome(1234322))
# False
