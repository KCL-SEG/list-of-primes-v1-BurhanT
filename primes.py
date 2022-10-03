"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    for i in range(0, number_of_primes):
        for j in range(1, i):
            if (i % j == 0):
                break
            else:
                list.append(i)
    return list
