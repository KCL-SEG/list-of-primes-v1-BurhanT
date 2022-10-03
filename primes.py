"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    for i in range(1, number_of_primes):
        for j in range(2, i):
            if (i % j == 0):
                break
            else:
                list.add(i)

    return list
