import socket

SERVER_PRT = 1234

def start_connection():
    server = socket.socket()
    server.bind(("", SERVER_PRT))  # Bind to all available interfaces
    server.listen(5)
    print(f"Server is listening on Port: {SERVER_PRT}")

    while True:
        client, _ = server.accept()
        print("Client connected")
        respond_to_client(client)

def respond_to_client(client):
    try:
        while True:
            # Receive data from the client
            data = client.recv(1024).decode()
            if not data:
                break  # No data means the client closed the connection

            print(f"Received data: {data} cm")

            # Optionally, send a response to the client
            client.send("Data received".encode())

    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    start_connection()
