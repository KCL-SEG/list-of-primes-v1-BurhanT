"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = [2]
    i = 1
    while len(list) < number_of_primes:
        for j in range(2, i):
            if i % j == 0 or i in list:
                break
            else:
                list.append(i)
        i += 1
    return list
