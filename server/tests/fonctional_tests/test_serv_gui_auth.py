##
## EPITECH PROJECT, 2023
## auth
## File description:
## gui
##

import subprocess
import socket
import threading
import time
from queue import Queue

serv_response = "0\n5 5\n"

def connect_to_server(result_queue):
    host = 'localhost'
    port = 4244
    message = "GRAPHIC"

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        response = client_socket.recv(1024).decode()
        client_socket.send(message.encode())
        response = client_socket.recv(1024).decode()

        if response == serv_response:
            print("\033[92mV Success Test_ser_gui_auth\033[0m")
            result_queue.put(0)
        else:
            print("\033[91mX ERROR Test_ser_gui_auth: Unexpected response from server:", response, "\033[0m")
            result_queue.put(1)
    except ConnectionRefusedError:
        print("\033[91mX ERROR Test_ser_gui_auth: The connection was refused. Make sure the server is running.\033[0m")
        result_queue.put(1)
    except socket.error as e:
        print("\033[91mX ERROR Test_ser_gui_auth: An error occurred during the connection:\033[0m", e)
        result_queue.put(1)

def run_serv():
    chemin_fichier = '../zappy_server'

    try:
        subprocess.run([chemin_fichier, '-f', '100', '-c', '10', '-n', 'martin', '-y', '5', '-x', '5', '-p', '4244'], timeout=2)
    except:
        return 0

def Test_ser_gui_auth():
    result_t2 = Queue()
    t1 = threading.Thread(target=run_serv)
    t2 = threading.Thread(target=connect_to_server, args=(result_t2,))
    t1.start()
    time.sleep(0.5)
    t2.start()
    t2.join()
    thread_result = result_t2.get()
    t1.join(1)
    return 0