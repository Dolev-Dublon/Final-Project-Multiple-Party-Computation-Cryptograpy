# unionB.py
import math
import numpy as np
from connections import Init_client_connection
from hand_shake import hand_shake_client_bob
from Bobfunctions import Bob


def orFunc(b, alice_server_socket):
    b = int(b)
    if hand_shake_client_bob(alice_server_socket):
        Bobbit = b
        bob = Bob(Bobbit)
        response = alice_server_socket.recv(2048).decode()
        cA_q_g_gk = response.split(",")
        cA = (int(cA_q_g_gk[0][1:]), int(cA_q_g_gk[1][:-1]))
        q = int(cA_q_g_gk[2])
        g = int(cA_q_g_gk[3])
        gk = int(cA_q_g_gk[4])
        bob.cB = bob.calc_encrypted_bit(cA, q, g, gk)
        alice_server_socket.send(str(bob.cB).encode())
        result = alice_server_socket.recv(1024).decode()
        return int(result)


def unionB(list, worldSize):
    alice_server_socket = Init_client_connection()
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
            bit_check = orFunc(P_check[j], alice_server_socket)
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
    alice_server_socket.close()
    return int_list 


if __name__ == "__main__":
    list = [0, 2]
    result = unionB(list, 16)
    print(result)
    # TODO: close socket after use (in both unionA.py and unionB.py)

