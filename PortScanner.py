import threading as t
import socket
import sys
import time

IP = sys.argv[1]
FOR_EACH_THREAD = int(sys.argv[2])
PORT_START = int(sys.argv[3])
PORT_END = int(sys.argv[4])

def isOpen(lPort, uPort):
    for port in range(lPort, uPort + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.settimeout(3)
            s.connect((IP, port))
            print("[+] " + str(port) + " is open")
        except:
            pass
    

for i in range(PORT_START, PORT_END + 1, FOR_EACH_THREAD):
    t.Thread(target=isOpen,args=(int(i), int(i+FOR_EACH_THREAD - 1))).start()