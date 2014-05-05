__author__ = 'dhash'
import math
def make_primes_factors(lim):
    prime_array = []
    for iter in range(3, int(math.sqrt(lim)) + 1, 2):
        if lim % iter == 0:
            prime_array.append(iter)
    for elem in prime_array:
        for remove_ind in range(0, len(prime_array)):
            if prime_array[remove_ind] > elem:
                if prime_array[remove_ind] % elem == 0:
                    del(prime_array[remove_ind])
                    break

    prime_array.append(1)
    if lim % 2 == 0:
        prime_array.append(2)
    prime_array.sort()
    return prime_array

input = int(input("to find the prime factors of a number, enter it: "))
print(make_primes_factors(input))