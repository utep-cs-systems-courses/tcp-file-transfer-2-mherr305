import re

def framedSend(sock, payload, debug=0):
    if debug: print("framedSend: sending %d byte message" % len(payload))
    msg = str(len(payload)).encode() + b':' + payload
    while len(msg):
        nsent = sock.send(msg)
        msg = msg[nsent:]

rbuf = b""                #STATIC RECEIVE BUFFER

def framedReceive(sock, debug=0):
    global rbuf
    state = "getLenght"
    msgLenght =-1
    while True:
        if(state == "getLenght"):
            match = re.match(b'([^:]+):(.*)', rbuf, re.DOTALL | re.MULTILINE) #LOOK FOR COLON
            lengthStr, rbuf = match.groups()
            try:
                msgLenght = int(lengthStr)
            except:
                if len(rbuf):
                    print("badly formed message length:", lengthStr)
                    return None
                state = "getPayload"
        if state == "getPayload":
            if len(rbuf) >= msgLenght:
                payload = rbuf[0:msgLenght]
                rbuf = rbuf[msgLenght:]
                return payload
        r = sock.recv(100)
        rbuf +=r
        if len(r) ==0:
            if len(rbuf) !=0:
                print("FramedReceive: incomplete message. \n state=%s, lenght=%d, rbuf%s" % (state, msgLenght, rbuf))
                return None
            if debug: print("FramedReceive: state=%s, lenght=%d, rbuf=%s" % (state, msgLenght, rbuf))
