# Задача 4: створення веб-сервера, що обслуговує кілька клієнтів одночасно
# Напишіть простий веб-сервер, який може обслуговувати кілька клієнтів одночасно, використовуючи потоки або процеси.
# Ваша програма повинна відповідати на HTTP-запити клієнтів і відправляти їм текстові повідомлення.
# Підказка: можна використовувати вбудовану бібліотеку http.server.


import socket # Provides functions and classes for working with network connections based on TCP and UDP.
import multiprocessing # Allows creation and management of processes.

def handle_client(client_socket):
    '''
    Handles enquiries from clients.
    :param client_socket: to exchange data with the client (Allows the client to receive its own connection).
    '''
    request = client_socket.recv(1024).decode('utf-8') # Reads up to 1024 data bytes sent by the client over a socket.
    print(f"Отримано запит: \n{request}")

    # Response to the client.
    response = "HTTP/1.1 200 OK\r\n"
    response += "Content-Type: text/html\r\n\r\n"
    response += "<html><body><h1>Hello! This is a multiprocessor server.</h1></body></html>"

    # Sends HTTP response to the client.
    client_socket.send(response.encode('utf-8'))
    client_socket.close()

def start_server():
    '''Starts the server and accepts client connections.'''

    # Creates a socket for TCP protocol operation.
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # socket.AF_INET: specifies that the socket will work with IPv4 addresses.
    # socket.SOCK_STREAM: indicates that the TCP protocol will be used.

    # Associates a socket with an IP address and port
    server.bind(('0.0.0.0', 8092))
    # '0.0.0.0': specifies that the server will accept connections on all network interfaces.
    # 8092: Sets the port on which the server will expect incoming connections. Clients will connect to this port.

    # Sets the socket to listen for incoming connections.
    server.listen(5) # Maximum connection queue length = 5
    print("Сервер запущено на порту 8092, очікування з'єднань...")

    # The server will run until it is forcibly stopped.
    while True:
        # server.accept(): returns a new socket to communicate with the client (client_socket) and the client address (addr).
        client_socket, addr = server.accept()
        print(f"Підключено клієнта: {addr}")

        # Create a new process to process a customer request
        client_process = multiprocessing.Process(target=handle_client, args=(client_socket,))
        client_process.start()

if __name__ == "__main__":
    start_server()
