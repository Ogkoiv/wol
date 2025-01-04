from send_package import construct_package
import socket
import sys
import uuid
import ipaddress

MASK='255.255.255.0'
broadcast_port=7

arg=sys.argv[1]

#sender functions opens udp socket and broadcastst
def sender(finalarray,broadcast_addr):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    udp_socket.sendto(finalarray, (broadcast_addr, broadcast_port))
    udp_socket.close()


#gets local ip
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

#get first interface mac addr
def gma():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    
    mac_address = ":".join([mac[e:e+2] for e in range(0, 12, 2)])
    
    return mac_address

myip = get_ip_address()
mymac = gma()


#getting brodcast addr
subnet = ipaddress.IPv4Network(myip + '/' + MASK, False)
broadcast_addr=str(subnet.broadcast_address)

if len(arg) > 8: # if there is mac addr as an arg
    finalarray=construct_package(arg)
    sender(finalarray,broadcast_addr)
    print("packet was sended to provided mac")
else:
    print("mac was not accessed")


