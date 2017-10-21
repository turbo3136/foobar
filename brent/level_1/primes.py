def answer(n):
    primes = [2, 3]

    s = '23'

    while len(s) < n + 5:      #stops iterating once the string is of length n+5

        #take the list of primes and loop through odd numbers greater than the last entry
        #    until we get to a prime. Then append it to the primes list and concat to s.
        check = True
        i = 1
        while check:
            test_prime = primes[-1] + 2*i
            if all(test_prime%primes[j] != 0 for j in range(1, len(primes) - 1)):
                primes.append(test_prime)
                s += str(test_prime)
                check = False

            i += 1

    return s[n:n+5]


a = answer(100)
print(a)
