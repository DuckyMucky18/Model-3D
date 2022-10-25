import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hip, port))
port = 80
Hip = socket.gethostbyname("about://blank")
c, addr = s.accept()
var = "Obtaining ip address.... Connected successfuly"
new = var.encode("ascii")
c.send(new)
c.close()
