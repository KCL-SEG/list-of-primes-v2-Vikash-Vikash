"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

from ast import Raise


def primes(number_of_primes):

    if number_of_primes <1:
        raise ValueError

    list = []
    num=1
    while len(list)<number_of_primes:
        num+=1
        prime=True
        for i in range(2,(num/2)+1):
            if num%i==0:
                prime=False
                break
        if prime:
            list.append(num)



    return list
