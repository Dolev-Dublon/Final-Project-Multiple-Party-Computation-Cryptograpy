# Bobfunctions.py
from sympy import isprime
import random


def generate_random_prime_with_n_bits(bits):
    min_value = 2 ** (bits - 1)
    max_value = 2**bits - 1
    prime_candidate = random.randint(min_value, max_value)
    while not isprime(prime_candidate):
        prime_candidate = random.randint(min_value, max_value)
    return prime_candidate


def extended_euclidean_algorithm(a, b):
    """Euclid's extended algorithm:
    Given a, b, find gcd, x, y that solve the equation:
    ax + by = gcd(a, b)
    """
    x, y = 0, 1
    u, v = 1, 0
    gcd = b
    while a != 0:
        q, r = divmod(gcd, a)
        m, n = x - u * q, y - v * q
        gcd, a, x, y, u, v = a, r, u, v, m, n
    return gcd, x, y


def modular_division(A, B, m):
    """Modular division:
    Returns integer z such that: z * B mod m == A.
    If there is more than one (i.e. when gcd(B, m) > 1) - returns the smallest such integer.
    """
    assert 0 <= A < m, "Invalid A value"
    assert 0 <= B < m, "Invalid B value"

    #TODO why y is not used?
    gcd, x, y = extended_euclidean_algorithm(B, m)
    if A % gcd == 0:
        q = A // gcd
        return ((x + m) * q) % (m // gcd)
    else:
        raise ValueError("no quotient")


def multiply_with_large_modulo(num1, num2, m):
    num1 %= m
    result = 0
    while num2 > 0:
        if num2 % 2 == 1:
            result = (result + num1) % m
        num1 = (num1 * 2) % m
        num2 //= 2
    return result


class Bob:
    def __init__(self, bit):
        self.bit = bit
        self.cB = None
        
    
    #TODO why gk is not used?
    def calc_encrypted_bit(self, cA, q, g, gk):
        r_ = random.randint(2, q - 1)
        p = 2 * q + 1
        if self.bit == 0:
            cB = (pow(cA[0], r_, p), pow(cA[1], r_, p))
        else:
            cB = (pow(cA[0], r_, p), multiply_with_large_modulo(pow(g, r_, p) , pow(cA[1], r_, p), p))
        return cB



    # make a function that will print Bob when running print(Bob)
    def __str__(self):
        return f"bit={self.bit}, q={self.q}, k={self.k}, p={self.p}, g={self.g}"
