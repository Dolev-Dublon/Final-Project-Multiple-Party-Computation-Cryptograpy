
import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_host = "0.0.0.0"  # listen on all available network interfaces
server_port = 1234  # choose a port number
server_socket.bind((server_host, server_port))
server_socket.listen()
print("Waiting for a connection...")
bob_socket, client_address = server_socket.accept()
print("Connected to:", client_address)
    