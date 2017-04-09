from primesieve import primes
import string
from sympy import isprime

def is_family(num, r):
    c = 0
    for digit in '0123456789':
        n = int(num.replace(r, digit))
        if (n > 100000 and isprime(n)):
            c = c + 1

for prime in primes(1000000):
    if (prime > 100000):
        s = str(prime)
        last_digit = s[5:6]
        if (s.count('0')  == 3 and is_family(s, '0') or s.count('1') == 3 and is_family(s, '1') or s.count('2') == 3 and is_family(s, '2')):
            print(s)
