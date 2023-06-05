import socket

def Init_connection():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_host = "0.0.0.0"  # listen on all available network interfaces
    server_port = 1234  # choose a port number
    server_socket.bind((server_host, server_port))
    server_socket.listen()
    print("Waiting for a connection...")
    bob_socket, client_address = server_socket.accept()
    print("Connected to:", client_address)
    return bob_socket



def Init_client_connection():        
    alice_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_host = "localhost"  # Replace with the server's IP address
    server_port = 1234  # Replace with the server's port number
    alice_server_socket.connect((server_host, server_port))
    return alice_server_socket