"""
Write a Python program to retrieve a 
web page over a socket and display the headers from the web server.
"""

import socket

host = 'neverssl.com'
port = 80
path = '/online'


mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host, port))

cmd = f'GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n'
mysock.send(cmd.encode())

while True:
    data = mysock.recv(512)
    if not data:
        break
    print(data.decode(errors='replace'), end='')

mysock.close()