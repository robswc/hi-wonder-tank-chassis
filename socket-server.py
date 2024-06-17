import socket

# Define the host and port
HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 65432

if __name__ == '__main__':
    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))  # Bind the socket to the host and port
        s.listen()            # Enable the server to accept connections
        print(f"Server listening on {HOST}:{PORT}")

        # Accept a connection
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)  # Receive data from the client
                if not data:
                    break
                print(f"Received: {data.decode()}")
                conn.sendall(data)      # Echo the data back to the client

    # The connection is closed automatically when the block is exited
    print("Connection closed")
