def hand_shake_sever_bob(server_socket):
    msg = server_socket.recv(1024).decode()
    if  msg == "Ready":
        server_socket.send(b"Acknowledged")
        msg = server_socket.recv(1024).decode()
        if msg == "Acknowledged":
            return True
    
    return False

def hand_shake_client_bob(server_socket):
    server_socket.send(b"Ready")
    Acknowledge = server_socket.recv(1024).decode()
    if Acknowledge == "Acknowledged":
        server_socket.send(b"Acknowledged")
        return True
    return False