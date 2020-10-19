#! /usr/bin/env python3

import socket,sys,re
import params
from os import path
from os.path import exists
sys.path.append("../../lib")

from encapFramedSock import EncapFramedSock

switchesVarDefaults = (
    (('-s', '--server'), 'server', "127.0.0.1:50001"),
    (('-d', '--debug'), "debug", False),
    (('-?', '--usage'), "usage", False),
    )

progname = "fileTClient"
paramMap = params.parseParams(switchesVarDefaults)

server, usage , debug = paramMap["server"], paramMap["usage"], paramMap["debug"]

if usage:
    params.usage()

try:
    serverHost, serverPort = re.split(":", server)
    serverPort = int(serverPort)

except:
    print("Cant parse server: port from '%s'" % server)
    sys.exit(1)

addrFamily = socket.AF_INTET
socktype = socket.SOCK_STREAM
addrPort = (serverHost, serverPort)

sock = socket.socket(addrFamily, socktype)

if sock is None:
    print('could not open socket!')
    sys.exit(1)

sock.connect(addrPort)
fsock = EncapFramedSock((sock, addrPort))
for i in range(1):
    filename = input("Enter file name")

    if exists(filename):
        file = open(filename, 'rb')
        payload = file.read()
        if len(payload) ==0;
        print("Cant send empty file")
        sys.exit(0)
    else:
        fsock.send(filename.encode() , debug)
        fileExi = fsock.receive(debug).decode()
        if fileExi== 'True':
            print("File exists")
            sys.exit(0)
        elif fileExi == 'exists':
            print("There is another user on this server")
            sys.exit(0)
        else:
            fsock.send(payload,debug)
            print(" Server : ",fsock.receive(debug).decode())
    else:
        print("File '%s' doesnt exist" % filename)

        
