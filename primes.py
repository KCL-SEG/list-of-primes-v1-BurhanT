"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = [2]
    i = 1
    while len(list) < number_of_primes:
        for j in range(2, i):
            if (i % j == 0):
                break
            elif i not in list:
                list.append(i)
        i += 1
    return list
