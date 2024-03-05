import socket
import threading

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except socket.error:
            print("Connection lost.")
            break

def send_messages():
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))

# Set up the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get user input for the room code
room_code = input("Enter the room code: ")

# Connect to the server
server_address = ('your_server_ip', 12345)  # Replace with your server's IP and port
client_socket.connect(server_address)

# Send the room code to the server
client_socket.send(room_code.encode('utf-8'))

# Start separate threads for sending and receiving messages
recv_thread = threading.Thread(target=receive_messages)
send_thread = threading.Thread(target=send_messages)

recv_thread.start()
send_thread.start()
