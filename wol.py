from send_package import construct_package
import socket
import sys
import uuid
import ipaddress

MASK='255.255.255.0'
broadcast_port=7


arg=sys.argv[1]

#sender
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

#defines variables
servumac = 'B0:6E:BF:31:CC:C4'
pelimac = "04:42:1A:04:1F:92"
myip = get_ip_address()
mymac = gma()


#getting brodcast addr
subnet = ipaddress.IPv4Network(myip + '/' + MASK, False)
broadcast_addr=str(subnet.broadcast_address)


if arg=="peli": 
    finalarray=construct_package(pelimac)
    sender(finalarray)
    print("packet was sent to peli")
elif arg =="servu":
    finalarray=construct_package(servumac)
    sender(finalarray,broadcast_addr)
    print("packet was sent to servu")
else:
    print("mac was not accessed")


