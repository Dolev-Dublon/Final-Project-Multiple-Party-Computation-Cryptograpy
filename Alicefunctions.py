# Alicefunctions.py
from sympy import is_quad_residue, isprime
import random

def generate_alice_keys(b):
    q = generate_random_prime_with_n_bits(30)
    alice = Alice(b, q)
    cA_q_g_gk = (
            str(alice.cA)
            + ","
            + str(alice.q)
            + ","
            + str(alice.g)
            + ","
            + str(alice.gk)
        )
    return cA_q_g_gk, alice


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


class Alice:
    def __init__(self, bit, q):
        self.bit = bit
        self.q = q
        self.k = random.randint(0, q - 1)
        self.p = 2 * self.q + 1
        self.g = self.find_quadratic_residue()
        self.cA, self.q, self.g, self.gk = self.calc_encrypted_bit()

    def calc_encrypted_bit(self):
        r = random.randint(2, self.q - 1)
        if self.bit == 0:
            cA = (pow(self.g, r, self.p), pow(self.g, r * self.k, self.p))
        else:
            cA = (
                pow(self.g, r, self.p),
                (self.g * pow(self.g, r * self.k, self.p)) % self.p,
            )
        return cA, self.q, self.g, pow(self.g, self.k, self.p)

    def decrypt_message(self, cB):
        return modular_division(cB[1], pow(cB[0], self.k, self.p), self.p)

    def find_quadratic_residue(self):
        while True:
            candidate = random.randint(2, self.p - 2)
            if is_quad_residue(candidate, self.p):
                return candidate

    def __str__(self):
        return f"bit={self.bit}, q={self.q}, k={self.k}, p={self.p}, g={self.g}"
