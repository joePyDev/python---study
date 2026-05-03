import socket

mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(("data.pre.org",80))