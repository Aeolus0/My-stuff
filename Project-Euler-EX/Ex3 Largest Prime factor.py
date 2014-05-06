''' Given a number, find its prime factors'''
__author__ = 'dhash'
import math


def make_primes_factors(lim):
    prime_array = []
    for is_ele in range(3, lim + 1, 2):
        if lim % is_ele == 0:
            prime_array.append(is_ele)
    for elem in prime_array:
        for remove_ind in range(0, len(prime_array)):
            if prime_array[remove_ind] > elem:
                if prime_array[remove_ind] % elem == 0:
                    del (prime_array[remove_ind])
                    break

    prime_array.append(1)
    if lim % 2 == 0:
        prime_array.append(2)
    prime_array.sort()
    return prime_array


input_to_find_prime_factors = int(input("to find the prime factors of a number, enter it: "))
print(make_primes_factors(input_to_find_prime_factors))