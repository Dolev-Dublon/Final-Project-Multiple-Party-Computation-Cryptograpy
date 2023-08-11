# unionA.py
import math
import numpy as np
from connections import Init_connection, accept_client
from hand_shake import hand_shake_sever_bob
from Alicefunctions import generate_alice_keys


def orFunc(bob_socket, b):
    b = int(b)
    if hand_shake_sever_bob(bob_socket):
        alice_public_keys, alice = generate_alice_keys(b)
        bob_socket.send(alice_public_keys.encode())
        bob_public_keys = bob_socket.recv(2048).decode()  # cb = (cB, q, g, gk)
        bob_public_keys_tuple = tuple(map(int, bob_public_keys.strip("()").split(",")))
        decrypted_result = alice.decrypt_message(bob_public_keys_tuple)
        result = 0
        if decrypted_result == 1:
            result = 0
        else:
            result = 1
        bob_socket.send(str(result).encode())
        return int(result)


def unionA(list, worldSize, server_socket):
    # server_socket = Init_connection()
    bob_socket = accept_client(server_socket)
    P = ["0", "1"]  # live bits
    bitsList = []
    for i in range(len(list)):
        temp = format(list[i], f"0{int(math.log2(worldSize))}b")
        bitsList.append(temp)
    for i in range(int(math.log2(worldSize))):
        P_check = np.zeros(len(P))
        for p_index in range(len(P)):
            if P_check[p_index] == 1:
                continue
            for j in range(len(bitsList)):
                if bitsList[j].startswith(P[p_index]):
                    P_check[p_index] = 1
                    break
        for j in range(len(P_check) - 1, -1, -1):
            bit_check = orFunc(bob_socket, P_check[j])
            if bit_check == 0:
                P.pop(j)
        if i == math.log2(worldSize) - 1:  # last round, no new live p
            break
        tempP = []
        for p in P:
            tempP.append(p + "0")
            tempP.append(p + "1")
        P = tempP
    int_list = [int(binary, 2) for binary in P]
    bob_socket.close()
    # server_socket.close()
    return int_list


if __name__ == "__main__":
    list = [1, 2, 5, 11]
    server_socket = Init_connection()
    result = unionA(list, 16, server_socket=server_socket)
    print(result)
    # TODO: make bob know that the union is done and he can close the socket
