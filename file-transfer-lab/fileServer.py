#! /usr/bin/env python3

import sys
sys.path.append("../lib")  # for params
import re, socket, params, os

switchesVarDefaults = (
    (('-l', '--listenPort'), 'listenPort', 50001),
    (('-d', '--debug'), "debug", False), # boolean (set if present)
    (('-?', '--usage'), "usage", False), # boolean (set if present)
    )

progname = "echoserver"
paramMap = params.parseParams(switchesVarDefaults)

debug, listenPort = paramMap['debug'], paramMap['listenPort']

if paramMap['usage']:
    params.usage()

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #listener socket
bindAddr = ("127.0.0.1", listenPort)
lsock.bind(bindAddr)
lsock.listen(5)
print("Listening on:", bindAddr)

sock, addr = lsock.accept()

print("connection rec'd from", addr)

from framedSock import framedSend, framedReceive

while True:
    if not os.fork():
        ("New connection from" , addr)
        while True:
            payload = framedReceive(sock, debug)
            if not payload:
                break
            payload = payload.decode()

            if exists(payload):
                framedSend(sock, b"Accept",1)
            else:
                framedSend(sock, b"Denied",1)

            try:
                framedSend(sock, b"Success", debug)
            except:
                print("Failed")
                sys.exit(0)

                outputFile = open(payload, 'a')
                payloadOut = payloadOut.decode()
                outputFile.write(payloadOut)
                outputFile.close()
                sock.close()
