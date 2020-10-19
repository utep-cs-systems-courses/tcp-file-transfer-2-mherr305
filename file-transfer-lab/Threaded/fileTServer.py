#! /usr/bin/env python3

import sys, re, os
import socket, params
from os.path import exists
from threading import Thread, enumerate, Lock
global lock
lock = Lock()

switchesVarDefaults = (
    (('-l', '--listenPort'), 'listenPort', 50001),
    (('-d', '--debug'), "debug", False),
    (('-?', '--usage'), "usage", False),
    )
progname = "echoserver"
paramMap = params.parseParams(switchesVarDefaults)

debug, listenPort = paramMap['debug'], paramMap['listenPort']

if paramMap['usage']:
    params.usage()

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bindAddr = ("127.0.0.1", listenPort)
lsock.bind(bindAddr)
lsock.listen(5)
print("Listening on: ", bindAddr)
active_Files = []

from threading import Thread;
from encapFramedSock import EncapFramedSock

def fileStart(filename):
    if filename in active_Files:
        fsock.send(b"exists", debug)
    else:
        active_Files.append(filename)

def fileEnd(filename):
    active_Files.remove(filename)

class Server(Thread):
    def __init__(self, sockAddr):
        Thread.__init__(self)
        self.sock, self.addr = sockAddr
        self.fsock = EncapFramedSock(sockAddr)

    def run(self):
        print ("Thread connection from" , self.addr)

        filename = self.fsock.receive(debug)
        lock.aquire()

        fileStart(filename)
        lock.release()
        file = filename.decode()
        file = "new"+flle
        if exists(file):
            self.fsock.send(b"True", debug)
        else:
            self.fsock.send(b"False",debug)
            payload = self.fsock.receive(debug)
            if debug:
                print("rec'd; : ", payload)

            if not payload:
                if debug:
                    print(f"thread connected to {addr} ")
                self.fsock.close()
                return

            outputFile = open(file, "wb")
            outputFile.write(filename)
            outputFile.write(payload)
            fileEnd(filename)
            self.fsock.send(b" Thread done", debug)

while True:
    sockAddr = lsock.accept()
    server = Server(sockAddr)
    server.start()
