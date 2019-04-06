# -*- coding: utf-8 -*-
import socket
import os
import shutil
import threading
import argparse

serverName = "localhost"
serverPort = 2080

while 1:
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    parser = argparse.ArgumentParser()
    parser.add_argument('--message', '-d', type=str,
                        help='Message to send')
    args = parser.parse_args()


    args.message = raw_input('Message: ')
    print (args.message)

    try:
        clientSocket.connect((serverName,serverPort))
    except Exception:
        pass

    try: 
        # sentence = input("Input lowercase sentence: ")
        sentence = args.message
        clientSocket.send(sentence.encode())

        modifiedSentence = clientSocket.recv(1024)

        if (sentence.split()[0] == 'GET'):
            arq = open(sentence.split()[2], 'w')
            arq.write(modifiedSentence)
            arq.close()

        print("From Server: ", modifiedSentence.decode())

        clientSocket.close()

    except KeyboardInterrupt:
        escape = True
    except Exception:
        clientSocket.close()


    clientSocket.close()
print("\nBye bye :)")