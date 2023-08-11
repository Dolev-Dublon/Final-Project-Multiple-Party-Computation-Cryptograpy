import socket

def Init_connection():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_host = "0.0.0.0"  # listen on all available network interfaces
    server_port = 2322  # choose a port number
    server_socket.bind((server_host, server_port))
    server_socket.listen()
    return server_socket

def accept_client(server_socket):
    client_socket, client_address = server_socket.accept()
    return client_socket

def Init_client_connection():
    alice_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    alice_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_host = "localhost"  # Replace with the server's IP address
    server_port = 2322  # Replace with the server's port number
    alice_server_socket.connect((server_host, server_port))
    return alice_server_socket
