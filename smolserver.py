import socket

# Server setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creating a TCP protocol
server.bind(('0.0.0.0', 9999))  # Listening on all IPs, port 9999
server.listen(1)
password = 33

print("Server is listening on port 9999...")

# Wait for a connection from the client
client_socket, client_address = server.accept()  # It will pause the program and wait for a client to connect. It doesn’t proceed until the client makes a connection.
print(f"Connection from {client_address} received now...")

ask_password = int(input("Enter the password to use client: "))
if ask_password == password:
    while True:
        # Ask the server user to input a command to send to the client
        command = input("Enter the command to execute on client ('exit' to quit): ")

        if command.lower() == 'exit':
            print("Exiting...")
            client_socket.send('exit'.encode())  # Tells the client to close the connection
            break

        # Send the command to the client
        client_socket.send(command.encode())

        # Receive the output from the client
        client_output = client_socket.recv(1024).decode()
        print(f"Output: {client_output}")
else:
    print("Wrong attempt! Exiting...")
    client_socket.send('exit'.encode())

# Close the connection
client_socket.close()
server.close()

