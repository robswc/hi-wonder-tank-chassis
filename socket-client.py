import socket

# Define the server's IP address and port
HOST = '127.0.0.1'  # Replace with the Raspberry Pi's IP address
PORT = 65432                      # Port to connect to (must match the server's port)

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))  # Connect to the server
    s.sendall(b'Hello, Raspberry Pi')  # Send some data
    data = s.recv(1024)  # Receive the response

print(f"Received from server: {data.decode()}")
