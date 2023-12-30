import socket


LOGO ="""
         _nnnn_
        dGGGGMMb
       @p~qp~~qMb
       M|@||@) M|
       @,----.JM|
      JS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMP|   .'
     `-'       `--' """
print(LOGO)
def is_port_open(host, port):
    
    s = socket.socket()
    s.settimeout(0.2)
    try:
        s.connect((host, port))
        s.close()
        return True
    except:
        return False  
     
ip = input("Enter ip address: ")
for port in range(0,65535):
    if is_port_open(ip, port):
        print(f"port {port} is open!")
    else:
        print(f"port {port} not open ")