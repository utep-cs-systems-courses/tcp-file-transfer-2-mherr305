#! /usr/bin/env python3

#ECHO CLIENT PROGRAM
import socket, sys, re, os

sys.path.append("../lib")
import params

from framedSock import framedSend, framedReceive

switchesVarDefaults = (
    (('-s', '--sever'), 'server', "127.0.0.1:50001"),
    (('-d', '--debug'), "debug", False), # boolean (set if present)
    (('-?', '--usage'), "usage", False), # boolean (set if present)
    )

progname = "framedClient"
paramMap = params.parseParams(switchesVarDefaults)

server, usage, debug = paramMap["server"], paramMap["usage"], paramMap["debug"]

if usage:
    params.usage()


try:
    serverHost, serverPort = re.split(":", server)
    serverPort = int(serverPort)

except:
    print("Can't parse server:port from '%s'" % server)
    sys.exit(1)


addrFamily = socket.AF_INET
socktype = socket.SOCK_STREAM
addrPort = (serverHost, serverPort)

s = socket.socket(addrFamily, socktype)

if s is None:
    print('Could not open socket')
    sys.exit(1)

s.connect(addrPort)
print('You are connected')

while True:
    inputFile = input("Type the name of your file please")
    if exists(inputFile):
        userFile = open(inputFile, "r" )
        file = userFile.read()

        if len(file)==0:
            print("The file does not contain data")

        else:
            framedSend(s,inputFile.encode(),debug)
            try:
                filerec = framedReceive(s,filerec.decode(),debug)
            except:
                print("There is an error when recieving")
            if filerec==True:
                print("File received succesfully!")

            else:
                try:
                    framedSend(s, file.encode(),1)
                except:
                    print("There is an error sending")
                try:
                    fileServer = framedReceive(s,fileServer.decode(),debug)
                    print(fileServer)
                except:
                    print("There is an rror recieving in Server")

    if inputFile=="exit":
        sys.exit(0)
    else:
        ("The file you are trying to execute does not exists!")
s.shutdown(socket.SHUT_WR)

While True:
    info = s.recv(1024).decode()
    print("Data succefully received '%s'" % info)
    s.close()










                
