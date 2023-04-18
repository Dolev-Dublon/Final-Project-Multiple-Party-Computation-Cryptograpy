

import random

def encrypt(value, key):
    return value + key

def decrypt(value, key):
    return value - key

def generate_key():
    return random.randint(1, 100)

def input_value(user_id):
    return int(input("User " + str(user_id) + ", please enter a value: "))

def secure_minimum():
    key1 = generate_key()
    key2 = generate_key()
    input1 = input_value(1)
    input2 = input_value(2)
    encrypted1 = encrypt(input1, key1)
    encrypted2 = encrypt(input2, key2)
    shared_key = key1 + key2
    decrypted1 = decrypt(encrypted1, key2)
    decrypted2 = decrypt(encrypted2, key1)
    minimum = min(decrypted1, decrypted2)
    encrypted_minimum = encrypt(minimum, shared_key)
    return encrypted_minimum

print("The minimum value is:", decrypt(secure_minimum(), generate_key() * 2))






